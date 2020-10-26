
from pytest import mark
import requests
import subprocess
import json


@mark.customer
@mark.get
class TestCustomerGet:

    def test_get_non_existing_customer(self, remove_customer_z3n_from_db):
        r = requests.get('http://localhost:5000/v1/customers/z3n')
        rbody = r.json()
        assert r.status_code == 404
        assert rbody['message'] == 'customer not found'

    def test_get_an_existing_customer_with_empty_boxes(self, add_customer_z3n_with_no_boxes_to_db):
        r = requests.get('http://localhost:5000/v1/customers/z3n')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'z3n'
        assert rbody['boxes'] == []

    def test_get_an_existing_customer_with_one_box(self, add_customer_z3n_with_one_box):
        r = requests.get('http://localhost:5000/v1/customers/z3n')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'z3n'
        assert rbody['boxes'] == ['box1']

    def test_get_an_existing_customer_with_two_boxes(self, add_customer_z3n_with_two_boxes):
        r = requests.get('http://localhost:5000/v1/customers/z3n')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'z3n'
        assert rbody['boxes'] == ['box1', 'box2']

    def test_get_an_existing_customer_with_three_boxes(self, add_customer_z3n_with_three_boxes):
        r = requests.get('http://localhost:5000/v1/customers/z3n')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'z3n'
        assert rbody['boxes'] == ['box1', 'box2', 'box3']

    def test_get_customer_with_a_space_in_the_name(self, add_customer_encoded_name_space):
        r = requests.get('http://localhost:5000/v1/customers/z3n%20z3n')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'z3n z3n'

    def test_get_customers_empty(self, remove_all_customers):
        r = requests.get('http://localhost:5000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['customers'] == []

    def test_get_customers_with_one_customer(self, remove_all_customers, add_customers_one):
        r = requests.get('http://localhost:5000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['customers'] == ['customer 1']

    def test_get_customers_with_two_customers(self, remove_all_customers, add_customers_two):
        r = requests.get('http://localhost:5000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['customers'] == ['customer 1', 'customer 2']

    def test_get_customers_with_three_customers(self, remove_all_customers, add_customers_three):
        r = requests.get('http://localhost:5000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'

@mark.customer
@mark.post
class TestCustomerPost:

    def test_post_customer_with_no_box(self, remove_all_customers):
        r = requests.post('http://localhost:5000/v1/customers', json={'name': 'customer 1'})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker container exec boxdb_boxdb-mongo_1 mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == []

    def test_post_customer_with_one_box(self, remove_all_customers):
        r = requests.post('http://localhost:5000/v1/customers', json={'name': 'customer 1', 'boxes': ['box1']})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker container exec boxdb_boxdb-mongo_1 mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == ['box1']

    def test_post_customer_with_two_boxes(self, remove_all_customers):
        r = requests.post('http://localhost:5000/v1/customers', json={'name': 'customer 1', 'boxes': ['box1', 'box2']})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker container exec boxdb_boxdb-mongo_1 mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == ['box1', 'box2']

    def test_post_customer_that_already_exists(self, remove_all_customers, add_customers_one):
        r = requests.post('http://localhost:5000/v1/customers', json={'name': 'customer 1', 'boxes': []})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker container exec boxdb_boxdb-mongo_1 mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 201
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == []
