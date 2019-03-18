#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:36:11 2019

@author: andreamansur
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new =[]
ask = int(input('give me a number: '))

for i in a:
    if i < ask:
        new.append(i)
print new