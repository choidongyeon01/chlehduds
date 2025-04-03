# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:07:05 2025

@author: choi dong yean
"""

from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd

# genie.xlsx
## 1~50위까지
driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('tbody > tr')
songs[10]
len(songs)
song_data = []
rank = 1 # 순위
for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text.strip()
    
    song_data.append(['Genie', rank, title, singer])
    
    rank = rank + 1


## 50~100위까지
driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20250218&hh=12&rtm=Y&pg=2'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('table > tbody > tr')

for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text.strip()
    
    song_data.append(['Genie', rank, title, singer])
    
    rank = rank + 1

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.to_excel('./files/genie.xlsx', index = False)