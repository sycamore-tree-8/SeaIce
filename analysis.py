# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:30:19 2021

@author: Professional
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Professional\Sea_ice\SeaIce\final_data.csv', 
                       sep = ';', 
                       index_col = 0)
print(df)

places = df['point'].unique()
years = range(1998, 2022)
#cyear = 2000
#place = 'м.Стерлегова'

i = 0
df0 = pd.DataFrame(np.zeros((len(places) * len(years), 7)))

place = 'МарреСале'
year = 2012
a = df.query("point == @place and year == @year")
print(a)

assert 1==2

for place in places:
    for year in years:

#        year = 2012
#        place = 'МарреСале'
         
        new = df.query("point == @place and year == @year")
        new.reset_index(drop=True, inplace=True)
        new['tdate'] = pd.to_datetime(new.loc[:, 'date'].values, format='%Y%m%d')
        #ts = pd.Series(new['value'].values, index=new['date'].values,
        #               reset_index=True)
        ii = np.where(new['value'].values == 'W')[0]
        
        if len(ii):
            start = new.loc[ii[0], 'tdate']
            sd = int(start.strftime('%j'))
            end = new.loc[ii[-1], 'tdate']
            ed = int(end.strftime('%j'))
            duration = (end-start).days
        else:
            start = -99
            end = -99
            duration = -99
            sd = -99
            ed = -99
        
        out = (place, year, start, sd, 
               end, ed, duration)
        
        df0.iloc[i, :] = out
        i += 1
        
#        plt.figure()
#        plt.plot()
#        plt.show()
df0.columns = ['name', 'year', 's', 'sdate', 'e', 'edate', 'dur']
df0.to_csv('db_8_places_ifp.csv', sep=';') 


