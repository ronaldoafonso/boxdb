#!/bin/sh

CUSTOMER="$1"
BOX="$2"

# GET /v1/<customer>/<box> -> {
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
curl -v http://localhost:5000/v1/$CUSTOMER/$BOX
