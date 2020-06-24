
import box
import customer


def test_get_customer1():
    c = customer.Customer('customer1')
    assert c.name == 'customer1'

def test_get_boxes_from_customer1():
    boxes = customer.Customer('customer1').getBoxes()
    assert boxes == [
        'box1',
        'box11'
    ]

def test_get_customer2():
    c = customer.Customer('customer2')
    assert c.name == 'customer2'

def test_get_boxes_from_customer1():
    boxes = customer.Customer('customer2').getBoxes()
    assert boxes == [
        'box2',
        'box22'
    ]
