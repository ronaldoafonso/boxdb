#!/bin/sh

ITEM="$1"

# GET /v1/<customer> -> {'customer': ['box1', 'box2']}
curl -v http://localhost:5000/v1/$ITEM
