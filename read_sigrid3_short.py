# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:00:32 2021
@author: Professional
"""
import geopandas
import pandas as pd


df = pd.DataFrame(
    {'name': ['MarreSalya', 'Amderma'],  # Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Latitude': [69.7142, 69.75], #, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [66.8144, 61.66]}) #, -47.91, -70.66, -74.08, -66.86]})


g = geopandas.GeoDataFrame(df, 
                           geometry=geopandas.points_from_xy(df.Longitude, df.Latitude),
                           crs=4326)
g1 = g.to_crs(3576)
#gdf = geopandas.read_file(r"D:/SCIENCE/2021/polina/aari/aari_arc_20210921_pl_a.shp")
gdf = geopandas.read_file(r"C:\Users\Professional\Sea_ice\SeaIce\aari_arc_20211130_pl_a.shp")

for i in range(2):
    p1 = g1.iloc[i, -1]
    dists = gdf.distance(p1).sort_values()
    ii = dists.index[0]
    print(i, ii)
    
    res = gdf.loc[ii]
    df.loc[i, 'poly_type'] = res['POLY_TYPE']

print(df) 



