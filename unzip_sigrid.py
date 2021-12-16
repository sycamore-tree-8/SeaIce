# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:37:56 2021

@author: Professional
"""

import os
import zipfile
#import pandas as pd

years = range(1997, 2022)

for cyear in years[:1]:
    
    zip_files = '../idata/zipped_data/{}'.format(cyear)
    
    files_list = os.listdir(zip_files)
    
    to_unzip_path = '../idata/unzipped/{}'.format(cyear)
    if not os.path.exists(to_unzip_path):
        os.makedirs(to_unzip_path)
        
    for f in files_list:
        
        with zipfile.ZipFile("{}/{}".format(zip_files, f), 'r') as zip_ref:
            zip_ref.extractall(to_unzip_path)
        
    