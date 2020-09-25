#!/bin/bash -e

source ./test/test_api.sh


# Test - Get with no resource
do_test "GET" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "" \
        "HTTP/1.0 404 NOT FOUND" \
        "Content-Type: application/json" \
        "{\"message\": \"box not found\"}"

# Test - Post 788a20298f81.z3n.com.br
do_test "POST" \
        "http://localhost:5000/v1/boxes" \
        "{\"name\": \"788a20298f81.z3n.com.br\", \"owner\": \"z3n\"}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box 788a20298f81.z3n.com.br created.\", \"location\": \"v1/boxes/788a20298f81.z3n.com.br\"}"

# Test - Get 788a20298f81.z3n.com.br and should get a response now
do_test "GET" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"788a20298f81.z3n.com.br\", \"owner\": \"z3n\", \"ssid\": \"\", \"macs\": \[\]}"

# Test - Put 788a20298f81.z3n.com.br with an SSID ssid1
do_test "PUT" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "{\"owner\": \"z3n\", \"ssid\": \"ssid1\", \"macs\": []}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box 788a20298f81.z3n.com.br updated.\"}"

# Test - Get 788a20298f81.z3n.com.br with SSID as ssid1 and no MACs
do_test "GET" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"788a20298f81.z3n.com.br\", \"owner\": \"z3n\", \"ssid\": \"ssid1\", \"macs\": \[\]}"

# Test - Put 788a20298f81.z3n.com.br with an SSID ssid1 and one MACs
do_test "PUT" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "{\"owner\": \"z3n\", \"ssid\": \"ssid1\", \"macs\": [\"11:11:11:11:11:11\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box 788a20298f81.z3n.com.br updated.\"}"

# Test - Get 788a20298f81.z3n.com.br with SSID as ssid1 and one MACs
do_test "GET" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"788a20298f81.z3n.com.br\", \"owner\": \"z3n\", \"ssid\": \"ssid1\", \"macs\": \[\"11:11:11:11:11:11\"\]}"

# Test - Put 788a20298f81.z3n.com.br with an SSID ssid1 and two MACs
do_test "PUT" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "{\"owner\": \"z3n\", \"ssid\": \"ssid1\", \"macs\": [\"11:11:11:11:11:11\", \"22:22:22:22:22:22\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box 788a20298f81.z3n.com.br updated.\"}"

# Test - Get 788a20298f81.z3n.com.br with SSID as ssid1 and two MACs
do_test "GET" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"788a20298f81.z3n.com.br\", \"owner\": \"z3n\", \"ssid\": \"ssid1\", \"macs\": \[\"11:11:11:11:11:11\", \"22:22:22:22:22:22\"\]}"

# Test - Delete 788a20298f81.z3n.com.br
do_test "DELETE" \
        "http://localhost:5000/v1/boxes/788a20298f81.z3n.com.br" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box 788a20298f81.z3n.com.br deleted.\"}"

# Test - Get a list of boxes
do_test "GET" \
        "http://localhost:5000/v1/boxes" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"boxes\": \[\]}"

BOXES="788a20298f81.z3n.com.br"

for BOX in $BOXES
do
    curl -s -i -o /dev/null \
         -H 'Content-Type: application/json' \
         -T - \
         -X POST \
         http://localhost:5000/v1/boxes<<__END__
{
    "name": "$BOX",
    "owner": "owner",
    "ssid": "ssid",
    "macs": []
}
__END__
done

do_test "GET" \
        "http://localhost:5000/v1/boxes" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"boxes\": \[\"788a20298f81.z3n.com.br\"\]}"

for BOX in $BOXES
do
    curl -s -i -o /dev/null \
         -X DELETE \
         http://localhost:5000/v1/boxes/$BOX
done

do_test "GET" \
        "http://localhost:5000/v1/boxes" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"boxes\": \[\]}"
