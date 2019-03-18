#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:29:41 2019

@author: andreamansur
"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression


boston = load_boston()
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos['PRICE'] = boston.target

X = bos.drop('PRICE', axis = 1)

model = LinearRegression()

model.fit(X, bos.PRICE)

model.intercept_

pd.DataFrame(zip(X.columns, model.coef_), columns = ['features', 'R-factor'])

prediction = model.predict(X)

plt.subplot(211)
plt.scatter(bos.RM, bos.PRICE)
plt.xlabel("RM")
plt.ylabel("PRICE")

plt.subplot(212)
plt.scatter(bos.PRICE, prediction)
plt.xlabel("Prices")
plt.ylabel("Predicted Price ")
plt.show()

meansqRoot = np.mean((bos.PRICE - prediction) ** 2)

print meansqRoot
