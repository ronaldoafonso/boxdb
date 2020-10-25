
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var customers = boxdb.getCollection('customers')

customers.insert({name: 'z3n', 'boxes': ['box1', 'box2', 'box3']})
