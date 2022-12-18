#!/usr/bin/python3

# 20221027 Rui Rigel

import sys
import numpy as np
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

RH, T = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

def temperature():
    t = T
    return t

def humidity():
    rh = RH
    return rh

a = 17.271
b = 237.7

def dewpoint():
    dp = (b * gamma(T,RH)) / (a - gamma(T,RH))
    return dp

def gamma(T,RH):
    g = (a * T / (b + T)) + np.log(RH/100.0)
    return g

def heatindex():
    t = (T * 1.8) + 32

    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783e-3
    c6 = -5.481717e-2
    c7 = 1.22874e-3
    c8 = 8.5282e-4
    c9 = -1.99e-6

    tr = float(t)
    rhr = float(RH)

    p1 = c1 + c2 * t + c3*rhr
    p2 = c4*tr*rhr + c5*tr**2 + c6*rhr**2

    p1 = c1 + c2 * tr + c3*rhr
    p2 = c4*tr*rhr + c5*tr**2 + c6*rhr**2
    p3 = c7*tr**2*rhr + c8*tr*rhr**2 + c9*tr**2*rhr**2
    hi = p1 + p2 + p3

    hi = (hi - 32)/1.8
    return hi

