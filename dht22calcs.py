#!/usr/bin/python3

# 20221027 Rui Rigel

import sys
import numpy as np

a = 17.271
b = 237.7

def dewpoint(T,RH):
    dp = (b * gamma(T,RH)) / (a - gamma(T,RH))
    return dp

def gamma(T,RH):
    g = (a * T / (b + T)) + np.log(RH/100.0)
    return g

def heatindex(T,RH):
    T = (T * 1.8) + 32

    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783e-3
    c6 = -5.481717e-2
    c7 = 1.22874e-3
    c8 = 8.5282e-4
    c9 = -1.99e-6

    T = float(T)
    RH = float(RH)

    p1 = c1 + c2 * T + c3*RH
    p2 = c4*T*RH + c5*T**2 + c6*RH**2
    p3 = c7*T**2*RH + c8*T*RH**2 + c9*T**2*RH**2
    hi = p1 + p2 + p3

    hi = (hi - 32)/1.8
    return hi
