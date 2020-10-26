
var mongo = new Mongo('mongodb://boxdb:boxdb@localhost')
var boxdb = mongo.getDB('boxdb')
var boxes = boxdb.getCollection('boxes')

boxes.insert({name: 'box1', 'owner': 'owner ', 'ssid': 'ssid1', 'macs': []})
boxes.insert({name: 'box2', 'owner': 'owner ', 'ssid': 'ssid2', 'macs': []})
boxes.insert({name: 'box3', 'owner': 'owner ', 'ssid': 'ssid3', 'macs': []})
