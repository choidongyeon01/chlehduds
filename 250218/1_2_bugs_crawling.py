# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:06:19 2025

@author: choi dong yean
"""

from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd

# bugs.xlsx
driver = webdriver.Chrome()
url = 'https://music.bugs.co.kr/chart'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('table.byChart > tbody > tr')
len(songs)
songs[0]

song_data = []
rank = 1 # 순위
for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    
    song_data.append(['Bugs', rank, title, singer])
    
    rank = rank + 1

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.to_excel('./files/bugs.xlsx', index = False)























