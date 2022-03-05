#!/bin/bash
# -*- coding: utf-8 -*-

temp1=38 #$(((RANDOM % 5) + 40))
temp2=38 #$(((RANDOM % 5) + 40))

if [ -f /tmp/powermetrics.txt ]; then
    rm /tmp/powermetrics.txt
    mkfifo /tmp/powermetrics.txt
fi

if [ -z "$(ps -ef | grep -v grep | grep powermetrics)" ]; then
    echo "start powermetrics!"
    sudo powermetrics --sample-rate=500 -o /tmp/powermetrics.txt &
fi

while read -r data; do

    sensor1=$(echo $data | awk '/CPU die temperature/ {print $4}')
    if [ -z "$sensor1" ]; then
        continue
    fi

    #echo "#### $sensor1"

    #sensor1="$(($temp1 + (RANDOM % 5))).$(((RANDOM % 50) + 1))"
    sensor2="$(($temp2 + (RANDOM % 5))).$(((RANDOM % 50) + 1))"

    curl -X 'POST' 'http://causaefeito.rlrobotics.com:8000/api/v1/sensor' -H 'accept: application/json' -H   'Content-Type: application/json' -d "{
    \"name\": \"string\",
    \"sensor1\": $sensor1,
    \"sensor2\": $sensor2,
    \"description\": \"string\"}"

done < /tmp/powermetrics.txt