#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:37:31 2019

@author: andreamansur

experiment to prove central limit theorem
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


 #set number of simultions
n = 1000

#store the 
avg =[]

#rememeber range is inclusive for start number and exlusive for end
for i in range (1, n):
    #simulate dice by setting potential range 1-7 (7 exclusive) and 10 rolls per
    #simultion
    a = np.random.randint(1, 7, 10)
    #take average of simulaition and add it to avg defined above
    avg.append(np.average(a))
    
#print avg[1:10] #uncomment to check if above is working

#create histogram for simultions    
def clt(current):
    plt.cla()
    #stop animation at set number of simulations
    if current == n:
        a.event_source.stop()
    
    plt.hist(avg[0:current])
    

    plt.gca().set_title('Expected value of die rolls')
    plt.gca().set_xlabel('Average from die roll')
    plt.gca().set_ylabel('Frequency')

    plt.annotate('Die roll = {}'.format(current), [3,27])
    
fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval=1)


