#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:55:15 2019

@author: andreamansur
"""

import pandas as pd
import numpy as np

#set dataframe equal to the csv file to be cleaned
#look at head() or if using IDE view in variable explorer


df = pd.read_csv('BL-Flickr-Images-Book.csv')

#setting index does not guarentee uniqueness
df.set_index('Identifier', inplace=True)

#several columns are not needed 

col_drop = ['Edition Statement',
            'Corporate Author',
            'Corporate Contributors',
          'Former owner',
           'Engraver',
            'Contributors',
           'Issuance type',
           'Shelfmarks']

# col_drop = labels or name of row/columns to drop
#axis 0 would be index, 1 is columns
#can use level attribute to do multi level drop
#inplace true returns none and has the changes made in the object itself
# can also do columns = col_drop

df.drop(col_drop, inplace= True, axis=1)


#can access locations via index because of set_index used earlier
#print df.loc[206]

df.get_dtype_counts()

#standardize dates by taking first 4 numbers and replacing values which do not have 4 number with NAN
#create seperate variable at first to ensure changes are correct
#then correct dataframe
extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

#ensure correct data type
df['Date of Publication'] = pd.to_numeric(extr)



pub = df['Place of Publication']
london = pub.str.contains('London')
oxford = pub.str.contains('Oxford')

df['Place of Publication'] = np.where(london, 'London',
                                          np.where(oxford, 'Oxford',
                                             pub.str.replace('-', ' ')))

#how to use applymap function

university_towns = []
with open ('university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            state = line
        else:
            university_towns.append((state, line))

towns_df = pd.DataFrame(university_towns,
                      columns=['State', 'RegionName'])

#now apply map can be used to remove () and [] from place names
#first create a function to do so

def get_citystate(item):
    if '(' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

#then use apply map to run above function across the dataframe and replace vaulues
        
towns_df = towns_df.applymap(get_citystate)

#rename columns
olympics_df = pd.read_csv('olympics.csv', header=1)

new_names =  {'Unnamed: 0': 'Country',
              '? Summer': 'Summer Olympics',
              '01 !': 'Gold',
              '02 !': 'Silver',
             '03 !': 'Bronze',
               '? Winter': 'Winter Olympics',
              '01 !.1': 'Gold.1',
              '02 !.1': 'Silver.1',
               '03 !.1': 'Bronze.1',
               '? Games': '# Games',
              '01 !.2': 'Gold.2',
               '02 !.2': 'Silver.2',
               '03 !.2': 'Bronze.2'}

olympics_df.rename(columns=new_names, inplace=True)