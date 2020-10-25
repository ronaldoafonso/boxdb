
from pytest import mark
import requests


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

    def test_get_customers_with_one_customer(self, add_customers_one):
        r = requests.get('http://localhost:5000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['customers'] == ['customer 1']

    def test_get_customers_with_two_customers(self, add_customers_two):
        r = requests.get('http://localhost:5000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['customers'] == ['customer 1', 'customer 2']

    def test_get_customers_with_three_customers(self, add_customers_three):
        r = requests.get('http://localhost:5000/v1/customers')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['customers'] == ['customer 1', 'customer 2', 'customer 3']
