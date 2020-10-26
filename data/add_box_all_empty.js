
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var boxes = boxdb.getCollection('boxes')

boxes.insert({name: 'box1', 'owner': 'owner1', 'ssid': '', 'macs': []})
