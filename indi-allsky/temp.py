#!/usr/bin/env python3

import urllib.request
import re

link = urllib.request.urlopen("http://192.168.1.65:8000/dht22values")
text = link.read().decode()
parts = text.split(',')

file="temp.txt"
f = open(file, "w")
f.write("\nInside the OBS: \nTemp " +  parts[2] + "\nHum " +  parts[3])
