#!/bin/sh

curl http://$(minikube ip):8080/v1/customers
curl http://$(minikube ip):8080/v1/boxes
