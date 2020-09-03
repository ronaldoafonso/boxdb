#!/bin/sh

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


BOXES="box1 \
       box11 \
       box2 \
       box22 \
       box%20one \
       box%20one%20one \
       box%20two%20two"

for BOX in $BOXES
do
    curl http://localhost:5000/v1/box/$BOX
done
