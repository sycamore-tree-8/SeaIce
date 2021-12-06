# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:00:32 2021

@author: Professional
"""
import geopandas
import pandas as pd
from shapely.geometry import Point
#from shapely.geometry.polygon import Polygon

df = pd.DataFrame(
    {'name': ['MarreSalya'],  # Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Latitude': [75], #, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [60.144]}) #, -47.91, -70.66, -74.08, -66.86]})

g = geopandas.GeoDataFrame(df, 
                           geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
g = g.set_crs(4326)
g1 = g.to_crs(3576)
gdf = geopandas.read_file(r"C:\Users\Professional\Sea_ice\SeaIce")
#print(gdf0.crs)
#gdf = gdf0.to_crs(4326)
#print(gdf.crs)
#print(gdf.columns)
#print(gdf['POLY_TYPE'])
#print(gdf['geometry'])

p1 = Point(66.8144, 69.7142) #МарреСале
#p1 = Point(62, 72) #МарреСале
p1 = g1.iloc[0, -1]

for i, row in gdf.iterrows():
    geom = row['geometry']
    try:
        if geom.contains(p1):
           print(i, row['POLY_TYPE'])
           break
#        else:
#            print(i)
    except:
        print('ER', i)
   



        