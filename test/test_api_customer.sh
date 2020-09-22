#!/bin/bash -e

source ./test/test_api.sh

# Test - Get with no resource
do_test "GET" \
        "http://localhost:5000/v1/customers/customer1" \
        "" \
        "HTTP/1.0 404 NOT FOUND" \
        "Content-Type: application/json" \
        "{\"message\": \"customer not found\"}"

# Test - Post customer1
do_test "POST" \
        "http://localhost:5000/v1/customers" \
        "{\"name\": \"customer1\"}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer customer1 created.\", \"location\": \"v1/customers/customer1\"}"

# Test - Get customer1
do_test "GET" \
        "http://localhost:5000/v1/customers/customer1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"customer1\", \"boxes\": \[\]}"

# Test - Put customer1 with box1
do_test "PUT" \
        "http://localhost:5000/v1/customers/customer1" \
        "{\"boxes\": [\"box1\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer customer1 updated.\"}"

# Test - Get customer1 and box1
do_test "GET" \
        "http://localhost:5000/v1/customers/customer1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"customer1\", \"boxes\": \[\"box1\"\]}"

# Test - Put box11 to customer1
do_test "PUT" \
        "http://localhost:5000/v1/customers/customer1" \
        "{\"boxes\": [\"box1\", \"box11\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer customer1 updated.\"}"

# Test - Get customer1 with box1 and box11
do_test "GET" \
        "http://localhost:5000/v1/customers/customer1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"customer1\", \"boxes\": \[\"box1\", \"box11\"\]}"

# Test - Delete customer1
do_test "DELETE" \
        "http://localhost:5000/v1/customers/customer1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"customer customer1 deleted.\"}"

# Test - Get a list of customers
do_test "GET" \
        "http://localhost:5000/v1/customers" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"customers\": \[\]}"

CUSTOMERS="customer1 \
           customer2 \
           customer3"

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
        "{\"customers\": \[\"customer1\", \"customer2\", \"customer3\"\]}"

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
