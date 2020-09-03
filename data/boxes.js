
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var boxes = boxdb.getCollection('boxes')

var _boxes = [
    {
        name: 'box1',
        owner: 'customer1',
        ssid: 'ssid1',
        macs: [
            '11:11:11:11:11:11'
         ]
    },
    {
        name: 'box11',
        owner: 'customer1',
        ssid: 'ssid1',
        macs: [
            '11:11:11:11:11:11',
            '11:11:11:11:11:22'
        ]
    },
    {
        name: 'box2',
        owner: 'customer2',
        ssid: 'ssid2',
        macs: [
            '22:22:22:22:22:11',
            '22:22:22:22:22:22',
            '22:22:22:22:22:33'
        ]
    },
    {
        name: 'box22',
        owner: 'customer2',
        ssid: 'ssid2',
        macs: [
            '22:22:22:22:22:22'
        ]
    },
    {
        name: 'box one',
        owner: 'customer one',
        ssid: 'one',
        macs: [
        ]
    },
    {
        name: 'box one one',
        owner: 'customer one',
        ssid: 'one one',
        macs: [
            '11:11:11:11:11:11'
        ]
    },
    {
        name: 'box two two',
        owner: 'customer two',
        ssid: 'two two',
        macs: [
            '11:11:11:11:11:11',
            '22:22:22:22:22:22'
        ]
    }
]

for (var i in _boxes) {
    boxes.insert(_boxes[i])
}
