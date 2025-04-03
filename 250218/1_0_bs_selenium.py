# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:07:55 2025

@author: choi dong yean
"""

from selenium import webdriver

# 크롬부라우저 실행
driver = webdriver.Chrome()

# URL 접속
url = 'https://www.naver.com'
driver.get(url)

# 웹페이지 html 다운로드
html = driver.page_source

# 웹페이지 html 다운로드
html = driver.page_source
# ---------------------------------- #
#### BeautifulSoup.select() ####
html = '''
<html>
    <head>
    </head>
    <body>
        <h1> 우리동네시장</h1>
            <div class = 'sale'>
                <p id='fruits1' class='fruits'>
                    <span class = 'name'> 바나나 </span>
                    <span class = 'price'> 3000원 </span>
                    <span class = 'inventory'> 500개 </span>
                    <span class = 'store'> 가나다상회 </span>
                    <a href = 'http://bit.ly/forPlaywithData' > 홈페이지 </a>
                </p>
            </div>
            <div class = 'prepare'>
                <p id='fruits2' class='fruits'>
                    <span class ='name'> 파인애플 </span>
                </p>
            </div>
    </body>
</html>
'''
# 클래스 값을 찾고 싶다 : 태그.~~~
# id 값을 찾고 싶다 : 태그#id -> 태그 생략 가능

# HTML 문자열 BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 태그명으로 태그 찾기
tags_open = soup.select('span')
'''
[<span class="name"> 바나나 </span>,
 <span class="price"> 3000원 </span>,
 <span class="inventory"> 500개 </span>,
 <span class="store"> 가나다상회 </span>,
 <span class="name"> 파인애플 </span>]
'''

tags_p = soup.select('p')
'''
[<p class="fruits" id="fruits1">
 <span class="name"> 바나나 </span>
 <span class="price"> 3000원 </span>
 <span class="inventory"> 500개 </span>
 <span class="store"> 가나다상회 </span>
 <a href="http://bit.ly/forPlaywithData"> 홈페이지 </a>
 </p>,
 <p class="fruits" id="fruits2">
 <span class="name"> 파인애플 </span>
 </p>]
'''

# 태그 구조로 위치 찾기
tags_name = soup.select('span.name')
'''
[<span class="name"> 바나나 </span>, <span class="name"> 파인애플 </span>]
'''

# 상위 구조 활용
tags_banana1 = soup.select('#fruits1 > span.name') # > : 누구의 직계라는 뜻
# [<span class="name"> 바나나 </span>]

tags_banana2 = soup.select('div.sale > #fruits1 > span.name')
'''
[<span class="name"> 바나나 </span>]
'''

tags_banana3 = soup.select('div.sale span.name')
'''
[<span class="name"> 바나나 </span>]
'''

# 태그 그룹에서 하나의 태그만 선택
tags = soup.select('span.name')
'''
[<span class="name"> 바나나 </span>, <span class="name"> 파인애플 </span>]
'''
tag_1 = tags[0]
# => <span class="name"> 바나나 </span>

# 태그에서 정보 가져오기
content = tag_1.text
# => ' 바나나 '

# 선택한 태그에서 텍스트, 속성 값 가져오기
tags = soup.select('a')
'''
[<a href="http://bit.ly/forPlaywithData"> 홈페이지 </a>]
'''
tag = tags[0]
# => <a href="http://bit.ly/forPlaywithData"> 홈페이지 </a>

content = tag.text
# => ' 홈페이지 '

link = tag['href']
# => 'http://bit.ly/forPlaywithData'


'''
메론 노래 순위 정보 크롤링
'''
driver = webdriver.Chrome()

url = 'http://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('tr')
len(songs) # 101

songs[0]
'''
<tr>
<th scope="col">
<div class="wrap t_right"><input class="input_check d_checkall" title="곡 목록 전체 선택" type="checkbox"/></div>
</th>
<th scope="col">
<div class="wrap t_center"><span class="rank">순위</span></div>
</th>
<th scope="col">
<div class="wrap none">순위등락</div>
</th>
<th scope="col">
<div class="wrap none">앨범이미지</div>
</th>
<th scope="col">
<div class="wrap none">곡 상세가기</div>
</th>
<th scope="col">
<div class="wrap pd_l_12">곡정보</div>
</th>
<th scope="col">
<div class="wrap pd_l_12">앨범</div>
</th>
<th scope="col">
<div class="wrap pd_l_30">좋아요</div>
</th>
<th scope="col">
<div class="wrap t_center">듣기</div>
</th>
<th scope="col">
<div class="wrap t_center">담기</div>
</th>
<th scope="col">
<div class="wrap t_center">다운</div>
</th>
<th scope="col">
<div class="wrap t_center">뮤비</div>
</th>
</tr>
'''

# 첫 번째는 제외하고, 두 번째(인덱스번호 1)부터 끝까지만 선택
songs = soup.select('tr')[1:]
len(songs) #100

# 한 개의 곡 정보 지정
song = songs[0]

# 곡 제목 찾기 : <a -> </a>
title = song.select('a')
len(title) # 6

title = song.select('span > a')
len(title) # 2

title = song.select('div.ellipsis.rank01 > span > a')
len(title) # 1
'''
[<a href="javascript:melon.play.playSong('1000002721',38444825);" title="REBEL HEART 재생">REBEL HEART</a>]
'''

title = song.select('div.ellipsis.rank01 > span > a')[0]
'''
<a href="javascript:melon.play.playSong('1000002721',38444825);" title="REBEL HEART 재생">REBEL HEART</a>
'''
title = song.select('div.ellipsis.rank01 > span > a')[0].text
# => 'REBEL HEART'

# 가수 찾기
singer = song.select('div.ellipsis.rank02 > a')[0].text
# => 'IVE (아이브)'

## 멜론 50위 노래순위 정보 (제목 | 가수)




















