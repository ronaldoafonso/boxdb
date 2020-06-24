
import box


def test_box1():
    box1 = box.Box('box1')
    assert box1.boxname == 'box1'

def test_box1_get_config():
    config = box.Box('box1').getConfig()
    assert config == {
        'ssid': 'ssid1',
        'macs': [
            '11:11:11:11:11:11',
            '11:11:11:11:11:22'
        ]
    }

def test_box2():
    box2 = box.Box('box2')
    assert box2.boxname == 'box2'

def test_box2_get_config():
    config = box.Box('box2').getConfig()
    assert config == {
        'ssid': 'ssid2',
        'macs': [
            '22:22:22:22:22:11',
            '22:22:22:22:22:22',
            '22:22:22:22:22:33'
        ]
    }
