
"""
    All operations related to the management of boxes for the boxdb-api.
"""

from resource import ResourceList


ARG_NAME = {
    'name': 'boxname',
    'params': {
        'type': str,
        'required': True,
        'help': 'Box name',
        'location': 'json'
    }
}

ARG_OWNER = {
    'name': 'owner',
    'params': {
        'type': str,
        'required': True,
        'help': 'Box owner\'s name',
        'location': 'json'
    }
}

ARG_SSID = {
    'name': 'ssid',
    'params': {
        'type': str,
        'help': 'Box SSID',
        'location': 'json'
    }
}

ARG_MACS = {
    'name': 'macs',
    'params': {
        'type': list,
        'help': 'Allowed MACs for the box',
        'location': 'json'
    }
}


class BoxList(ResourceList):
    """
        RESTful API for "boxes" as a list.
    """

    def __init__(self):
        arguments = [ARG_NAME, ARG_OWNER, ARG_SSID, ARG_MACS]
        super().__init__(arguments)

    def get(self):
        """
            RESTful GET method for boxes list.
        """
        boxes = self.boxdb_database.get_boxes()
        return {'boxes': [box['boxname'] for box in boxes]}

    def post(self):
        """
            RESTful POST method for boxes list.
        """
        box = self.reqparse.parse_args()
        box['ssid'] = box['ssid'] or ""
        box['macs'] = box['macs'] or []
        return_message = {
            'message': f'box {box["boxname"]} created.',
            'location': f'v1/boxes/{box["boxname"]}'
        }
        if self.boxdb_database.get_box(box['boxname']):
            return return_message, 201
        self.boxdb_database.add_box(box)
        return return_message, 200


class BoxItem(ResourceList):
    """
        RESTful API for "boxes" as an item.
    """

    def __init__(self):
        arguments = [ARG_OWNER, ARG_SSID, ARG_MACS]
        super().__init__(arguments)

    def get(self, box_name):
        """
            RESTful GET method for boxes items.
        """
        box = self.boxdb_database.get_box(box_name)
        if box:
            return {key:box[key] for key in ('boxname', 'owner', 'ssid', 'macs')}
        return {'message': 'box not found'}, 404

    def delete(self, box_name):
        """
            RESTful DELETE method for boxes items.
        """
        self.boxdb_database.del_box(box_name)
        return {'message': f'box {box_name} deleted.'}

    def put(self, box_name):
        """
            RESTful PUT method for boxes items.
        """
        box = self.reqparse.parse_args()
        box['boxname'] = box_name
        box['ssid'] = box['ssid'] or ""
        box['macs'] = box['macs'] or []
        if self.boxdb_database.get_box(box_name):
            self.boxdb_database.update_box(box_name, box)
            return {'message': f'box {box_name} updated.'}
        return {'message': f'box {box_name} not found.'}, 404
