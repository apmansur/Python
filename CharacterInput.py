#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:21:04 2019

@author: andreamansur
"""
import datetime

now = datetime.datetime.now()
age = int(input("What is your age: "))
repeat = int(input('how many times should I say it: '))

year100 = (100 - age) + now.year

for i in range(repeat):
    print 'You will be 100 in ' + str(year100) + '\n'


