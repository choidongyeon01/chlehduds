# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:22:02 2025

@author: tuesv

2_1 address.py
    seoul_starbucks_list.xlsx
    sgg_pop.xlsx
    sgg_biz.xlsx
"""
import pandas as pd
seoul_starbucks = pd.read_excel('data_files/starbucks_location/files/seoul_starbucks_list.xlsx', header = 0)

# 스타벅스 주소 정보에서 시군구명 추출
sgg_names = []

# 서울특별시 강남구 연주로 425(역삼동)
for address in seoul_starbucks['주소']:
    sgg = address.split()[1]
    sgg_names.append(sgg)
    
seoul_starbucks['시군구명'] = sgg_names

# 엑셀로 저장
seoul_starbucks.to_excel('data_files/starbucks_location/files/seoul_starbucks_list.xlsx', index = False)





























