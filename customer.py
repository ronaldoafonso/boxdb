
from flask_restful import Resource
import json


CUSTOMER_DB = 'data/customer.json'
BOX_DB = 'data/box.json'


class CustomerList(Resource):

    def get(self):
        with open(CUSTOMER_DB) as customer_db:
            customers = json.load(customer_db)
        return {'customers': [customer for customer in customers.keys()]}

class CustomerItem(Resource):

    def get(self, customer):
        with open(CUSTOMER_DB) as customer_db:
            customers = json.load(customer_db)
        if customers.get(customer, None):
            return {'customer': customers[customer]}
        else:
            return {'message': 'customer not found'}, 404


class BoxItem(Resource):

    def get(self, customer, box):
        with open(CUSTOMER_DB) as customer_db:
            customers = json.load(customer_db)
        if customers.get(customer, None):
            if box in customers[customer]:
                with open(BOX_DB) as box_db:
                    boxes = json.load(box_db)
                return {'box': boxes[box]}
            else:
                return {'message': 'box not found'}, 404
        else:
            return {'message': 'customer not found'}, 404
