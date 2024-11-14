#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:40:51 2024

@author: lukamandir
"""

a = 1
r = 0.5
s = 0
k = 0
limit = a/(1-r)
epsilon = 0.00001

while True:
    s += a * r**k
    k += 1
    print(s, end = " ")
    
    #if s == limit:
    # break

    if (limit - s) < epsilon:
        break
    