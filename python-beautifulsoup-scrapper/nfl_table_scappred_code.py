#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:18:42 2022

@author: longnguyen
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'
page = requests.get(url);
soup = BeautifulSoup(page.text, 'lxml');
table = soup.find('table')

ths = table.find_all('th')
headers = []
for i in ths:
    headers.append(i.text);
df = pd.DataFrame(columns = headers)
trs = table.find_all('tr')[1:]

for j in trs:
    row_data = j.find_all('td')
    print(row_data);
    row = [];
    for data in row_data:
        row.append(data.text)
    length = len(df)
    df.loc[length] = row
df.to_csv('/Users/longnguyen/scrapping python/python-beautifulsoup-scrapper/nfl_table_scrapped.csv')


