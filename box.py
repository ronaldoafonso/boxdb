
from flask_restful import Resource, reqparse
from pymongo import MongoClient

from db import Db


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
        super(BoxItem, self).__init__()

    def get(self, box):
        _box = self.db.get_box(box)
        if _box:
            return {key:_box[key] for key in ('name',
                                              'owner',
                                              'ssid',
                                              'macs')}
        else:
            return {'message': 'box not found'}, 404

    def delete(self, box):
        self.db.del_box(box)
        return {'message': f'box {box} deleted.'}

    def put(self, box):
        _box = self.reqparse.parse_args()
        _box['name'] = box
        _box['ssid'] = _box['ssid'] or ""
        _box['macs'] = _box['macs'] or []
        if self.db.get_box(box):
            self.db.update_box(box, _box)
            return {'message': f'box {box} updated.'}
        return {'message': f'box {box} not found.'}, 404
