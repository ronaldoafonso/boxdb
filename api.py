
"""
    The main RESTfull API module for boxdb-api.
    This is where all the "endpoints" are defined and routed.
"""

from flask import Flask
from flask_restful import Api

import customer
import box


app = Flask(__name__)
api = Api(app)

api.add_resource(customer.CustomerList, '/v1/customers')
api.add_resource(customer.CustomerItem, '/v1/customers/<string:customer_name>')
api.add_resource(box.BoxList, '/v1/boxes')
api.add_resource(box.BoxItem, '/v1/boxes/<string:box_name>')


#@app.route('/healthy', methods=['GET'])
#def healthy():
#    c = customer.Customer('healthy')
#    return flask.jsonify(c.getBoxes())
