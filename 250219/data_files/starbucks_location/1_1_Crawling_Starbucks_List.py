# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:38:33 2025

@author: choi dong yean
"""

'''
    1.1 크롤링을 이용한 서울시 스타벅스 매장 목록 데이터 생성
        (1_1_Crawling_Starbucks_list.py)
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url = 'https://www.istarbucks.co.kr/store/store_map.do?disp=locale'
driver.get(url)

### webdriver로 '서울' 버튼 요소를 찾아 클릭 ###
# 1. '서울' 버튼 요소를 찾아
seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'

# 2. driver.find_element()
#    'css selector'
#     seoul_btn
# 3. click()
driver.find_element('css selector', seoul_btn).click()

### webdriver로 ‘전체’ 버튼 요소를 찾아 클릭
all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'
driver.find_element('css selector', all_btn).click()

# BeautifulSoup으로 HTML 파서 만들기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# select()를 이용해 원하는 HTML 태그를 모두 찾아오기
starbucks_soup_list = soup.select('li.quickResultLstCon')
print(len(starbucks_soup_list)) # 632

starbucks_soup_list[0]
# 스타벅스 매장 정보 샘플 확인
starbucks_store = starbucks_soup_list[0]
name = starbucks_store.select('strong')[0].text.strip()
lat = starbucks_store['data-lat'].strip()
lng = starbucks_store['data-long'].strip()
store_type = starbucks_store.select('i')[0]['class'][0][4:]
address = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
tel = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]

'''
store_type = starbucks_store.select('i')[0]['class'][0][4:]

store_type = starbucks_store.select('i')
=> [<i class="pin_general">리저브 매장 2번</i>]

store_type = starbucks_store.select('i')[0]['class']
=> ['pin_general']

store_type = starbucks_store.select('i')[0]['class'][0][4:]
=> 'general'
'''

'''
address = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]

starbucks_store.select('p.result_details')[0]
=> <p class="result_details">서울특별시 강남구 언주로 425 (역삼동)<br/>1522-3232</p>

str(starbucks_store.select('p.result_details')[0])
=> '<p class="result_details">서울특별시 강남구 언주로 425 (역삼동)<br/>1522-3232</p>'

str(starbucks_store.select('p.result_details')[0]).split('<br/>')
=> ['<p class="result_details">서울특별시 강남구 언주로 425 (역삼동)', '1522-3232</p>']

str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0]
=> '<p class="result_details">서울특별시 강남구 언주로 425 (역삼동)'

str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')
=> ['<p class="result_details"', '서울특별시 강남구 언주로 425 (역삼동)']

str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
=> '서울특별시 강남구 언주로 425 (역삼동)'
'''

### 서울시 스타벅스 매장 목록 데이터 ###
# 매장명, 위도, 경도, 주소, 전화번호
starbucks_list = []

for item in starbucks_soup_list:
    name = item.select('strong')[0].text.strip()
    lat = item['data-lat'].strip()
    lng = item['data-long'].strip()
    store_type = item.select('i')[0]['class'][0][4:]
    address = str(item.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
    tel = str(item.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
    
    starbucks_list.append([name, lat, lng, store_type, address, tel])
    
# starbucks_list => Dataframe
columns = ['매장명', '위도', '경도', '매장타입', '주소', '전화번호']
seoul_starbucks_df = pd.DataFrame(starbucks_list, columns = columns)

# 데이터프레임의 요약 정보 확인
seoul_starbucks_df.info()

# 엑셀로 저장
seoul_starbucks_df.to_excel('data_files/starbucks_location/files/seoul_starbucks_list.xlsx', index = True)
    














