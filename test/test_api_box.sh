#!/bin/bash -e

source ./test/test_api.sh


# Test - Get with no resource
do_test "GET" \
        "http://localhost:5000/v1/boxes/box1" \
        "" \
        "HTTP/1.0 404 NOT FOUND" \
        "Content-Type: application/json" \
        "{\"message\": \"box not found\"}"

# Test - Post box1
do_test "POST" \
        "http://localhost:5000/v1/boxes" \
        "{\"name\": \"box1\", \"owner\": \"owner1\"}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box box1 created.\", \"location\": \"v1/boxes/box1\"}"

# Test - Get box1 and should get a response now
do_test "GET" \
        "http://localhost:5000/v1/boxes/box1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"box1\", \"owner\": \"owner1\", \"ssid\": \"\", \"macs\": \[\]}"

# Test - Put box1 with an SSID ssid1
do_test "PUT" \
        "http://localhost:5000/v1/boxes/box1" \
        "{\"owner\": \"owner1\", \"ssid\": \"ssid1\", \"macs\": []}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box box1 updated.\"}"

# Test - Get box1 with SSID as ssid1 and no MACs
do_test "GET" \
        "http://localhost:5000/v1/boxes/box1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"box1\", \"owner\": \"owner1\", \"ssid\": \"ssid1\", \"macs\": \[\]}"

# Test - Put box1 with an SSID ssid1 and one MACs
do_test "PUT" \
        "http://localhost:5000/v1/boxes/box1" \
        "{\"owner\": \"owner1\", \"ssid\": \"ssid1\", \"macs\": [\"11:11:11:11:11:11\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box box1 updated.\"}"

# Test - Get box1 with SSID as ssid1 and one MACs
do_test "GET" \
        "http://localhost:5000/v1/boxes/box1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"box1\", \"owner\": \"owner1\", \"ssid\": \"ssid1\", \"macs\": \[\"11:11:11:11:11:11\"\]}"

# Test - Put box1 with an SSID ssid1 and two MACs
do_test "PUT" \
        "http://localhost:5000/v1/boxes/box1" \
        "{\"owner\": \"owner1\", \"ssid\": \"ssid1\", \"macs\": [\"11:11:11:11:11:11\", \"22:22:22:22:22:22\"]}" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box box1 updated.\"}"

# Test - Get box1 with SSID as ssid1 and two MACs
do_test "GET" \
        "http://localhost:5000/v1/boxes/box1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"name\": \"box1\", \"owner\": \"owner1\", \"ssid\": \"ssid1\", \"macs\": \[\"11:11:11:11:11:11\", \"22:22:22:22:22:22\"\]}"

# Test - Delete box1
do_test "DELETE" \
        "http://localhost:5000/v1/boxes/box1" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"message\": \"box box1 deleted.\"}"

# Test - Get a list of boxes
do_test "GET" \
        "http://localhost:5000/v1/boxes" \
        "" \
        "HTTP/1.0 200 OK" \
        "Content-Type: application/json" \
        "{\"boxes\": \[\]}"

BOXES="box1 \
       box2 \
       box3"

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
        "{\"boxes\": \[\"box1\", \"box2\", \"box3\"\]}"

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
