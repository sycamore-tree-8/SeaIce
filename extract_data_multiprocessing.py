# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:03:40 2021

@author: Professional
"""
import os
import time

from itertools import repeat

import numpy as np
import pandas as pd

import geopandas

import multiprocessing as mp


def func_open_shp_file(full_path_to_file, df):


    xp = df.Latitude
    yp = df.Longitude
    
    g = geopandas.GeoDataFrame(df, 
                               geometry=geopandas.points_from_xy(xp, yp),
                               crs=4326)
    g1 = g.to_crs(3576)
    gdf = geopandas.read_file(full_path_to_file)
    
#    out = {}

    fd = pd.DataFrame(np.zeros((len(df), 4)), 
                      columns=['date', 'value', 'year', 'point'])

    idate = (full_path_to_file.split('/')[-1]).split('_')[2]
    iyear = full_path_to_file.split('/')[3]

    for i, row in df.iterrows():
        p1 = g1.iloc[i, -1]
        dists = gdf.distance(p1).sort_values()
        ii = dists.index[0]
#        print(i, ii)
        
        res = gdf.loc[ii]
#        out[row['name']] = res['POLY_TYPE']
        
        output = [idate, res['POLY_TYPE'], iyear, row['name']]
        
        fd.iloc[i, :] = output
  
    return fd


if __name__ == '__main__':
    

    years = range(1997, 2022)
    
    df = pd.read_excel(r"C:\Users\Professional\Sea_ice\idata\db_ice_stations.xlsx")
 #   print(df)
    df = df[['cname', 'lon360', 'lat']]
    df.columns = ['name', 'Longitude', 'Latitude']
#    print(df)
#    assert 1==0
    
    # df = pd.DataFrame(
    #     {'name': ['MarreSalya', 'Amderma'],  # Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
    #      'Latitude': [69.7142, 69.75], #, -15.78, -33.45, 4.60, 10.48],
    #      'Longitude': [66.8144, 61.66]}) #, -47.91, -70.66, -74.08, -66.86]})
    t = 0
#    database = pd.DataFrame(np.zeros((1, 4)), 
#                            columns=['date', 'value', 'year', 'point'])
    
    base = r"../idata/unzipped"  #path to year
    
    t0 = time.time()
    new = []
    for year in years[:]:
        # C:\Users\Professional\Sea_ice\idata\unziped
        
        annual_path_2_unzip = '{}/{}'.format(base, year)
        flist = os.listdir(annual_path_2_unzip)            #(unziped_folder)
        flist = [f for f in flist if '.shp' in f[-4:]]
            
        for f in flist[:]:
                
            date = f.split('_')[2]
            cyear = date[:4]
            f = "aari_kar_{}_pl_a.shp".format(date)  #name of file       
            full_path_to_file = '{}/{}/{}'.format(base, cyear, f)
            
            new.append(full_path_to_file)

#    assert 1==2
    mp.freeze_support()
    pool = mp.Pool(processes = (mp.cpu_count()) - 1)
    outputs = pool.starmap(func_open_shp_file, zip(new, repeat(df)))
    pool.close()

    database = pd.DataFrame()
    for out in outputs:
        database = pd.concat((database, out), axis=0, ignore_index=True)
    database.to_csv('final_data.csv', sep=';')    
                       
    # for point in out.keys():
    #     value = out[point]
     
    #     database.loc[t, :] = date, value, int(year), point 
    #     t += 1

    t1 = time.time()
    print('Total time: {:.2f}'.format(t1 - t0))
#
