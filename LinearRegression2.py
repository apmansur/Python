#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:01:50 2019

@author: andreamansur
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('lsd.csv')

#np.newaxis increases the dimension of existing array, this is needed
#because x values must be in 2D array for .fit(). comment out below to see
#difference between x1 and X 
#x1 = data['Tissue Concentration'].values
X = data['Tissue Concentration'].values[:,np.newaxis]

y = data['Test Score'].values


model = LinearRegression()
model.fit(X,y)
print model.score(X,y)

plt.scatter(X, y, color='r')
plt.plot(X, model.predict(X), color='k')
