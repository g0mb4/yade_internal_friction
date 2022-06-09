#!/bin/bash

if [[ -f "/usr/bin/yadedaily" ]]; then
    YADE="/usr/bin/yadedaily"
elif [[ -f "/usr/bin/yade" ]]; then
    YADE="/usr/bin/yade"
else
    echo "no yade found"
    exit 1
fi

if [[ ! -f "data.csv" ]]; then
    echo "date;time;X;Y;Z" > data.csv
fi

if [[ $# -eq 0 ]]; then
    $YADE -j $(nproc --all) visual.py
else
    for (( i=0; i<$1; ++i )); do
        $YADE -j $(nproc --all) -x -n batch.py
    done
fi