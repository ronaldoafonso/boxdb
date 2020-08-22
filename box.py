
from flask_restful import Resource
from pymongo import MongoClient


# DOTO: Maybe it could be a 'singleton'
MONGO = MongoClient('mongodb://boxdb:boxdb@boxdb_mongo_1')


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
