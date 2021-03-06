#!/bin/bash
# -*- coding: utf-8 -*-

temp1=$(((RANDOM % 10) + 40))
temp2=$(((RANDOM % 10) + 30))

while [ 1 ]; do

    sensor1="$(($temp1 + (RANDOM % 5))).$(((RANDOM % 50) + 1))"
    sensor2="$(($temp2 + (RANDOM % 5))).$(((RANDOM % 50) + 1))"

    curl -X 'POST' 'http://causaefeito.rlrobotics.com:8000/api/v1/sensor' -H 'accept: application/json' -H   'Content-Type: application/json' -d "{
    \"name\": \"string\",
    \"sensor1\": $sensor1,
    \"sensor2\": $sensor2,
    \"description\": \"string\"}"

    sleep 0.5
done