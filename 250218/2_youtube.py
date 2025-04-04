# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:02:00 2025

@author: choi dong yean

youtube 데이터(10개 페이지) 및 시각화
유튜브 랭킹 데이터 수집
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# webdriver로 크롬 브라우저 실행
browser = webdriver.Chrome()
url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
browser.get(url)

# 페이지 정보 가져오기
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

# BeautifulSoup으로 tr 태그 추출
channel_list = soup.select('tr')
len(channel_list) # 102
channel_list[0]

channel_list = soup.select('form > table > tbody > tr')
len(channel_list)

# 카테고리 정보 추출 : <p class = category>
channel = channel_list[0]
category = channel.select('p.category')[0].text.strip()
# => '[음악/댄스/가수]'

# 채널명 : <h1><a ~~>채널명</a></h1>
title = channel.select('h1 > a')[0].text.strip()
# => 'BLACKPINK'

# 구독자 수(subscriber_cnt)
# view 수(view_cnt)
# 동영상 수 추출(video_cnt)
subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text
# ---------------------------------------------- #

## 페이지별 URL : 10개
page = 1
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={}'.format(page)
# => 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1'
# ---------------------------------------------- #

results = [] # <= [title, category, subscriber, view, video]

for page in range(1, 11):
    url = f'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}'
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    channel_list = soup.select('form > table > tbody > tr')
    
    for channel in channel_list:
        title = channel.select('h1 > a')[0].text.strip()
        category = channel.select('p.category')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text
        view = channel.select('.view_cnt')[0].text
        video = channel.select('.video_cnt')[0].text
        
        data = [title, category, subscriber, view, video]
        results.append(data)

# 데이터 칼럼명을 설정하고 엑셀 파일로 저장
df = pd.DataFrame(results)
df.columns = ['title', 'category', 'subscriber', 'view', 'video']
df.info()
df.replace('고기남자', '고기남자')
# => 해도 안 바뀜 / 정규표현식을 알아야함
df.to_excel('./files/youtube_rank.xlsx', index = False)











