
import os

from pymongo import MongoClient


BOXDB_MONGO = os.getenv('BOXDB_MONGO')
BOXDB_MONGO_USERNAME = os.getenv('BOXDB_MONGO_USERNAME')
BOXDB_MONGO_PASSWORD = os.getenv('BOXDB_MONGO_PASSWORD')
BOXDB_MONGO_URL = 'mongodb://' + BOXDB_MONGO_USERNAME + ':' \
                               + BOXDB_MONGO_PASSWORD + '@' \
                               + BOXDB_MONGO
                               

class Db:

    def __init__(self):
        mongo = MongoClient(BOXDB_MONGO_URL)
        self.customers = mongo.boxdb.customers
        self.boxes = mongo.boxdb.customers

    def get_customers(self):
        return self.customers.find()

    def get_customer(self, customer_name):
        return self.customers.find_one({'name': customer_name})

    def add_customer(self, customer):
        self.customers.insert_one(customer)

    def del_customer(self, customer_name):
        self.customers.delete_one({'name': customer_name})

    def update_customer(self, customer_name, new_customer):
        self.customers.update_one({'name': customer_name},
                                  {'$set': new_customer})

    def get_boxes(self):
        return self.boxes.find()

    def get_box(self, box_name):
        return self.boxes.find_one({'name': box_name})

    def add_box(self, box):
        self.boxes.insert_one(box)

    def del_box(self, box_name):
        self.boxes.delete_one({'name': box_name})

    def update_box(self, box_name, new_box):
        self.boxes.update_one({'name': box_name}, {'$set': new_box})
