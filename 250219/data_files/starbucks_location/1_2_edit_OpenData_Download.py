# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:22:02 2025

@author: tuesv
"""

import pandas as pd
sgg_pop_df = pd.read_csv('data_files/starbucks_location/files/report.txt', sep = '\t', header = 2)
columns = {
    '기간': 'GIGAN',
    '자치구': 'JACHIGU',
    '계': 'GYE_1',
    '계.1': 'GYE_2',
    '계.2': 'GYE_3',
    '남자': 'NAMJA_1',
    '남자.1': 'NAMJA_2',
    '남자.2': 'NAMJA_3',
    '여자': 'YEOJA_1',
    '여자.1': 'YEOJA_2',
    '여자.2': 'YEOJA_3',
    '세대': 'SEDAE',
    '세대당인구': 'SEDAEDANGINGU',
    '65세이상고령자': 'N_65SEISANGGORYEONGJA'
}
sgg_pop_df.rename(columns = columns, inplace = True)

# 서울시 구별 주민등록인구 데이터프레임의 요약 정보 확인
sgg_pop_df.info()

# 필요없는 데이터 제거 : 첫 번째 데이터 합계
condition = sgg_pop_df['JACHIGU'] != '합계'
sgg_pop_df_selected = sgg_pop_df[condition]

# 분석에 필요한 칼럼 선택
columns = ['JACHIGU', "GYE_1"]
sgg_pop_df_final = sgg_pop_df_selected[columns]

# 데이터프레임의 칼럼명 변경
sgg_pop_df_final.columns = ['시군구명', '주민등록인구']
sgg_pop_df_final.info()

# 엑셀로 저장
sgg_pop_df_final.to_excel('data_files/starbucks_location/files/sgg_pop.xlsx', index = True)


# ---------------- 여기까지 인구 데이터 정리 ----------------- #

### 서울시 동별 사업체현황 통계 데이터 : report.txt
sgg_biz_df = pd.read_csv('data_files/starbucks_location/files/report2.txt', sep = '\t', header = 2)

# 시군구동별 사업체 현황 데이터 추출
condition = sgg_biz_df['동'] == '소계'
sgg_biz_df_selected = sgg_biz_df[condition]

# 필요없는 칼럼 제거 : '자치구', '계', '사업체수'
columns = ['자치구', '계', '사업체수']
sgg_biz_df_final = sgg_biz_df_selected[columns]
sgg_biz_df_final.columns = ['시군구명', '종사자수', '사업체수']

# 데이터프레임의 인덱스 초기화
sgg_biz_df_final = sgg_biz_df_final.reset_index(drop = True)

# 엑셀로 저장
sgg_biz_df_final.to_excel('data_files/starbucks_location/files/sgg_biz.xlsx', index = False)

















