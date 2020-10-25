
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var customers = boxdb.getCollection('customers')

customers.remove({name: 'z3n'})
