
from flask import Flask
from flask_restful import Api

import customer


app = Flask(__name__)
api = Api(app)

api.add_resource(customer.CustomerList, '/v1/customers')
api.add_resource(customer.CustomerItem, '/v1/<string:customer>')
api.add_resource(customer.BoxItem, '/v1/<string:customer>/<string:box>')


#@app.route('/healthy', methods=['GET'])
#def healthy():
#    c = customer.Customer('healthy')
#    return flask.jsonify(c.getBoxes())
