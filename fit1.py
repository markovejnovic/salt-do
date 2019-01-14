#!/usr/bin/env python

import numpy as np
from scipy.optimize import curve_fit

X = np.array([
    0.00,
    6.05,
    11.87,
    18.01,
    23.99,
    30.01
])

Y = np.array([
    2.36,
    1.85,
    1.60,
    1.45,
    1.19,
    1.09
]) * 0.01

def fit_func(x, a, b, c):
    return a * x ** 2 + b * x + c
    
fx = np.linspace(0, 40, 100)
fparams, fcovariances = curve_fit(fit_func, X, Y)
print(fparams)