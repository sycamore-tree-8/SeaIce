# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:34:16 2021

@author: Professional
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df0 = pd.read_csv(r'C:\Users\Professional\Sea_ice\SeaIce\db_8_places_ifp.csv', 
                       sep = ';', 
                       index_col = 0)



df = df0.query("name == 'МарреСале'")
x = df['year'].values
y = df['dur'].values
ym = np.ma.array(y, mask= y < 1)

plt.figure()
plt.plot(x, ym, 'b--')
plt.grid(ls=':')
plt.show()

