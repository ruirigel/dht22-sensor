#!/usr/bin/python3

# 20221027 Rui Rigel

import os
import time
import subprocess
from dht22sensor import temperature, humidity, dewpoint, heatindex

f = open('plot.txt', 'a+')

if humidity is not None and temperature is not None:
   f.write('{0},{1},{2:0.1f},{3:0.1f},{4},{5}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), round(temperature(),1), round(humidity(),1), round(dewpoint(),1), round(heatindex(),1)))
   subprocess.run(["gnuplot", "plot.conf"])
