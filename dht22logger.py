#!/usr/bin/python3

# 20221027 Rui Rigel

import os
import time
import Adafruit_DHT
import subprocess
from dht22calcs import dewpoint, heatindex

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

t = round(temperature,1)
rh = round(humidity,1)
hi = round(heatindex(t,rh),1)

f = open('plot.txt', 'a+')

if humidity is not None and temperature is not None:
   f.write('{0},{1},{2:0.1f},{3:0.1f},{4},{5}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, round(dewpoint(t,rh),1), round(heatindex(t,rh),1)))
   subprocess.run(["gnuplot", "plot.conf"])
