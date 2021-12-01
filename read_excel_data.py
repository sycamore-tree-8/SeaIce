# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:50:37 2021

@author: Professional
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_excel('../idata/kara_obs_8st.xlsx') #, dtype='int32')
print(df)

#построить графики
#перевести даты

y1 = df['FI']
y2 = df['AD']
y3 = df['LD']
y4 = df['CC']
x = df.index

print(df.describe())

plt.plot(x, y1, label='FI')
plt.plot(x, y2, label='AD', alpha=0.5)
plt.plot(x, y3, label='LD')
plt.plot(x, y4, label='CC')
plt.xlabel('frequency')
plt.ylabel('DOY')
plt.legend()
plt.show
  
cyear = df['YEAR']
doy = df['FI']    
full_date = pd.to_datetime('{}{}'.format(cyear, doy), format='%Y%j%d')
print(full_date)

#full_date = df['FI'].to_datetime('{}{}'.format(cyear, doy), format='%Y%j')
#print(full_date)