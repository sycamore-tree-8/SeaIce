# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:03:40 2021

@author: Professional
"""
import os
import time

import numpy as np
import pandas as pd

import geopandas


def func_open_shp_file(df, full_path_to_file):


    xp = df.Latitude
    yp = df.Longitude
    
    g = geopandas.GeoDataFrame(df, 
                               geometry=geopandas.points_from_xy(xp, yp),
                               crs=4326)
    g1 = g.to_crs(3576)
    gdf = geopandas.read_file(full_path_to_file)
    
    out = {}
    for i, row in df.iterrows():
        p1 = g1.iloc[i, -1]
        dists = gdf.distance(p1).sort_values()
        ii = dists.index[0]
#        print(i, ii)
        
        res = gdf.loc[ii]
        out[row['name']] = res['POLY_TYPE']
        
    return out


years = range(1997, 2022)
    
df = pd.DataFrame(
    {'name': ['MarreSalya', 'Amderma'],  # Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Latitude': [69.7142, 69.75], #, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [66.8144, 61.66]}) #, -47.91, -70.66, -74.08, -66.86]})
t = 0
database = pd.DataFrame(np.zeros((1, 4)), 
                        columns=['date', 'value', 'year', 'point'])

base = r"../idata/unzipped"  #path to year

t0 = time.time()
for year in years[10:11]:
    # C:\Users\Professional\Sea_ice\idata\unziped
    
    annual_path_2_unzip = '{}/{}'.format(base, year)
    flist = os.listdir(annual_path_2_unzip)            #(unziped_folder)
    flist = [f for f in flist if '.shp' in f[-4:]]
        
    for f in flist[:]:
            
        date = f.split('_')[2]
        cyear = date[:4]
        f = "aari_kar_{}_pl_a.shp".format(date)  #name of file       
        full_path_to_file = '{}/{}/{}'.format(base, cyear, f)
        
        out = func_open_shp_file(df, full_path_to_file)
        
        for point in out.keys():
            value = out[point]
         
            database.loc[t, :] = date, value, int(year), point 
            t += 1
            
#        database.iloc[t, 0] = date
#        database.iloc[t, 0] = date
#        database.iloc[t, 0] = date
#        database.iloc[t, 0] = date
t1 = time.time()
print('Total time: {:.2f}'.format(t1 - t0))
database.to_csv('final_data.csv', sep=';')    
