#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:27:36 2019

@author: andreamansur
"""

number = int(input('give me a number: '))
div = int(input('what should I divide by: '))

if number%div == 0 :
    print 'divisible by' + str(div)
else:
    print 'not divisible by ' + str(div)