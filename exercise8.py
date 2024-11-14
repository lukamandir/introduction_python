#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:37:13 2024

@author: lukamandir
"""

def vokon_zählen(x):
    vokale = "aeiou"
    x_lower = x.lower()
    
    buchstaben = [i for i in x_lower if i.isalpha()]
    vokale = [i for i in buchstaben if i in vokale]
    
    #return [len(buchstaben), len(vokale)]

    print(f"Es gibt {len(vokale)} Vokale und {len(buchstaben)} Konsonanten.")


vokon_zählen("HI,&%/ BerliN!!")