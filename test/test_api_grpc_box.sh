#!/bin/bash -e

curl -s -i -o /tmp/grpc.tmp \
     -H 'Content-Type: application/json' \
     -T - \
     -X POST \
     http://localhost:5000/v1/boxes<<__END__
{
    "name": "788a20298f81.z3n.com.br",
    "owner": "z3n",
    "ssid": "z3n",
    "macs": [
        "11:11:11:11:11:11",
        "11:11:11:11:11:22"
    ]
}
__END__
