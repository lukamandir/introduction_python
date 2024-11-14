#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:11:54 2024

@author: lukamandir
"""


def buchstaben_zählen(x):
    x_list = list(x)
    x_buchstaben = [i for i in x_list if i.isalpha()]
    x_buchstaben_len = len(x_buchstaben)
    return x_buchstaben_len

print(buchstaben_zählen("Hallo, Berlin!"))

