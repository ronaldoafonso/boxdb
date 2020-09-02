
import os

from flask_restful import Resource
from pymongo import MongoClient


BOXDB_MONGO = os.getenv('BOXDB_MONGO')
BOXDB_MONGO_USERNAME = os.getenv('BOXDB_MONGO_USERNAME')
BOXDB_MONGO_PASSWORD = os.getenv('BOXDB_MONGO_PASSWORD')
BOXDB_MONGO_URL = 'mongodb://' + BOXDB_MONGO_USERNAME + ':' \
                               + BOXDB_MONGO_PASSWORD + '@' \
                               + BOXDB_MONGO

MONGO = MongoClient(BOXDB_MONGO_URL)


class BoxList(Resource):

    def get(self):
        boxes = MONGO.boxdb.boxes
        return {'boxes': [box['name'] for box in boxes.find()]}


class BoxItem(Resource):

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
