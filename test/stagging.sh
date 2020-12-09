#!/bin/sh

curl http://$(minikube ip):30000/v1/customers
curl http://$(minikube ip):30000/v1/boxes
