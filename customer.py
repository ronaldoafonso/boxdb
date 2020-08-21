
from flask_restful import Resource
from pymongo import MongoClient


# DOTO: Maybe it could be a 'singleton'
MONGO = MongoClient('mongodb://boxdb:boxdb@boxdb_mongo_1')

class CustomerList(Resource):

    def get(self):
        customers = MONGO.boxdb.customers
        return {'customers': [customer['name'] for customer in
                              customers.find()]}

class CustomerItem(Resource):

    def get(self, customer):
        _customer = MONGO.boxdb.customers.find_one({'name': customer})
        if _customer:
            return {'name': _customer['name'], 'boxes': _customer['boxes']}
        return {'message': 'customer not found'}, 404


class BoxItem(Resource):

    def get(self, customer, box):
        _customer = MONGO.boxdb.customers.find_one({'name': customer})
        if _customer:
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
        else:
            return {'message': 'customer not found'}, 404
