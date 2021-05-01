
"""
    All operations related to the management of customers for the boxdb-api.
"""

from resource import ResourceList


ARG_NAME = {
    'name': 'name',
    'params': {
        'type': str,
        'required': True,
        'help': 'Customer name',
        'location': 'json'
    }
}

ARG_BOXES = {
    'name': 'boxes',
    'params': {
        'type': list,
        'help': 'Customer\'s boxes',
        'location': 'json'
    }
}


class CustomerList(ResourceList):
    """
        RESTful API for "customers" as a list.
    """

    def __init__(self):
        arguments = [ARG_NAME, ARG_BOXES]
        super().__init__(arguments)


    def get(self):
        """
            RESTful GET method for custormers list.
        """
        customers = self.boxdb_database.get_customers()
        return {'customers': [customer['name'] for customer in customers]}

    def post(self):
        """
            RESTful POST method for customers list.
        """
        customer = self.reqparse.parse_args()
        customer['boxes'] = customer['boxes'] or []
        return_message = {
            'message': f'customer {customer["name"]} created.',
            'location': f'v1/customers/{customer["name"]}'
        }
        if self.boxdb_database.get_customer(customer['name']):
            return return_message, 201
        self.boxdb_database.add_customer(customer)
        return return_message, 200


class CustomerItem(ResourceList):
    """
        RESTful API for "customers" as an item.
    """

    def __init__(self):
        arguments = [ARG_BOXES]
        super().__init__(arguments)


    def get(self, customer_name):
        """
            RESTful GET method for customers item.
        """
        customer = self.boxdb_database.get_customer(customer_name)
        if customer:
            return {key:customer[key] for key in ('name', 'boxes')}
        return {'message': 'customer not found'}, 404

    def delete(self, customer_name):
        """
            RESTful DELETE method for customers item.
        """
        self.boxdb_database.del_customer(customer_name)
        return {'message': f'customer {customer_name} deleted.'}

    def put(self, customer_name):
        """
            RESTful PUT method for customers item.
        """
        customer = self.reqparse.parse_args()
        customer['name'] = customer_name
        if self.boxdb_database.get_customer(customer_name):
            self.boxdb_database.update_customer(customer_name, customer)
            return {'message': f'customer {customer_name} updated.'}
        return {'message': f'customer {customer_name} not found.'}, 404
