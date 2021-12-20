# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:30:19 2021

@author: Professional
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate

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

#place = 'МарреСале'
place = 'Усть-Кара'
year = 2012
a = df.query("point == @place and year == @year")
print(a)

#assert 1==2

for place in places:
    for year in years:

#        year = 2012
#        place = 'МарреСале'
         
        code = {'W': 0, 'I': 1, 'N': -1}
        df = df.replace(dict.fromkeys(['value'], code))
        
        new = df.query("point == @place and year == @year")
        new.reset_index(drop=True, inplace=True)
        new['tdate'] = pd.to_datetime(new.loc[:, 'date'].values, format='%Y%m%d')
    
        new['jdate'] = new['tdate'].dt.strftime('%j')
        
        #ts = pd.Series(new['value'].values, index=new['date'].values,
        #               reset_index=True)
        
        ii = np.where(new['value'].values == 0)[0]
    
        #print(df)
        
        if len(ii):
            start = new.loc[ii[0], 'tdate']
            sd = int(new.loc[ii[0], 'jdate']) #start.strftime('%j'))
            end = new.loc[ii[-1], 'tdate']
            ed = int(new.loc[ii[-1], 'jdate']) #end.strftime('%j'))
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

info = {'Year':df0['year'], 'Start Date (DoY)': df0['sdate'], 'End Date (DoY)': df0['edate'], 'Duration (days)': df0['dur']}
print(tabulate(info, headers='keys', tablefmt='fancy_grid'))

df0.to_csv('db_8_places_ifp.csv', sep=';') 



