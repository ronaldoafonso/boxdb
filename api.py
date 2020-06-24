
import flask

import customer
import box


app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/v1/resources/customers', methods=['GET'])
def customers():
    if 'name' in flask.request.args:
        name = flask.request.args['name']
    else:
        return 'Error: no "name" field provides.'

    c = customer.Customer(name)
    return flask.jsonify(c.getBoxes())

@app.route('/v1/resources/boxes', methods=['GET'])
def boxes():
    if 'boxname' in flask.request.args:
        boxname = flask.request.args['boxname']
    else:
        return 'Error: no "boxname" field provides.'

    b = box.Box(boxname)
    return flask.jsonify(b.getConfig())

@app.route('/healthy', methods=['GET'])
def healthy():
    c = customer.Customer('healthy')
    return flask.jsonify(c.getBoxes())
