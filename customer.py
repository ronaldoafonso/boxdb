
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


    def get(self, customer_name):
        customer = self.db.get_customer(customer_name)
        if customer:
            return {key:customer[key] for key in ('name', 'boxes')}
        return {'message': 'customer not found'}, 404

    def delete(self, customer_name):
        self.db.del_customer(customer_name)
        return {'message': f'customer {customer_name} deleted.'}

    def put(self, customer_name):
        customer = self.reqparse.parse_args()
        customer['name'] = customer_name
        if self.db.get_customer(customer_name):
            self.db.update_customer(customer_name, customer)
            return {'message': f'customer {customer_name} updated.'}
        return {'message': f'customer {customer_name} not found.'}, 404
