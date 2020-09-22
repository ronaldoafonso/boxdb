
import os

from flask_restful import Resource, reqparse
from pymongo import MongoClient


BOXDB_MONGO = os.getenv('BOXDB_MONGO')
BOXDB_MONGO_USERNAME = os.getenv('BOXDB_MONGO_USERNAME')
BOXDB_MONGO_PASSWORD = os.getenv('BOXDB_MONGO_PASSWORD')
BOXDB_MONGO_URL = 'mongodb://' + BOXDB_MONGO_USERNAME + ':' \
                               + BOXDB_MONGO_PASSWORD + '@' \
                               + BOXDB_MONGO

MONGO = MongoClient(BOXDB_MONGO_URL)


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
        super(BoxList, self).__init__()

    def get(self):
        boxes = MONGO.boxdb.boxes
        return {'boxes': [box['name'] for box in boxes.find()]}

    def post(self):
        box = self.reqparse.parse_args()
        box['ssid'] = box['ssid'] or ""
        box['macs'] = box['macs'] or []
        rc = {
            'message': f'box {box["name"]} created.',
            'location': f'v1/boxes/{box["name"]}'
        }
        boxes = MONGO.boxdb.boxes 
        if boxes.find_one({'name': box['name']}):
            return rc, 201
        boxes.insert_one(box)
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
        super(BoxItem, self).__init__()

    def get(self, box):
        _box = MONGO.boxdb.boxes.find_one({'name': box})
        if _box:
            return {
                'name': _box['name'],
                'owner': _box['owner'],
                'ssid': _box['ssid'],
                'macs': _box['macs']
            }
        else:
            return {'message': 'box not found'}, 404

    def delete(self, box):
        MONGO.boxdb.boxes.delete_one({'name': box})
        return {'message': f'box {box} deleted.'}

    def put(self, box):
        _box = self.reqparse.parse_args()
        _box['name'] = box
        _box['ssid'] = _box['ssid'] or ""
        _box['macs'] = _box['macs'] or []
        if MONGO.boxdb.boxes.find_one({'name': box}):
            MONGO.boxdb.boxes.update_one({'name': box}, {"$set": _box})
            return {'message': f'box {box} updated.'}
        return {'message': f'box {box} not found.'}, 404
