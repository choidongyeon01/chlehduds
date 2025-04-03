# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:22:46 2025

@author: choi dong yean
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json
import folium

driver = webdriver.Chrome()
url = 'https://www.mega-mgccoffee.com/store/find/'
driver.get(url)

# 지역찾기
local_btn = 'body > div.wrap > div.cont_wrap.find_wrap > div > div.cont_box.find01 > div.map_search_wrap > div > div.cont_text_wrap.map_search_tab_wrap > div > ul > li.check'
driver.find_element('css selector', local_btn).click()


# 서울 버튼 요소 찾기 (2 ~ 26번까지 서울에 있는 구) -> range(2, 27)
seoul_btn = '#store_area_search_list > li:nth-child(1)'
driver.find_element('css selector', seoul_btn).click()

# BeautifulSoup으로 HTML 파서 만들기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

'''
강남구
#store_area_search_list_result > li:nth-child(2)
'''

mega_soup_list = soup.select('li.store_area_search_list')
print(len(mega_soup_list)) #25

mega_soup_list[0]
# 메가커피 매장 정보 샘플 확인
mega_store = mega_soup_list[0]
name = mega_store.select('#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(23) > div:nth-child(2) > div > div > div.cont_text.map_point_info_title_wrap > div.cont_text_title.cont_text_inner > b')[0].text.strip()
lat = mega_store[''].strip()
lng = mega_store[''].strip()



















