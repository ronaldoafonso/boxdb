#!/bin/sh

# GET /v1/boxes -> {
#    'boxes': [
#        'box1,
#        'box11,
#        'box2',
#        'box22'
#    ]
#}
curl -v http://localhost:5000/v1/boxes
