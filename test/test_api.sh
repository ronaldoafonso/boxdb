#!/bin/bash 

function do_test {
    METHOD="$1"
    URL="$2"
    INPUT="$3"
    HTTP_CODE="$4"
    CONTENT_TYPE="$5"
    MESSAGE="$6"

    TMPFILE="/tmp/boxdb_test.tmp"

    curl -s -i -o $TMPFILE \
         -H 'Content-Type: application/json' \
         -T - \
         -X $METHOD \
         $URL <<__END__
    $INPUT
__END__

    ERROR=false

    if ! grep -q "$HTTP_CODE" $TMPFILE; then
        echo "Wrong HTTP Response Code." && ERROR=true
    elif ! grep -q "$CONTENT_TYPE" $TMPFILE; then
        echo "Not 'application/json'" && ERROR=true
    elif ! grep -q "$MESSAGE" $TMPFILE; then
        echo "Wrong returned message." && ERROR=true
    fi

    $ERROR && cat $TMPFILE
    rm -f $TMPFILE
}
