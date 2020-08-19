
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')

boxdb.createCollection('boxes')
boxdb.createCollection('customers')
