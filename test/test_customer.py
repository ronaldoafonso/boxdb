
from pytest import mark
import requests
import subprocess
import json


@mark.customer
@mark.get
class TestCustomerGet:

    def test_get_all_customer_empty(self, remove_all_customers):
        r = requests.get('http://localhost:30000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert rbody['customers'] == []

    def test_get_all_customers_with_one_customer(self, remove_all_customers, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': ['box1']}])
        r = requests.get('http://localhost:30000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert rbody['customers'] == ['customer 1']

    def test_get_all_customers_with_two_customer(self, remove_all_customers, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': ['box1']},
                           {'name': 'customer2', 'boxes': ['box1', 'box2']}])
        r = requests.get('http://localhost:30000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert rbody['customers'] == ['customer 1', 'customer2']

    def test_get_non_existing_customer(self, remove_all_customers):
        r = requests.get('http://localhost:30000/v1/customers/customer%201')
        rbody = r.json()
        assert r.status_code == 404
        assert rbody['message'] == 'customer not found'

    def test_get_existing_customer_with_no_boxes(self, remove_all_customers, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': []}])
        r = requests.get('http://localhost:30000/v1/customers/customer%201')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'customer 1'
        assert rbody['boxes'] == []

    def test_get_existing_customer_with_one_box(self, remove_all_customers, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': ['box1']}])
        r = requests.get('http://localhost:30000/v1/customers/customer%201')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'customer 1'
        assert rbody['boxes'] == ['box1']

    def test_get_existing_customer_with_two_boxes(self, remove_all_customers, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': ['box1', 'box2']}])
        r = requests.get('http://localhost:30000/v1/customers/customer%201')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'customer 1'
        assert rbody['boxes'] == ['box1', 'box2']


@mark.customer
@mark.post
class TestCustomerPost:

    def test_post_customer_with_no_box(self, remove_all_customers):
        r = requests.post('http://localhost:30000/v1/customers', json={'name': 'customer 1'})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == []

    def test_post_customer_with_one_box(self, remove_all_customers):
        r = requests.post('http://localhost:30000/v1/customers', json={'name': 'customer 1', 'boxes': ['box1']})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == ['box1']

    def test_post_customer_with_two_boxes(self, remove_all_customers):
        r = requests.post('http://localhost:30000/v1/customers', json={'name': 'customer 1', 'boxes': ['box1', 'box2']})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == ['box1', 'box2']

    def test_post_customer_that_already_exists(self, remove_all_customers, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': ['box1']}])
        r = requests.post('http://localhost:30000/v1/customers', json={'name': 'customer 1', 'boxes': []})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 201
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 created.'
        assert rbody['location'] == 'v1/customers/customer 1'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == ['box1']


@mark.customer
@mark.put
class TestCustomerPut:

    def test_put_an_non_existing_customer(self, remove_all_customers):
        r = requests.put('http://localhost:30000/v1/customers/customer%201', json={'boxes': ['box1']})
        rbody = r.json()
        assert r.status_code == 404
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 not found.'

    def test_put_a_customer_without_boxes(self, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': []}])
        r = requests.put('http://localhost:30000/v1/customers/customer%201', json={'boxes': ['box1']})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 updated.'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == ['box1']

    def test_put_a_customer_with_one_box(self, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': ['box1']}])
        r = requests.put('http://localhost:30000/v1/customers/customer%201', json={'boxes': ['box1', 'box2']})
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 updated.'
        assert rdata['name'] == 'customer 1'
        assert rdata['boxes'] == ['box1', 'box2']


@mark.customer
@mark.delete
class TestCustomerDelete:

    def test_delete_an_non_existing_customer(self, remove_all_customers):
        r = requests.delete('http://localhost:30000/v1/customers/customer%201')
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 deleted.'
        assert rdata == None

    def test_delete_an_existing_customer(self, add_customers):
        add_customers.add([{'name': 'customer 1', 'boxes': ['box1']}])
        r = requests.delete('http://localhost:30000/v1/customers/customer%201')
        rbody = r.json()
        rdata = json.loads(subprocess.check_output('docker-compose exec -T boxdb-mongo mongo --quiet --eval \'var customer="customer 1"\' /root/data/check_customer.js', shell=True))
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['message'] == 'customer customer 1 deleted.'
        assert rdata == None
