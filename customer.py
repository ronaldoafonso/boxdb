
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


class CustomerList(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name',
                                    type=str,
                                    required=True,
                                    help='Customer name',
                                    location='json')
        self.reqparse.add_argument('boxes',
                                    type=list,
                                    help='Customer\'s boxes',
                                    location='json')
        super(CustomerList, self).__init__()


    def get(self):
        customers = MONGO.boxdb.customers
        return {'customers': [customer['name'] for customer in
                              customers.find()]}

    def post(self):
        customer = self.reqparse.parse_args()
        customer['boxes'] = customer['boxes'] or []
        rc = {
            'message': f'customer {customer["name"]} created.',
            'location': f'v1/customers/{customer["name"]}'
        }
        customers = MONGO.boxdb.customers
        if customers.find_one({'name': customer['name']}):
            return rc, 201
        customers.insert_one(customer)
        return rc, 200


class CustomerItem(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('boxes',
                                    type=list,
                                    required=True,
                                    help='Customer\'s boxes',
                                    location='json')
        super(CustomerItem, self).__init__()


    def get(self, customer):
        _customer = MONGO.boxdb.customers.find_one({'name': customer})
        if _customer:
            return {'name': _customer['name'], 'boxes': _customer['boxes']}
        return {'message': 'customer not found'}, 404

    def delete(self, customer):
        MONGO.boxdb.customers.delete_one({'name': customer})
        return {'message': f'customer {customer} deleted.'}

    def put(self, customer):
        _customer = self.reqparse.parse_args()
        _customer['name'] = customer
        if MONGO.boxdb.customers.find_one({'name': customer}):
            MONGO.boxdb.customers.update_one({'name': customer}, {"$set": _customer})
            return {'message': f'customer {customer} updated.'}
        return {'message': f'customer {customer} not found.'}, 404
