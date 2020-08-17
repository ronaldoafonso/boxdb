
var mongo = new Mongo('mongodb://mongo:mongo@localhost')
var boxdb = mongo.getDB('boxdb')

var boxdbUser = {
    user: 'boxdb',
    pwd: 'boxdb',
    roles: [
      'readWrite'
    ]
}
boxdb.createUser(boxdbUser)

boxdb.createCollection('boxes')
boxdb.createCollection('customers')
