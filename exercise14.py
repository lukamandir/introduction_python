#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:44:33 2024

@author: lukamandir
"""
import numpy as np

y = [2,3,8,4,10,1,9,5,1,0,]

y_std = np.sqrt(1/len(y) * sum((y-np.mean(y))**2))

