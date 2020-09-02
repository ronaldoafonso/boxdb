
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
