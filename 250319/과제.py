# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:02:44 2025

@author: choi dong yean
"""
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./bc_card_data/201906.csv')
df.head()
df.tail()

# 1-1. 서울시 거주/비거주 구하기
df.columns
df['MEGA_CTY_NM'].value_counts()

df['CSTMR_MEGA_CTY_NM'].value_counts()

df['CSTMR_GUBUN'].value_counts()

df = df[['REG_YYMM', 'MEGA_CTY_NM', 'CTY_RGN_NM', 'TP_BUZ_NO', 'TP_BUZ_NM',
           'CSTMR_MEGA_CTY_NO', 'CSTMR_MEGA_CTY_NM',
           'CSTMR_CTY_RGN_NO', 'CSTMR_CTY_RGN_NM', 'SEX_CTGO_CD',
           'AMT', 'CNT']]

df.loc[df['CSTMR_MEGA_CTY_NM'] == '서울특별시'].count()
df.loc[df['CSTMR_MEGA_CTY_NM'] != '서울특별시'].count()

# 데이터 정의
labels = ['Seoul', 'Not Seoul']
values = [54150, 45851]

# 막대그래프 생성
plt.bar(labels, values, color=['blue', 'orange'])

# 그래프 제목 및 라벨 설정
plt.xlabel('Dataset')
plt.ylabel('Values')
plt.title('Seoul / Not Seoul')

# 값 표시
for i, v in enumerate(values):
    plt.text(i, v + 500, str(v), ha='center', fontsize=12)

# 그래프 표시
plt.show()


# 1-2. 총 소비액 구하기

df.loc[df['CSTMR_MEGA_CTY_NM'] == '서울특별시', ['AMT']].sum()
df.loc[df['CSTMR_MEGA_CTY_NM'] != '서울특별시', ['AMT']].sum()

# 데이터 정의
labels = ['Seoul', 'Not Seoul']
values = [119663142676, 146587135822]

# 막대그래프 생성
plt.bar(labels, values, color=['blue', 'orange'])

# 그래프 제목 및 라벨 설정
plt.xlabel('Dataset')
plt.ylabel('Values')
plt.title('Seoul / Not Seoul')

# 값 표시
for i, v in enumerate(values):
    plt.text(i, v + 500, str(v), ha='center', fontsize=12)

# 그래프 표시
plt.show()


# 1-3. 성별 소비액 구하기
df1 = df.loc[df['CSTMR_MEGA_CTY_NM'] == '서울특별시']

# 서울시 성별 소비액
df.loc[df['CSTMR_MEGA_CTY_NM'] == '서울특별시', ['AMT']].sum()
df1.loc[df1['SEX_CTGO_CD'] == 1, ['AMT']].sum()
df1.loc[df1['SEX_CTGO_CD'] == 2, ['AMT']].sum()

# 비서울시 성별 소비액
df2 = df.loc[df['CSTMR_MEGA_CTY_NM'] != '서울특별시']

df.loc[df['CSTMR_MEGA_CTY_NM'] != '서울특별시', ['AMT']].sum()
df2.loc[df2['SEX_CTGO_CD'] == 1, ['AMT']].sum()
df2.loc[df2['SEX_CTGO_CD'] == 2, ['AMT']].sum()


# 데이터 정의
labels = ['Seoul', 'Not Seoul']
values = [[58128378947, 61534763729], [73579570815, 73007565007]]
genders = ['Male', 'Female']

# 막대그래프 생성
x = np.arange(len(labels))  # x 좌표 설정
width = 0.4  # 막대 너비

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, [v[0] for v in values], width, label='Male', color='blue')
rects2 = ax.bar(x + width/2, [v[1] for v in values], width, label='Female', color='orange')

# 그래프 제목 및 라벨 설정
ax.set_xlabel('Region')
ax.set_ylabel('Values')
ax.set_title('Comparison of Male and Female Values in Seoul and Not Seoul')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# 값 표시
for rects in [rects1, rects2]:
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 500000000, f'{height:,}', ha='center', fontsize=10)

# 그래프 표시
plt.show()


## 1-4. 카드 이용건수 구하기
df1.loc[:, ['CNT']].sum()
df2.loc[:, ['CNT']].sum()

# 데이터 정의
labels = ['Seoul', 'Not Seoul']
values = [5542462, 4950200]

# 막대그래프 생성
plt.bar(labels, values, color=['blue', 'orange'])

# 그래프 제목 및 라벨 설정
plt.xlabel('Dataset')
plt.ylabel('Values')
plt.title('Seoul / Not Seoul CNT')

# 값 표시
for i, v in enumerate(values):
    plt.text(i, v + 500, str(v), ha='center', fontsize=12)

# 그래프 표시
plt.show()


## 2-1 서울/비서울 편의점 소비액 구하기
df1.loc[df['TP_BUZ_NM'] == '편 의 점', ['AMT']].sum()

df2.loc[df['TP_BUZ_NM'] == '편 의 점', ['AMT']].sum()

# 데이터 정의
labels = ['Seoul', 'Not Seoul']
values = [6107016378, 1192167720]

# 막대그래프 생성
plt.bar(labels, values, color=['blue', 'orange'])

# 그래프 제목 및 라벨 설정
plt.xlabel('Dataset')
plt.ylabel('Values')
plt.title('Seoul / Not Seoul convenience store AMT')

# 값 표시
for i, v in enumerate(values):
    plt.text(i, v + 500, str(v), ha='center', fontsize=12)

# 그래프 표시
plt.show()


# 강남구 편의점 소비액 구하기
df1.loc[(df['CTY_RGN_NM'] == '강남구') & (df['TP_BUZ_NM'] == '편 의 점'), ['AMT']].sum()

# 데이터 정의
labels = ['Gangnam']
values = [529966670]

# 막대그래프 생성
plt.bar(labels, values, color=['blue'])

# 그래프 제목 및 라벨 설정
plt.xlabel('Dataset')
plt.ylabel('Values')
plt.title('Gangnam convenience store AMT')

# 값 표시
for i, v in enumerate(values):
    plt.text(i, v + 500, str(v), ha='center', fontsize=12)

# 그래프 표시
plt.show()


