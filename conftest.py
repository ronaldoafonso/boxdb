
from pytest import fixture
from os import system


@fixture()
def remove_customer_z3n_from_db():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_customer_z3n.js')

@fixture()
def add_customer_z3n_with_no_boxes_to_db():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customer_z3n_with_no_boxes.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_customer_z3n.js')

@fixture()
def add_customer_z3n_with_one_box():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customer_z3n_with_one_box.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_customer_z3n.js')

@fixture()
def add_customer_z3n_with_two_boxes():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customer_z3n_with_two_boxes.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_customer_z3n.js')

@fixture()
def add_customer_z3n_with_three_boxes():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customer_z3n_with_three_boxes.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_customer_z3n.js')

@fixture()
def add_customer_encoded_name_space():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customer_encoded_name_space.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_customer_encoded_name_space.js')

@fixture()
def remove_all_customers():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_customers.js')

@fixture()
def add_customers_one():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customers_one.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_customers.js')

@fixture()
def add_customers_two():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customers_two.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_customers.js')

@fixture()
def add_customers_three():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_customers_three.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_customers.js')

@fixture()
def remove_all_boxes():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')

@fixture()
def add_boxes_one():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_boxes_one.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')

@fixture()
def add_boxes_two():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_boxes_two.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')

@fixture()
def add_boxes_three():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_boxes_three.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')

@fixture()
def remove_box1_from_db():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_box1.js')

@fixture()
def add_box1_with_all_empty():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_box_all_empty.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')

@fixture()
def add_box1_with_ssid_and_macs():
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/add_box_ssid_macs.js')
    yield
    system('docker container exec boxdb_boxdb-mongo_1 mongo /root/data/remove_all_boxes.js')
