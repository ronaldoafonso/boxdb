
from flask_restful import Resource, reqparse

from db import Db


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
        self.db = Db()
        super(CustomerList, self).__init__()


    def get(self):
        customers = self.db.get_customers()
        return {'customers': [customer['name'] for customer in customers]}

    def post(self):
        customer = self.reqparse.parse_args()
        customer['boxes'] = customer['boxes'] or []
        rc = {
            'message': f'customer {customer["name"]} created.',
            'location': f'v1/customers/{customer["name"]}'
        }
        if self.db.get_customer(customer['name']):
            return rc, 201
        self.db.add_customer(customer)
        return rc, 200


class CustomerItem(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('boxes',
                                    type=list,
                                    required=True,
                                    help='Customer\'s boxes',
                                    location='json')
        self.db = Db()
        super(CustomerItem, self).__init__()


    def get(self, customer):
        _customer = self.db.get_customer(customer)
        if _customer:
            return {'name': _customer['name'], 'boxes': _customer['boxes']}
        return {'message': 'customer not found'}, 404

    def delete(self, customer):
        self.db.del_customer(customer)
        return {'message': f'customer {customer} deleted.'}

    def put(self, customer):
        _customer = self.reqparse.parse_args()
        _customer['name'] = customer
        if self.db.get_customer(customer):
            self.db.update_customer(customer, _customer)
            return {'message': f'customer {customer} updated.'}
        return {'message': f'customer {customer} not found.'}, 404
