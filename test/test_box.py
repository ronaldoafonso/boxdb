
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

    def test_get_all_boxes_with_one_box(self, remove_all_boxes, add_boxes):
        add_boxes.add([{'name': 'box1', 'owner': 'owner1', 'ssid': '', 'macs': []}])
        r = requests.get('http://localhost:5000/v1/boxes')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['boxes'] == ['box1']

    def test_get_all_boxes_with_two_boxes(self, remove_all_boxes, add_boxes):
        add_boxes.add([{'name': 'box1', 'owner': 'owner1', 'ssid': '', 'macs': []},
                       {'name': 'box2', 'owner': 'owner2', 'ssid': '', 'macs': []}])
        r = requests.get('http://localhost:5000/v1/boxes')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['boxes'] == ['box1', 'box2']

    def test_get_all_boxes_with_three_boxes(self, remove_all_boxes, add_boxes):
        add_boxes.add([{'name': 'box1', 'owner': 'owner1', 'ssid': '', 'macs': []},
                       {'name': 'box2', 'owner': 'owner2', 'ssid': '', 'macs': []},
                       {'name': 'box3', 'owner': 'owner3', 'ssid': '', 'macs': []}])
        r = requests.get('http://localhost:5000/v1/boxes')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['boxes'] == ['box1', 'box2', 'box3']

    def test_get_a_non_existing_box(self, remove_all_boxes):
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 404
        assert rbody['message'] == 'box not found'

    def test_get_an_existing_box_with_no_configuration(self, add_boxes):
        add_boxes.add([{'name': 'box1', 'owner': 'owner1', 'ssid': '', 'macs': []}])
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'box1'
        assert rbody['owner'] == 'owner1'
        assert rbody['ssid'] == ''
        assert rbody['macs'] == []

    def test_get_an_existing_box_with_ssid(self, add_boxes):
        add_boxes.add([{'name': 'box1', 'owner': 'owner1', 'ssid': 'ssid1', 'macs': []}])
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'box1'
        assert rbody['owner'] == 'owner1'
        assert rbody['ssid'] == 'ssid1'
        assert rbody['macs'] == []

    def test_get_an_existing_box_with_macs(self, add_boxes):
        macs = ['11:11:11:11:11:11', '22:22:22:22:22:22']
        add_boxes.add([{'name': 'box1', 'owner': 'owner1', 'ssid': '', 'macs': macs}])
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'box1'
        assert rbody['owner'] == 'owner1'
        assert rbody['ssid'] == ''
        assert rbody['macs'] == macs

    def test_get_an_existing_box_with_ssid_and_macs(self, add_boxes):
        ssid = 'ssid 1'
        macs = ['11:11:11:11:11:11', '22:22:22:22:22:22']
        add_boxes.add([{'name': 'box1', 'owner': 'owner1', 'ssid': ssid, 'macs': macs}])
        r = requests.get('http://localhost:5000/v1/boxes/box1')
        rbody = r.json()
        assert r.status_code == 200
        assert r.headers['content-type'] == 'application/json'
        assert rbody['name'] == 'box1'
        assert rbody['owner'] == 'owner1'
        assert rbody['ssid'] == ssid
        assert rbody['macs'] == macs
