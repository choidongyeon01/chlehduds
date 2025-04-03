# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:28:36 2025

@author: choi dong yean
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 삶의 만족도
lifegood = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_삶의만족도.xlsx')
lifegood.info() # 결측치 한개 - 경상북도 근위군
lifegood.drop('No', axis = 1, inplace = True)
lifegood = lifegood[['시도', '삶의 만족도']]
lifegood['삶의 만족도'].mean()
lifegood['삶의 만족도'].median()
lifegood.fillna(0.4839, inplace = True)

# 건강
health = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_건강.xlsx')
health.info() # 결측치 한개 - 경상북도 고령군
health.drop('No', axis = 1, inplace = True)
health = health[['시도', '평균']]
health.columns = ['시도', '건강평균']
health['건강평균'].mean()
health['건강평균'].median()
health.fillna(0.3895, inplace = True)

# 경제
economy = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_경제.xlsx')
economy.info() # 결측치 한개 - 경상북도 영양군
economy.drop('No', axis = 1, inplace = True)
economy = economy[['시도', '평균']]
economy.columns = ['시도', '경제평균']
economy['경제평균'].mean()
economy['경제평균'].median()
economy.fillna(0.3774, inplace = True)

# 관계
relation = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_관계및사회참여.xlsx')
relation.info() # 결측치 한개 - 대구광역시 서구
relation.drop('No', axis = 1, inplace = True)
relation = relation[['시도', '평균']]
relation.columns = ['시도', '관계평균']
relation['관계평균'].mean()
relation['관계평균'].median()
relation.fillna(0.4652, inplace = True)

# 교육
education = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_교육.xlsx')
education.info() # 결측치 한개
education.drop('No', axis = 1, inplace = True)
education = education[['시도', '평균']]
education.columns = ['시도', '교육평균']
education['교육평균'].mean()
education['교육평균'].median()
education.fillna(0.5397, inplace = True)

# 안전
safe = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_안전.xlsx')
safe.info() # 결측치 한개 - 대구광역시 동구
safe.drop('No', axis = 1, inplace = True)
safe = safe[['시도', '평균']]
safe.columns = ['시도', '안전평균']
safe['안전평균'].mean()
safe['안전평균'].median()
safe.fillna(0.4461, inplace = True)

# 여가
hobby = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_여가.xlsx')
hobby.info() # 결측치 한개 - 부산광역시 북구
hobby.drop('No', axis = 1, inplace = True)
hobby = hobby[['시도', '평균']]
hobby.columns = ['시도', '여가평균']
hobby['여가평균'].mean()
hobby['여가평균'].median()
hobby.fillna(0.4504, inplace = True)

# 환경
environment = pd.read_excel('./데이터/행복지수 데이터/대한민국행복지도_환경.xlsx')
environment.info() # 결측치 한개 - 대구광역시 서구
environment.drop('No', axis = 1, inplace = True)
environment = environment[['시도', '평균']]
environment.columns = ['시도', '환경평균']
environment['환경평균'].mean()
environment['환경평균'].median()
environment.fillna(0.5806, inplace = True)

# 데이터 병합하기





