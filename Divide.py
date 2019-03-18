#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:41:55 2019

@author: andreamansur
"""

number = int(input('Give me a number: '))
divisor =[]
test = range(2,number)

for i in test:
    if number%i == 0:
        divisor.append(i)
        
print divisor