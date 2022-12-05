#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:26:02 2022

@author: longnguyen
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url);
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
ths = table.find_all('th')
headers = []
for i in table.find_all('th'):
    headers.append(i.text);

df = pd.DataFrame(columns = headers)    

trs = table.find_all('tr')[1:]


for j in trs :
    row_data = j.find_all('td')
    row = []
    for data in row_data:
        row.append(data.text)
    length = len(df)
    df.loc[length] = row

df.to_csv('/Users/longnguyen/table_scappred.csv')