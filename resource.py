
"""
    Implement a base class that should be used by any "resource" of the
    RESTful API.
"""

from flask_restful import Resource, reqparse
from db import Db


class ResourceList(Resource):
    """
        Base class for a resource of boxdb-api RESTful API.
    """

    def __init__(self, arguments):
        self.reqparse = reqparse.RequestParser()
        for argument in arguments:
            argument_name = argument['name']
            argument_params = argument['params']
            self.reqparse.add_argument(argument_name, **argument_params)
        self.boxdb_database = Db()
        super().__init__()
