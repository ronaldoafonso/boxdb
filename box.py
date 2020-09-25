
from flask_restful import Resource, reqparse
from pymongo import MongoClient

from db import Db
from boxcmd import BoxCmd


class BoxList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name',
                                    type=str,
                                    required=True,
                                    help='Box name',
                                    location='json')
        self.reqparse.add_argument('owner',
                                    type=str,
                                    required=True,
                                    help='Box owner\'s name',
                                    location='json')
        self.reqparse.add_argument('ssid',
                                    type=str,
                                    help='Box SSID',
                                    location='json')
        self.reqparse.add_argument('macs',
                                    type=list,
                                    help='Allowed MACs for the box',
                                    location='json')
        self.db = Db()
        self.cmd = BoxCmd()
        super(BoxList, self).__init__()

    def get(self):
        boxes = self.db.get_boxes()
        return {'boxes': [box['name'] for box in boxes]}

    def post(self):
        box = self.reqparse.parse_args()
        box['ssid'] = box['ssid'] or ""
        box['macs'] = box['macs'] or []
        rc = {
            'message': f'box {box["name"]} created.',
            'location': f'v1/boxes/{box["name"]}'
        }
        if self.db.get_box(box['name']):
            return rc, 201
        self.db.add_box(box)
        self.cmd.exec_cmd(box)
        return rc, 200


class BoxItem(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('owner',
                                    type=str,
                                    required=True,
                                    help='Box owner\'s name',
                                    location='json')
        self.reqparse.add_argument('ssid',
                                    type=str,
                                    help='Box SSID',
                                    location='json')
        self.reqparse.add_argument('macs',
                                    type=list,
                                    help='Allowed MACs for the box',
                                    location='json')
        self.db = Db()
        self.cmd = BoxCmd()
        super(BoxItem, self).__init__()

    def get(self, box_name):
        box = self.db.get_box(box_name)
        if box:
            return {key:box[key] for key in ('name', 'owner', 'ssid', 'macs')}
        return {'message': 'box not found'}, 404

    def delete(self, box_name):
        self.db.del_box(box_name)
        return {'message': f'box {box_name} deleted.'}

    def put(self, box_name):
        box = self.reqparse.parse_args()
        box['name'] = box_name
        box['ssid'] = box['ssid'] or ""
        box['macs'] = box['macs'] or []
        if self.db.get_box(box_name):
            self.db.update_box(box_name, box)
            self.cmd.exec_cmd(box)
            return {'message': f'box {box_name} updated.'}
        return {'message': f'box {box_name} not found.'}, 404
