#!/bin/bash

MINIKUBE=$(minikube ip)

curl -v \
     -H 'Content-Type: application/json' \
     -T - \
     -X POST \
     http://$MINIKUBE:30000/v1/customers<<__END__
{
    "name": "z3n",
    "boxes": [
        "788a20298f81.z3n.com.br"
    ]
}
__END__

curl -v \
     -H 'Content-Type: application/json' \
     -T - \
     -X POST \
     http://$MINIKUBE:30000/v1/boxes<<__END__
{
    "name": "788a20298f81.z3n.com.br",
    "owner": "z3n",
    "ssid": "z3ntest",
    "macs": [
        "11:11:11:11:11:11",
        "11:11:11:11:11:22",
        "11:11:11:11:11:33"
    ]
}
__END__
