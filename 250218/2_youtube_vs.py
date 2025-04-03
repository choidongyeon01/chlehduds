# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:11:43 2025

@author: choi dong yean
"""
import pandas as pd
import matplotlib.pyplot as plt

# 한글을 표기하기 위한 글꼴 변경(윈도우, macOS에 대해 각각 처리)
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')
    
# youtube_rank1.xlsx
df = pd.read_excel('./files/youtube_rank1.xlsx')

# 데이터
df.head()
df.tail()

# 구독자 수 : 0부터 10개만...
df['subscriber'][0:10]

# 만 => 0000
df['subscriber'].str.replace('만', '0000')
df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df.head()

df.info()

df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
df.info()


### 구독자 수 => 파이차트 => 채널 ###
# category => 카테고리 갯수
# replaced_subscriber => 카테고리별로 더하기
# 구독자 수, 채널 수 피봇 테이블 생성
# 데이터프레임.pivot_table()
# index = 'category'
# values = 'replaced_subscriber'
# aggfunc = ['sum', 'count']
pivot_df = df.pivot_table(index = 'category',
                          values = 'replaced_subscriber',
                          aggfunc = ['sum', 'count'])
pivot_df.head()
'''
                            sum               count
            replaced_subscriber replaced_subscriber
category                                           
[BJ/인물/연예인]           238590000                  57
[IT/기술/컴퓨터]            11070000                   6
[TV/방송]               285970000                 108
[게임]                   76830000                  45
[교육/강의]                31090000                  18
'''

# 데이터프레임의 칼럼명 변경
pivot_df.columns = ['subscriber_sum', 'category_count']
pivot_df.head()
'''
             subscriber_sum  category_count
category                                   
[BJ/인물/연예인]       238590000              57
[IT/기술/컴퓨터]        11070000               6
[TV/방송]           285970000             108
[게임]               76830000              45
[교육/강의]            31090000              18
'''

# 데이터프레임의 인덱스 초기화
pivot_df = pivot_df.reset_index()
pivot_df.head()
'''
      category  subscriber_sum  category_count
0  [BJ/인물/연예인]       238590000              57
1  [IT/기술/컴퓨터]        11070000               6
2      [TV/방송]       285970000             108
3         [게임]        76830000              45
4      [교육/강의]        31090000              18
'''

# 데이터프레임을 내림차순 정렬
pivot_df = pivot_df.sort_values(by = 'subscriber_sum', ascending = False)
pivot_df.head()
'''
       category  subscriber_sum  category_count
12   [음악/댄스/가수]       888860000             139
7         [미분류]       782940000             240
16     [키즈/어린이]       464770000             131
2       [TV/방송]       285970000             108
0   [BJ/인물/연예인]       238590000              57
'''

plt.figure(figsize = (30, 10))

# 카테고리별 구독자 수 시각화
plt.pie(pivot_df['subscriber_sum'],
        labels = pivot_df['category'],
        autopct = '%1.1f%%')
plt.show()

# 카테고리별 채널 수 시각화
pivot_df = pivot_df.sort_values(by = 'category_count', ascending = False)

plt.figure(figsize = (30, 10))
plt.pie(pivot_df['category_count'],
        labels = pivot_df['category'],
        autopct = '%1.1f%%')
plt.show()















