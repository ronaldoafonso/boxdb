
"""
    All data base operations for boxdb-api.
"""

import os
from pymongo import MongoClient


BOXDB_MONGO = os.getenv('BOXDB_MONGO')
BOXDB_MONGO_USERNAME = os.getenv('BOXDB_MONGO_USERNAME')
BOXDB_MONGO_PASSWORD = os.getenv('BOXDB_MONGO_PASSWORD')
BOXDB_MONGO_URL = 'mongodb://' + BOXDB_MONGO_USERNAME + ':' \
                               + BOXDB_MONGO_PASSWORD + '@' \
                               + BOXDB_MONGO

class Db:
    """
        Manage database operations.
    """

    def __init__(self):
        mongo = MongoClient(BOXDB_MONGO_URL)
        self.customers = mongo.boxdb.customers
        self.boxes = mongo.boxdb.boxes

    def get_customers(self):
        """
            Return a list of customers storaged in the database.
        """
        return self.customers.find()

    def get_customer(self, customer_name):
        """
            Return a customer seached using the customer name.
        """
        return self.customers.find_one({'name': customer_name})

    def add_customer(self, customer):
        """
            Store a customer into the database.
        """
        self.customers.insert_one(customer)

    def del_customer(self, customer_name):
        """
            Delete a customer from the database.
        """
        self.customers.delete_one({'name': customer_name})

    def update_customer(self, customer_name, new_customer):
        """
            Update a user into the database.
        """
        self.customers.update_one({'name': customer_name},
                                  {'$set': new_customer})

    def get_boxes(self):
        """
            Return a list of boxes storaged in the database.
        """
        return self.boxes.find()

    def get_box(self, box_name):
        """
            Return a box seached using the box name.
        """
        return self.boxes.find_one({'boxname': box_name})

    def add_box(self, box):
        """
            Store a box into the database.
        """
        self.boxes.insert_one(box)

    def del_box(self, box_name):
        """
            Delete a box from the database.
        """
        self.boxes.delete_one({'boxname': box_name})

    def update_box(self, box_name, new_box):
        """
            Update a box into the database.
        """
        self.boxes.update_one({'boxname': box_name}, {'$set': new_box})
