#!/bin/bash

name="co2.raspberrypi"
val=`sudo /usr/bin/python3 /opt/co2sensor/co2sensor.py`
date=`env TZ=JST date +%s`

echo -e "${name}\t${val}\t${date}"
