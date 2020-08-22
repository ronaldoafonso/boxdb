#!/bin/sh

CUSTOMER="$1"

# GET /v1/customers/<customer> -> {
#    'name': 'customer',
#    'boxes': [
#        'box1',
#        'box2'
#    ]
#}
curl -v http://localhost:5000/v1/customer/$CUSTOMER
