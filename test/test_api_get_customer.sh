#!/bin/sh -e

# GET /v1/customers/<customer> -> {
#    'name': 'customer',
#    'boxes': [
#        'box1',
#        'box2'
#    ]
#}

CUSTOMERS="customer1 \
           customer2 \
           customer%20one \
           customer%20two%20two"

for CUSTOMER in $CUSTOMERS
do
    curl http://localhost:5000/v1/customer/$CUSTOMER
done
