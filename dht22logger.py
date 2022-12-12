# 20221027 Rui Rigel

import os
import time
import Adafruit_DHT
import subprocess
import numpy as np

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

def dewpoint_approximation(T,RH):
    Td = (b * gamma(T,RH)) / (a - gamma(T,RH))
    return Td

def gamma(T,RH):
    g = (a * T / (b + T)) + np.log(RH/100.0)
    return g

f = open('plot.txt', 'a+')

if humidity is not None and temperature is not None:

   a = 17.271
   b = 237.7

   T = temperature
   RH = humidity

   Td = dewpoint_approximation(T,RH)

   f.write('{0},{1},{2:0.1f},{3:0.1f},{4}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, round(Td,1)))

   subprocess.run(["gnuplot", "plot.conf"])

