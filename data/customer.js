
var mongo = new Mongo('mongodb://mongo:mongo@localhost')
var boxdb = mongo.getDB('boxdb')
var customers = boxdb.getCollection('customers')

var customer1 = [
    {
        name: 'box1',
        ssid: 'ssid1',
        macs: [
            '11:11:11:11:11:11'
         ]
    },
    {
        name: 'box11',
        ssid: 'ssid1',
        macs: [
            '11:11:11:11:11:11',
            '11:11:11:11:11:22'
        ]
    }
]
customers.insert({customer1: customer1})

var customer2 = [
    {
        name: 'box2',
        ssid: 'ssid2',
        macs: [
            '22:22:22:22:22:11',
            '22:22:22:22:22:22',
            '22:22:22:22:22:33'
        ]
    },
    {
        name: 'box22',
        ssid: 'ssid2',
        macs: [
            '22:22:22:22:22:22'
        ]
    }
]
customers.insert({customer2: customer2})
