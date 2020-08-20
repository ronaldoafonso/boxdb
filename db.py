
from pymongo import MongoClient


class Database:

    def __init__(self):
        self.mongo = MongoClient('mongodb://boxdb:boxdb@boxdb_mongo_1')
        self.boxdb = self.mongo.boxdb

    def getAllCustomers(self):
        return {'customers': [customer['name'] for customer in
                              self.boxdb.customers.find()]}

    def getCustomer(self, name):
        customer = self.boxdb.customers.find_one({'name': name})
        return {
            'name': customer['name'],
            'boxes': customer['boxes']
        }

    def getBox(self, boxname):
        box = self.boxdb.boxes.find_one({'name': boxname})
        return {
            'name': box['name'],
            'owner': box['owner'],
            'ssid': box['ssid'],
            'macs': box['macs']
        }


if __name__ == '__main__':
    db = Database()
    print('getAllCustomers', db.getAllCustomers())
    print('getCustomer', db.getCustomer('customer1'))
    print('getCustomer', db.getCustomer('customer2'))
    print('getBox', db.getBox('box1'))
    print('getBox', db.getBox('box11'))
    print('getBox', db.getBox('box2'))
    print('getBox', db.getBox('box22'))
