# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:26:29 2025

@author: choi dong yean

Melon_Crawling => Excel 파일로 저장
"""

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'http://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
# ----------------------------------------- #
# 반복문을 이용해 곡과 가수명을 song_data에 저장
song_data = []

'''
    서비스  순위 타이틀          가수
0   Melon   1    Dynamite       BTS
1   Melon   2    Don't Touch me 환불원정대    
'''

rank = 1 # 순위
songs = soup.select('table > tbody > tr')
len(songs) # 100

for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > a')[0].text
    
    song_data.append(['Melon', rank, title, singer])
    
    rank = rank + 1
    
song_data[0]
# => ['Melon', 1, 'REBEL HEART', 'IVE (아이브)']

# song_data 리스트를 이용해 데이터프레임 만들기
import pandas as pd

columns = ['서비스', '순위', '타이틀', '가수']    

pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.head()
pd_data.tail()

# 크롤링 결과를 엑셀파일로 저장
pd_data.to_excel('./files/melon.xlsx', index = False)

