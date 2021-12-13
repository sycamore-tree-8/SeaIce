# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:55:03 2021

@author: Professional
"""

import os
import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

# def get_html(url):
#     response = urllib.request.urlopen(url)
#     return response.read()
# def parse(html):
#     soup = BeautifulSoup(html)
#     table = soup.find("table", clazz="items_list")
#     print(table)
# # def main():
#       parse(get_html(fpath))
    
# fpath = r"http://www.aari.ru/projects/ECIMO/index.php"
# fpath2 = r"http:/www.aari.ru/odata"
# fpath3 = r"http://www.aari.ru/odata/_d0009.php?mod=1"
# fpath4 = r"http://www.aari.ru/resources/d0009/2019/kara_NE_2019.html"
# response = urllib.request.urlopen(fpath4)
# html = response.read()
# soup = BeautifulSoup(html, features="lxml")
# tab = soup.find_all("table")
# print(tab)
# ===========================================================================

base_url = r"http://www.aari.ru/resources/d0009"
tmp_path = r"./tmp_files"
if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)
regions = {'kara_SW' : 1, 
           'kara_NE' : 1,
           'chukcha' : 1,
           'eastsib' : 1,
           'laptevs' : 1
           }
years = range(1996, 2022)
for region in list(regions.keys())[:]:
    
    rdf = pd.DataFrame()
    
    for k, cyear in enumerate(years[:]):
        
        if cyear < 2010:
            header = 1
        else:
            header = 2
        
        if region == 'chukcha' and cyear == 2007:
            continue
        
        fpath5 = r"{0:}/{1:}/{2:}_{1:}.html".format(base_url, cyear, region)
        r = requests.get(fpath5)
        if r:
            print('OK! Year: {} - REGION: {}'.format(cyear, region))
            df = pd.read_html(r.text, header=header,
                              index_col=[0])[0]
            
    #        print(df)
    #        df.to_csv('test_{}_{}.txt'.format(region, cyear), sep=';')  
            tmp_reg_folders = '{}/{}'.format(tmp_path, region)
            if not os.path.exists(tmp_reg_folders):
                os.makedirs(tmp_reg_folders)   
            df.to_excel('{}/test_{}_{}.xlsx'.format(tmp_reg_folders, 
                                                    region, cyear))
        else:
            print('ERROR! Year: {} - REGION: {}'.format(cyear, region))
    
        
            
#         try:
#             ts = df.loc["Очищение акватории", :]
# #            ts = df.loc["Устойчивое становление припая", :]
#         except KeyError:
# #            ts = df.loc["Устойчивое  становление припая", :]
#             ts = df.loc["Очищение  акватории", :]
            
#         ts.name = cyear
            
#         if k == 0:
#             rdf = ts[:]
#         else:
#             rdf = pd.concat((rdf, ts), axis=1)
            
#     rdf = rdf.T