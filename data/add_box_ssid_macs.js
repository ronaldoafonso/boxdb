
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var boxes = boxdb.getCollection('boxes')

boxes.insert({name: 'box1', 'owner': 'owner1', 'ssid': 'ssid1', 'macs': ['11:11:11:11:11:11', '22:22:22:22:22:22']})
