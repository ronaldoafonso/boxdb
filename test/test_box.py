
from pytest import mark
import requests
import subprocess
import json


@mark.box
@mark.get
class TestBoxGet:

    def test_get_boxes_empty(self, remove_all_boxes):
        r = requests.get('http://localhost:5000/v1/boxes')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['boxes'] == []

    def test_get_boxes_with_one_box(self, remove_all_boxes, add_boxes_one):
        r = requests.get('http://localhost:5000/v1/boxes')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['boxes'] == ['box1']

    def test_get_boxes_with_two_boxes(self, remove_all_boxes, add_boxes_two):
        r = requests.get('http://localhost:5000/v1/boxes')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['boxes'] == ['box1', 'box2']

    def test_get_boxes_with_three_boxes(self, remove_all_boxes, add_boxes_three):
        r = requests.get('http://localhost:5000/v1/boxes')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['boxes'] == ['box1', 'box2', 'box3']

    def test_get_non_existing_box(self, remove_box1_from_db):
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 404
        assert rbody['message'] == 'box not found'

    def test_get_an_existing_box_with_all_empty(self, add_box1_with_all_empty):
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'box1'
        assert rbody['owner'] == 'owner1'
        assert rbody['ssid'] == ''
        assert rbody['macs'] == []

    def test_get_an_existing_box_with_ssid_and_macs(self, add_box1_with_ssid_and_macs):
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'box1'
        assert rbody['owner'] == 'owner1'
        assert rbody['ssid'] == 'ssid1'
        assert rbody['macs'] == ['11:11:11:11:11:11', '22:22:22:22:22:22']
