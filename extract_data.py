# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:03:40 2021

@author: Professional
"""

years = []
points = []
full_path_to_file = (base, cyear, f)

for year in years:
    flist = os.listdir(unziped_folder)
    flist = [f for f in flist if '.shp' in f[-4:]]

    for f in flist:
        date = f.split('_')[2]
        #base = path to c year
        #cyear = year
        #f = name of file
        full_path_to_file = (base, cyear, f)
        func_open_shp_file(xp, yp, full_path_to_file) #=value
        
        
        