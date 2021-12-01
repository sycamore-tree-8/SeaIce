# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:50:37 2021

@author: Professional
"""

import calendar
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

meta = pd.read_excel('../idata/db_ice_stations.xlsx', sheet_name=None)
print(meta)

assert 1==2

df_dict = pd.read_excel('../idata/kara_obs_8st.xlsx', sheet_name=None) #, dtype='int32')

for key in sorted(list(df_dict.keys()))[:]:
    df = df_dict[key]
    print(df)



    #построить графики
    #перевести даты
    
    y1 = df['FI']
    y2 = df['AD']
    y3 = df['LD']
    y4 = df['CC']
    x = df.index
    
    print(df.describe())
    
    fig = plt.figure(figsize=(8, 6))
    
    plt.plot(x, y1, label='FI')
    plt.plot(x, y2, label='AD', alpha=0.5)
    plt.plot(x, y3, label='LD')
    plt.plot(x, y4, label='CC')
    plt.xlabel('frequency')
    plt.ylabel('DOY')
    plt.title('{}'.format(key))
    plt.legend()
    
    plt.show()
    
    new = df.dropna()
    new = new[['FI', 'YEAR']].copy()
    
    for i, row in new.iterrows():
        if calendar.isleap(row['YEAR']):
            tr = 366
        else:
            tr = 365
        if row['FI'] > tr:
            new.loc[i, 'YEAR'] += 1
            new.loc[i, 'FI'] -= tr 
    
    
    cyear = new['YEAR'].astype('int32').values
    doy = new['FI'].astype('int').values
    box = [str('{}{}'.format(iyear, idoy)) for iyear, idoy in zip(cyear, doy)]
    full_date = pd.to_datetime(box, format='%Y%j')
