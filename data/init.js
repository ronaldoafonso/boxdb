
var mongo = new Mongo('mongodb://mongo:mongo@localhost')
var boxdb = mongo.getDB('boxdb')

boxdb.createCollection('customers')
