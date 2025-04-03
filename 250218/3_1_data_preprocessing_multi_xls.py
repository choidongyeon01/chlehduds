# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:51:01 2025

@author: choi dong yean

여러 개의 엑셀 파일을 전처리하여 통합!!!
kto_201001.xlsx ~ kto_202005.xlsx : 125개 파일
"""

import pandas as pd

kto_201901 = pd.read_excel('./data/kto_201901.xlsx',
                           header = 1,
                           usecols = 'A:G',
                           skipfooter = 4)

kto_201901.head()
kto_201901.tail()

## 데이터 전처리 ##
kto_201901.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 67 entries, 0 to 66
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   국적      67 non-null     object
 1   관광      67 non-null     int64 
 2   상용      67 non-null     int64 
 3   공용      67 non-null     int64 
 4   유학/연수   67 non-null     int64 
 5   기타      67 non-null     int64 
 6   계       67 non-null     int64 
dtypes: int64(6), object(1)
memory usage: 3.8+ KB
'''

kto_201901.describe()
'''
                 관광            상용  ...             기타              계
count      67.00000     67.000000  ...      67.000000      67.000000
mean    26396.80597    408.208955  ...    5564.208955   32979.194030
std    102954.04969   1416.040302  ...   17209.438418  122821.369969
min         0.00000      0.000000  ...      16.000000      54.000000
25%       505.00000     14.500000  ...     260.000000     927.000000
50%      1304.00000     45.000000  ...     912.000000    2695.000000
75%      8365.00000    176.500000  ...    2824.500000   14905.500000
max    765082.00000  10837.000000  ...  125521.000000  916950.000000
'''

# 각 컬럼에서 0인 부분을 필터링 : 4개 컬럼 중 1개라도 0이 있으면 
condition = (kto_201901['관광'] == 0) | (kto_201901['상용'] == 0) | \
            (kto_201901['공용'] == 0) | (kto_201901['유학/연수'] == 0)
'''
0     False
1     False
2     False
3     False
4      True
 
62    False
63     True
64     True
65     True
66     True
Length: 67, dtype: bool
'''

kto_201901[condition]
'''
65    교포소계     0    0   0      0  15526  15526
66      교포     0    0   0      0  15526  15526
'''
kto_201901['기준년월'] = '2019-01'
kto_201901.head()

kto_201901['국적'].unique()

continents_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙',
                   '교포소계']

# 대륙 목록에 해당하는 값 제외
# .isin()
# 국적.isin(continents_list) == False
condition = (kto_201901.국적.isin(continents_list) == False)

kto_201901_country = kto_201901[condition]
kto_201901_country['국적'].unique()

kto_201901_country.head()

kto_201901_country_newindex = kto_201901_country.reset_index(drop = True)

continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 \
             + ['아프리카']*2 + ['기타대륙'] + ['교포']

kto_201901_country_newindex['대륙'] = continents

# 관광객비율(%) 컬럼 생성 : .1
# 관광객비율(%) = 관광 / 계 * 100
# round(관광객비율(%) = 관광 / 계 * 100, 1)
kto_201901_country_newindex['관광객비율(%)'] = \
    round(kto_201901_country_newindex['관광']/  \
          kto_201901_country_newindex['계']*100, 1)
# ---------------------------------------------------- #
# 함수로 선언
def create_kto_data(yy, mm): # 2018, 12
    # 1. 불러올 Excdl 파일 경로를 지정
    file_path = './data/kto_{}{}.xlsx'.format(yy, mm)
    
    # 2. Excel 파일 불러오기
    df = pd.read_excel(file_path, header = 1, skipfooter=4, usecols = 'A:G')
    
    # 3. '기준년월' 컬럼 추가
    df['기준년월'] = '{}-{}'.format(yy, mm)
    
    # 4. '국적' 컬럼에서 대륙 제거하고 국가만 남기기
    # 대륙 컬럼 생성을 위한 목록
    ignore_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙',
                       '교포소계']
    # 대륙 미포함 조건
    condition = (kto_201901.국적.isin(continents_list) == False)
    df_country = df[condition].reset_index(drop = True)
    
    # 5. '대륙' 컬럼 추가
    continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 \
                 + ['아프리카']*2 + ['기타대륙'] + ['교포']
    df_country['대륙'] = continents
    
    # 6. 국가별 '관광객비율(%)' 컬럼 추가
    df_country['관광객비율(%)'] = \
        round(df_country.관광/  \
              df_country.계 *100, 1)
    
    # 7. '전체비율(%)' 컬럼 추가
    tourist_sum = sum(df_country['관광'])
    df_country['전체비율(%)'] = \
        round(df_country['관광']/  \
              tourist_sum *100, 1)
            
    # 8. 결과
    return(df_country)

kto_test = create_kto_data(2018, 12)
kto_test.head()

'''
for yy in range(2010, 2021): # 2010 ~  2020
    for mm in range(1, 13):  # 1 ~ 12
        temp = create_kto_data(str(yy), str(mm).zfill(2))
'''
df = pd.DataFrame()

for yy in range(2010, 2021):
    for mm in range(1, 13):
        try:
            temp = create_kto_data(str(yy), str(mm).zfill(2))
            df = pd.concat([df, temp], ignore_index = True)
            
        except:
            pass
        
df.info()

df.to_excel('./files/kto_total.xlsx', index = False)

# -------------------------------------------------- #
## 문제 겸 과제 ## -> 3_2_visualizaion 으로 이어짐

# 국적별 관광객 데이터를 개별 엑셀 파일로 저장하기
# [국적별 관광객 데이터] 나라이름.xlsx

cntry_list = []
# 국가 리스트 : cntry_list
for cntry in cntry_list:
    # 국적으로 필터링
    # 국적이름을 반영한 파일명
    # 정해 놓은 파일명으로 저장
















