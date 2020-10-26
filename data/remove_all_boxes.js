
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var boxes = boxdb.getCollection('boxes')

boxes.remove({})
