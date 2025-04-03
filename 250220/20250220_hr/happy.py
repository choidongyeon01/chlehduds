# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:10:53 2025

@author: Admin

건강 관련 데이터 분석

    행복은 건강에 영향을 주는 중요한 요소.
    삶에 영향을 주는 중요 요소들을 포함하여 측정한 
    행복지수 자료를 분석 대상으로 요소 간의 상관관계를 분석
"""
from pandas import *

happy_life = read_excel('./data/대한민국행복지도_삶의만족도.xlsx')
happy_health = read_excel('./data/대한민국행복지도_건강.xlsx')
happy_safe = read_excel('./data/대한민국행복지도_안전.xlsx')
happy_environ = read_excel('./data/대한민국행복지도_환경.xlsx')
happy_econo = read_excel('./data/대한민국행복지도_경제.xlsx')
happy_edu = read_excel('./data/대한민국행복지도_교육.xlsx')
happy_relation = read_excel('./data/대한민국행복지도_관계및사회참여.xlsx')
happy_leisure = read_excel('./data/대한민국행복지도_여가.xlsx')

### 데이터 병합 ###
city = list(happy_life['시도'].unique())
happy_merge = DataFrame( {'시도' : city} )

life = happy_life['삶의 만족도'].groupby(by=happy_life['시도']).mean()
happy_merge = merge(happy_merge, life, on='시도')

health = happy_health['평균'].groupby(by=happy_health['시도']).mean()
happy_merge = merge(happy_merge, health.rename('건강'), on='시도')

safe = happy_safe['평균'].groupby(by=happy_safe['시도']).mean()
happy_merge = merge(happy_merge, safe.rename('안전'), on='시도')

environ = happy_environ['평균'].groupby(by=happy_environ['시도']).mean()
happy_merge = merge(happy_merge, environ.rename('환경'), on='시도')

econo = happy_econo['평균'].groupby(by=happy_econo['시도']).mean()
happy_merge = merge(happy_merge, econo.rename('경제'), on='시도')

edu = happy_edu['평균'].groupby(by=happy_edu['시도']).mean()
happy_merge = merge(happy_merge, edu.rename('교육'), on='시도')

relation = happy_relation['평균'].groupby(by=happy_relation['시도']).mean()
happy_merge = merge(happy_merge, relation.rename('관계및사회참여'), on='시도')

leisure = happy_leisure['평균'].groupby(by=happy_leisure['시도']).mean()
happy_merge = merge(happy_merge, leisure.rename('여가'), on='시도')

### 데이터 검산 ###
print(happy_merge['삶의 만족도'].mean())
print(happy_life['삶의 만족도'].mean())

print(happy_merge['건강'].mean())
print(happy_health['평균'].mean())

print(happy_merge['안전'].mean())
print(happy_safe['평균'].mean())

print(happy_merge['환경'].mean())
print(happy_environ['평균'].mean())

print(happy_merge['경제'].mean())
print(happy_econo['평균'].mean())

print(happy_merge['교육'].mean())
print(happy_edu['평균'].mean())

print(happy_merge['관계및사회참여'].mean())
print(happy_relation['평균'].mean())

print(happy_merge['여가'].mean())
print(happy_leisure['평균'].mean())

happy_merge.isnull().sum()


### 데이터 분석 및 시각화 ###
# 데이터 분석

happy_merge.describe()

happy_merge.mean(axis=0, numeric_only=True)

# dtype: float64
happy_merge.mean(axis=1, numeric_only=True)
happy_merge.set_index('시도').mean(axis=1)

happy_merge.corr(numeric_only=True)


## 시도별 지역에 따라 행복지수가 얼나마 차이가 나는지 시각화
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import platform 

font_path = ''
if platform.system() == 'Windows': 
    font_path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = font_path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    font_path = '/Users/$USER/Library/Fonts/AppleGothic.ttf'
    rc('font', family = 'AppleGothic')
else: 
    print('Check your OS system')

# 선 그래프
plt.figure(figsize=(15,6))
items = list(happy_merge.columns[1:9])
for a in items:
    chartdata = happy_merge[a]
    plt.plot(chartdata, marker='o', label=a)

plt.xlabel('시도')
plt.ylabel('수치')
plt.xticks(range(17), happy_merge['시도'],fontsize=8)
plt.title('대한민국 행복지수')
plt.legend()
plt.grid()
plt.show()

# 막대 그래프.
from numpy import *

happy_merge.plot(kind='bar', xlabel='시도', ylabel='수치', figsize=(15,20), grid=True, subplots=True)

plt.suptitle('대한민국 행복지수', fontsize=25)
plt.tight_layout(pad = 8, h_pad = 2)
plt.xticks(arange(17), city, rotation=360)
plt.show()


# 히트맵 그래프
import seaborn as sns

plt.figure(figsize=(15,13))
plt.title('대한민국 행복지수 상관관계', fontsize=25)
plt.rc('axes', unicode_minus=False)

correlation_mat = happy_merge.corr(numeric_only=True)
upp_mat = triu(correlation_mat)

sns.heatmap(correlation_mat, mask=upp_mat, annot=True, cmap='RdYlGn')
plt.show()

"""
환경이 좋아지면 삶의 만족도가 높아진다.
경제가 높을 수록 환경이 나빠진다.
라는 상관 관게를 확인
"""































