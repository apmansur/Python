#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:46:46 2019

@author: andreamansur
"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

d = random.sample(range(1,100), 10)
e = random.sample(range(1,100), 10)



def compareList(a,b):
    new_list = []
    for i in a:
        if i in b and i not in new_list:
            new_list.append(i)
    print new_list
            
            
compareList(d,e)

