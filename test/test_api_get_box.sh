#!/bin/sh

BOX="$1"

# GET /v1/box/<box> -> {
#   {
#       'name': 'boxname',
#       'owner': 'box owner',
#       'ssid': 'ssid',
#       "macs": [
#            "11:11:11:11:11:11",
#            "11:11:11:11:11:22"
#       ]
#   }
#}
curl -v http://localhost:5000/v1/box/$BOX
