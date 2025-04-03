# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:22:02 2025

@author: tuesv

스타벅스 매장 리스트에 시군구명을 추가
시군구목록 데이터 => 시군구별 매장 수, 인구 수, 사업체 수
통계 데이터 병합
"""

import pandas as pd

# 시군구 목록 데이터 불러오기
seoul_sgg = pd.read_excel('data_files/starbucks_location/files/seoul_sgg_list.xlsx')

# 서울시 스타벅스 매장 목록 데이터 불러오기
seoul_starbucks = pd.read_excel('data_files/starbucks_location/files/seoul_starbucks_list.xlsx')

# 시군구별 스타벅스 매장 수 세기 : '시군구명', '매장명' => count()
# pivot_table()
starbucks_sgg_count = seoul_starbucks.pivot_table(index = '시군구명',
                                                  values = '매장명',
                                                  aggfunc = 'count')\
                      .rename(columns = {'매장명' : '스타벅스_매장수'})
                                                  
# 서울시 시군구 목록 데이터에 스타벅스 매장 수 데이터를 병합
seoul_sgg = pd.merge(seoul_sgg, starbucks_sgg_count, how = 'left', on = '시군구명')



### 서울시 시군구 목록 데이터에 서울시 시군구별 인구 통계 데이터를 병합
sgg_pop = pd.read_excel('data_files/starbucks_location/files/sgg_pop.xlsx')
seoul_sgg = pd.merge(seoul_sgg, sgg_pop, how = 'left', on = '시군구명')

### 서울시 시군구 목록 데이터에 서울시 시군구별 사업체 수 통계 데이터를 병합
sgg_biz = pd.read_excel('data_files/starbucks_location/files/sgg_biz.xlsx')
sgg_biz = sgg_biz.rename(columns = {'자치구' : '시군구명', '계' : '종사자수'})
seoul_sgg = pd.merge(seoul_sgg, sgg_biz, how = 'left', on = '시군구명')


### 병합 결과를 엑셀 파일로 저장
seoul_sgg.to_excel('data_files/starbucks_location/files/seoul_sgg_stat.xlsx', index = False)























