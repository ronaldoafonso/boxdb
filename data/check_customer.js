
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var customers = boxdb.getCollection('customers')

var result = customers.findOne({name: customer})
print(JSON.stringify(result))
