#!/bin/sh

python -m grpc_tools.protoc \
       -I=./gcommand \
       --python_out=. \
       --grpc_python_out=. \
       ./gcommand/gcommand.proto 
