#!/bin/bash -e

function do_test {
    module="$1"
    arg="$2"

    curl http://localhost:5000/v1/resources/${module}?${arg}
}

do_test "customers" "name=customer1"
do_test "customers" "name=customer2"

do_test "boxes" "boxname=box1"
do_test "boxes" "boxname=box11"
do_test "boxes" "boxname=box2"
do_test "boxes" "boxname=box22"
