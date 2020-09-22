
from flask import Flask
from flask_restful import Api

import customer
import box


app = Flask(__name__)
api = Api(app)

api.add_resource(customer.CustomerList, '/v1/customers')
api.add_resource(customer.CustomerItem, '/v1/customers/<string:customer>')
api.add_resource(box.BoxList, '/v1/boxes')
api.add_resource(box.BoxItem, '/v1/boxes/<string:box>')


#@app.route('/healthy', methods=['GET'])
#def healthy():
#    c = customer.Customer('healthy')
#    return flask.jsonify(c.getBoxes())
