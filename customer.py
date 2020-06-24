
import json


DB = 'data/customer.json'
DB_MODE = 'r'


class Customer:

    def __init__(self, name):
        self.name = name
        self.boxes = {}

    def getBoxes(self):
        with open(DB, DB_MODE) as db:
            boxes = json.load(db)
        return boxes[self.name]
