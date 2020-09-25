#!/bin/bash -e

source ./test/test_api.sh

# Test - Get with no resource
do_test "GET" \
        "http://localhost:5000/v1/customers/z3n1" \
        "" \
        "HTTP/1.0 404 NOT FOUND" \
        "Content-Type: application/json" \
        "{\"message\": \"customer not found\"}"

# Test - Post z3n1
do_test "POST" \
        "http://localhost:5000/v1/customers" \
        "{\"name\": \"z3n1\"}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer z3n1 created.\", \"location\": \"v1/customers/z3n1\"}"

# Test - Get z3n1
do_test "GET" \
        "http://localhost:5000/v1/customers/z3n1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"z3n1\", \"boxes\": \[\]}"

# Test - Put z3n1 with 788a20298f81.z3n.com.br
do_test "PUT" \
        "http://localhost:5000/v1/customers/z3n1" \
        "{\"boxes\": [\"788a20298f81.z3n.com.br\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer z3n1 updated.\"}"

# Test - Get z3n1 and 788a20298f81.z3n.com.br
do_test "GET" \
        "http://localhost:5000/v1/customers/z3n1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"z3n1\", \"boxes\": \[\"788a20298f81.z3n.com.br\"\]}"

# Test - Put box11 to z3n1
do_test "PUT" \
        "http://localhost:5000/v1/customers/z3n1" \
        "{\"boxes\": [\"788a20298f81.z3n.com.br\", \"box11\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer z3n1 updated.\"}"

# Test - Get z3n1 with 788a20298f81.z3n.com.br and box11
do_test "GET" \
        "http://localhost:5000/v1/customers/z3n1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"z3n1\", \"boxes\": \[\"788a20298f81.z3n.com.br\", \"box11\"\]}"

# Test - Delete z3n1
do_test "DELETE" \
        "http://localhost:5000/v1/customers/z3n1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer z3n1 deleted.\"}"

# Test - Get a list of customers
do_test "GET" \
        "http://localhost:5000/v1/customers" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"customers\": \[\]}"

CUSTOMERS="z3n1 \
           z3n2 \
           z3n3"

for CUSTOMER in $CUSTOMERS
do
    curl -s -i -o /dev/null \
         -H 'Content-Type: application/json' \
         -T - \
         -X POST \
         http://localhost:5000/v1/customers<<__END__
{
    "name": "$CUSTOMER",
    "boxes": [
        "box$CUSTOMER",
        "boxbox"
    ]
}
__END__
done

do_test "GET" \
        "http://localhost:5000/v1/customers" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"customers\": \[\"z3n1\", \"z3n2\", \"z3n3\"\]}"

for CUSTOMER in $CUSTOMERS
do
    curl -s -i -o /dev/null \
         -X DELETE \
         http://localhost:5000/v1/customers/$CUSTOMER
done

do_test "GET" \
        "http://localhost:5000/v1/customers" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"customers\": \[\]}"
