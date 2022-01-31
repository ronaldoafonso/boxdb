#!/bin/sh

PORT="30000"

curl http://$(minikube ip):$PORT/v1/customers
curl http://$(minikube ip):$PORT/v1/boxes
