
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var customers = boxdb.getCollection('customers')

var _customers = [
    {
        name: 'customer1',
        boxes: [
            'box1',
            'box11'
        ]
    },
    {
        name: 'customer2',
        boxes: [
            'box2',
            'box22'
        ]
    },
    {
        name: 'customer one',
        boxes: [
            'box one',
            'box one one'
        ]
    },
    {
        name: 'customer two two',
        boxes: [
            'box two',
            'box two two '
        ]
    }
]

for (var i in _customers) {
    customers.insert(_customers[i])
}
