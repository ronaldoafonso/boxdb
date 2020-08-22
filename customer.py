
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
