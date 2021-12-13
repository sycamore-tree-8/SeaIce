# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:37:56 2021

@author: Professional
"""

import os
import zipfile
import pandas as pd

years = range(1997, 2022)

for cyear in years[:1]:
    
    files_list = os.listdir('./{}'.format(cyear))
    
    if not os.path.exists(str(cyear)):
        os.makedirs('./unziped/{}'.format(cyear))
        
    for f in files_list:
        
        with zipfile.ZipFile("./{}/{}".format(cyear, f), 'r') as zip_ref:
            zip_ref.extractall('./unziped/{}'.format(cyear))
        
    