#!/bin/sh

# GET /v1/customers -> {
#    'customers': [
#        'customer1,
#        'customer2,
#        'customer3'
#    ]
#}
curl -v http://localhost:5000/v1/customers
