
var mongo = new Mongo('localhost')
var boxdb = mongo.getDB('boxdb')

var boxdbUser = {
    user: 'boxdb',
    pwd: 'boxdb',
    roles: [
      'readWrite'
    ]
}
boxdb.createUser(boxdbUser)
