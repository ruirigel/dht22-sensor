# 20221027 Rui Rigel

import os
import time
import Adafruit_DHT
import subprocess

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

f = open('/home/pi/dht22_server/plot.txt', 'a+')
if os.stat('/home/pi/dht22_server/plot.txt').st_size == 0:
            print("Logging.")

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperature is not None:
    f.write('{0},{1},{2:0.1f},{3:0.1f}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
    subprocess.run(["gnuplot", "/home/pi/dht22_server/plot.conf"])

else:
    print("Failed to retrieve data from humidity sensor")
