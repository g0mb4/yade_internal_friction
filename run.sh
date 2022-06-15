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
    echo "date;time;radius;friction_angle;X;Y;Z;approx_angle" > data.csv
fi

if [[ $# -eq 0 ]]; then
    $YADE -j $(nproc --all) visual.py
else
    for (( i=0; i<$1; ++i )); do
        if [[ $# -eq 2 ]]; then
            if [ "$2" = "t" ]; then
                $YADE-batch --job-threads $(nproc --all) params.table batch.py
            else
                echo "unknow argument: $2"
                exit 1
            fi
        else
            $YADE -j $(nproc --all) -x -n batch.py
        fi
    done
fi