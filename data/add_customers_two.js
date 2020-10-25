
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var customers = boxdb.getCollection('customers')

customers.insert({name: 'customer 1', 'boxes': []})
customers.insert({name: 'customer 2', 'boxes': []})
