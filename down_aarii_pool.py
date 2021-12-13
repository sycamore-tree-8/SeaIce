# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:45:02 2021

@author: Professional
"""

import os
import time
import urllib

import pandas as pd

import requests # get the requsts library from https://github.com/requests/requests

import multiprocessing as mp
from multiprocessing import freeze_support

# Example
#http://wdc.aari.ru/datasets/d0015/arcice/2021/aari_arc_20210105_pl_b.zip

#http://wdc.aari.ru/datasets/d0004/kar/sigrid/1997/aari_kar_19970611_pl_a.zip


def foo(url):
    '''
    '''
    
    cyear = url.split('/')[-2] #kw.get('cyear', 1997)
    
    ff = url.split('/')[-1]
    fpath = './{}'.format(cyear)
    try:            
        urllib.request.urlretrieve(url, '{}/{}'.format(fpath, ff))
        print('Downloaded {} file'.format(ff))
    except:
        pass


if __name__ == '__main__':
    
    base_url = r'http://wdc.aari.ru/datasets/d0004/kar/sigrid'
    years = range(1997, 2022)
    
    t0 = time.time()
    
    flist = []
    for cyear in years[:1]:
        if not os.path.exists(str(cyear)):
            os.makedirs(str(cyear))
    
        dd = pd.date_range('{}0101'.format(cyear), '{}1231'.format(cyear),
                           freq='1d')
        dates = dd.strftime('%Y%m%d')
        for date in dates[:]:
        
            ff = 'aari_kar_{}_pl_a.zip'.format(date)
            url = '{}/{}/{}'.format(base_url, cyear, ff)
            flist.append(url)
    
    t1 = time.time()
    print('{:.2f}'.format(t1 - t0))
    

    

