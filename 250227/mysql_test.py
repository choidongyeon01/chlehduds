# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:02:04 2025

@author: choi dong yean
"""

import pymysql
import pandas as pd

from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

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




# python mysql에 연결
host = 'localhost'
user = 'root'
password = 'dongyean0525!'
db = 'test'
charset = 'utf8'

df = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 1월 국내노선 여객 이용률.csv')

engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}')
conn = engine.connect()

df.to_sql(name = 'tmp2', con = engine, if_exists = 'replace', index = False)

conn.close()



# -----------------------------------------------#
# 항공사 운항 실태 조사
df1 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 1월 국내노선 여객 이용률.csv')
df2 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 2월 국내노선 여객 이용률.csv')
df3 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 3월 국내노선 여객 이용률.csv')
df4 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 4월 국내노선 여객 이용률.csv')
df5 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 5월 국내노선 여객 이용률.csv')
df6 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 6월 국내노선 여객 이용률.csv')
df7 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 7월 국내노선 여객 이용률.csv')
df8 = pd.read_csv('한국공항공사_국내노선 여객 이용률/2024년 8월 국내노선 여객 이용률.csv')

df_12 = pd.concat([df1, df2], ignore_index=True)
df_12 = df_12.rename(columns={'이용율':'이용률'})
df_34 = pd.concat([df3, df4], ignore_index=True)
df_56 = pd.concat([df5, df6], ignore_index=True)
df_78 = pd.concat([df7, df8], ignore_index=True)

df_1234 = pd.concat([df_12, df_34], ignore_index=True)
df_5678 = pd.concat([df_56, df_78], ignore_index=True)

# 1-8월 통합
df = pd.concat([df_1234, df_5678], ignore_index=True)
df.to_csv('국내노선 여객 이용 1-8월 통합.csv', index = False)

# MySQL 저장
host = 'localhost'
user = 'root'
password = 'dongyean0525!'
db = 'test'
charset = 'utf8'

df = pd.read_csv('국내노선 여객 이용 1-월 통합.csv')

engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}')
conn = engine.connect()

df.to_sql(name = '국내노선 여객 이용 1-월 통합', con = engine, if_exists = 'replace', index = False)

df2 = pd.read_csv('1-8월 그룹화 합산.csv')
df2.to_sql(name = '1-8월 그룹화 합산', con = engine, if_exists = 'replace', index = False)

conn.close()



# 국내노선 항공사 수
df_count = df.groupby(df['노선']).count()
df_count = df_count.sort_values('항공사', ascending = False)


# 국내노선 총 이용률
df_sum = df.groupby(['노선', '항공사']).sum()

df_sum['이용률'] = round((df_sum['여객수'] / df_sum['좌석수']) * 100, 1)
df_sum = df_sum.sort_values('이용률', ascending = False)

df_sum.to_csv("1-8월 그룹화 합산.csv", index = False)

# 국내노선 평균 이용률
df_mean = df.groupby(['노선', '항공사']).mean()
df_mean = df_mean.round(1)


# 국내노선 항공사별 평균 이용률 비교 - 막대그래프까지
df_airline_utilization = df_sum.groupby("항공사")["이용률"].mean().round(1)

# 그래프 그리기
plt.figure(figsize=(10, 5))
ax = df_airline_utilization.sort_values().plot(kind="bar", color="skyblue", edgecolor="black")

# 그래프 제목 및 축 레이블 설정
plt.xlabel("항공사")
plt.ylabel("평균 이용률 (%)")
plt.title("항공사별 평균 이용률 비교")
plt.xticks(rotation=45)
plt.ylim(0, 100)  # 이용률이 100% 넘지 않도록 제한 (필요시 조정 가능)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# 막대 위에 숫자 표시
for bar in ax.patches:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom', color='black')

# 그래프 표시
plt.show()






# ------------------------------------------------------ #
## 제주 노선 vs 비제주 노선 비교 ##
# '노선' 컬럼이 있다고 가정하고, 제주 포함 여부 확인
df_jeju = df[df["노선"].str.contains("제주", na=False)]  # 제주 포함 노선
df_non_jeju = df[~df["노선"].str.contains("제주", na=False)]  # 제주 미포함 노선

df_jeju = df_jeju.sort_values('이용률', ascending = False)
df_non_jeju = df_non_jeju.sort_values('이용률', ascending = False)

jeju_passengers = df_jeju["여객수"].mean().round(1)
non_jeju_passengers = df_non_jeju["여객수"].mean().round(1)

print(f"제주 노선 평균 여객 수: {jeju_passengers}")
print(f"비제주 노선 평균 여객 수: {non_jeju_passengers}")


# 각 카테고리의 평균 값을 계산
jeju_utilization = df_jeju["이용률"].mean().round(1)  # 제주 노선 이용률 평균
jeju_seats = df_jeju["좌석수"].mean().round(1)  # 제주 노선 좌석수 평균
jeju_passengers = df_jeju["여객수"].mean().round(1)  # 제주 노선 여객수 평균

non_jeju_utilization = df_non_jeju["이용률"].mean().round(1)  # 비제주 노선 이용률 평균
non_jeju_seats = df_non_jeju["좌석수"].mean().round(1)  # 비제주 노선 좌석수 평균
non_jeju_passengers = df_non_jeju["여객수"].mean().round(1)  # 비제주 노선 여객수 평균

# 비교할 항목
import numpy as np
categories = ["이용률(%)", "좌석수", "여객수"]
jeju_values = [jeju_utilization, jeju_seats, jeju_passengers]
non_jeju_values = [non_jeju_utilization, non_jeju_seats, non_jeju_passengers]

# 막대 그래프 설정
x = np.arange(len(categories))
width = 0.35  # 막대 너비

fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - width/2, jeju_values, width, label="제주 노선", color="orange")
bars2 = ax.bar(x + width/2, non_jeju_values, width, label="비제주 노선", color="skyblue")

# 그래프 설정
ax.set_ylabel("값")
ax.set_title("제주 노선 vs 비제주 노선 비교")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# 막대 위에 값 표시
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f"{height:.1f}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha="center", va="bottom")

plt.show()



# -------------------------------------------------------#
# 인덱스를 데이터로 변환
df_sum_reset = df_sum.reset_index()

# 인덱스에 '제주항공'이 포함된 행 필터링
df_jeju_air = df_sum_reset[df_sum_reset["항공사"] == "제주항공"]

df_jeju_air_route = df_jeju_air[['노선', '이용률']]

plt.figure(figsize=(10, 6))
bars = plt.barh(df_jeju_air_route['노선'], df_jeju_air_route['이용률'], color='orange')

# 그래프 제목과 축 라벨 설정
plt.title("제주항공 노선별 이용률")
plt.xlabel("이용률 (%)")
plt.ylabel("노선")

for bar in bars:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width():.1f}%', 
             va='center', ha='left', color='black', fontweight='bold')
    
# 그래프 표시
plt.tight_layout()
plt.show()







