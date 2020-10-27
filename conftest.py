
from pytest import fixture
from os import system


class DataCustomers:

    def add(self, customers):
        for customer in customers:
            cmd = f'docker container exec boxdb_boxdb-mongo_1 mongo --eval "var customer = {customer}" /root/data/add_customer.js'
            system(cmd)


@fixture()
def remove_all_customers():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_customers.js')

@fixture()
def add_customers():
    yield DataCustomers()
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_customers.js')


class DataBoxes:

    def add(self, boxes):
        for box in boxes:
            cmd = f'docker container exec boxdb_boxdb-mongo_1 mongo --eval "var box = {box}" /root/data/add_box.js'
            system(cmd)


@fixture()
def remove_all_boxes():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')

@fixture()
def add_boxes():
    yield DataBoxes()
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')
