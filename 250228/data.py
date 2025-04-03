# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:31:18 2025

@author: choi dong yean
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1987년도
df_1987 = pd.read_csv('dataverse_files_1987-1999/1987.csv')
df_1987.columns
df_1987['Month'].value_counts()
df_1987['DayOfWeek'].value_counts()
df_1987['UniqueCarrier'].value_counts()
df_1987['CancellationCode'].value_counts(dropna = False) # 전부 Nan
df_1987['Diverted'].value_counts(dropna = False)
df_1987['TailNum']

# 2008년도
df_1988 = pd.read_csv('dataverse_files_1987-1999/1988.csv')
df_1988.columns















# 통합
df_reduced = pd.read_csv('merged_1987_1994.csv')
df_reduced['Year'].value_counts()

airports_df = pd.read_csv("dataverse_files_2000-2008/airports.csv")
carriers_df = pd.read_csv("dataverse_files_2000-2008/carriers.csv")
plane_df = pd.read_csv("dataverse_files_2000-2008/plane-data.csv")
var_desc_df = pd.read_csv("dataverse_files_2000-2008/variable-descriptions.csv")

# plane_df 컬럼 year -> PlaneYear 변경
plane_df.rename(columns={'year': 'PlaneYear'}, inplace=True)
plane_df.info()

# PlanYear 결측값 확인
plane_df['PlaneYear'].value_counts()

# df_reduced['TailNum'] 데이터 타입 변경
df_reduced.info()
df_reduced['TailNum'] = df_reduced['TailNum'].astype(str)

# df_reduced와 plane_df 병합
df_reduced = pd.merge(df_reduced, plane_df[['tailnum', 'PlaneYear']], how='left',
                      left_on='TailNum', right_on='tailnum')



df_reduced.tail(3)
df_reduced['Year'].value_counts()


df_reduced['PlaneYear'].value_counts(dropna = False)

df_reduced['PlaneYear'] = df_reduced['PlaneYear'].dropna(subset = 'PlaneYear').astype(int)  # 0으로 대체
df_reduced['AircraftAge'] = df_reduced['Year'] - df_reduced['PlaneYear']
df_reduced = df_reduced[df_reduced['AircraftAge'] >= 0]

df_reduced.drop(columns=['tailnum'], inplace=True)
print("plane-data 병합 후 df_reduced 컬럼:", df_reduced.columns)

df_reduced = pd.merge(df_reduced, carriers_df, how='left',
                      left_on='UniqueCarrier', right_on='Code')





#----------------------------------------#











