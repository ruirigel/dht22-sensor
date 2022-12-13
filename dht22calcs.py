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

