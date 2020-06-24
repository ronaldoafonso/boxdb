
import json


DB = 'data/box.json'
DB_MODE = 'r'


class Box:

    def __init__(self, boxname):
        self.boxname = boxname 

    def getConfig(self):
        with open(DB, DB_MODE) as db:
            config = json.load(db)
        return config[self.boxname]
