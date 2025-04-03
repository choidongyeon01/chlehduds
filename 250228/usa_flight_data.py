# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:28:43 2025

@author: Jiyeon Baek

USA_flight_ data.py

20250228 team project
"""
import pandas as pd
import numpy as np
import glob
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# 1. 데이터 불러오기: 두 폴더의 모든 CSV 파일을 한꺼번에 읽어오기
folder1 = r"C:/Users/Admin/Desktop/JY/LG U+/20250228_project/dataverse_files_1987-1999/*.csv"
folder2 = r"C:/Users/Admin/Desktop/JY/LG U+/20250228_project/dataverse_files_2000-2008/*.csv"

# 두 폴더의 파일 리스트를 합치기
file_list = glob.glob(folder1) + glob.glob(folder2)
print("불러온 파일 개수:", len(file_list))

# 각 파일을 읽어서 리스트에 저장 (파일명에서 연도를 추출하여 'Year' 컬럼이 없으면 추가)
df_list = []
for file in file_list:
    temp_df = pd.read_csv(file)
    # 파일명에서 4자리 숫자를 찾아 연도로 사용 (예: "1987" 등)
    match = re.search(r'(\d{4})', file)
    if match:
        year = int(match.group(1))
        if 'Year' not in temp_df.columns:
            temp_df['Year'] = year
    df_list.append(temp_df)

# 모든 파일을 하나의 DataFrame으로 합치기
df_all = pd.concat(df_list, ignore_index=True)
print("전체 항공편 수:", df_all.shape[0])

# 합친 DataFrame을 CSV 파일로 저장 (지정된 경로에 저장)
output_path = r'C:/Users/Admin/Desktop/JY/LG U+/20250228_project/all_data.csv'
df_all.to_csv(output_path, index=False)
print("CSV 파일이 저장되었습니다:", output_path)


# -------------------------------
# 2. 추가 참조 데이터 불러오기
# -------------------------------
# 각 CSV 파일은 프로젝트 폴더 내에 있다고 가정
airports_df = pd.read_csv("C:/Users/Admin/Desktop/JY/LG U+/20250228_project/dataverse_files_2000-2008/airports.csv")
carriers_df = pd.read_csv("C:/Users/Admin/Desktop/JY/LG U+/20250228_project/dataverse_files_2000-2008/carriers.csv")
plane_df = pd.read_csv("C:/Users/Admin/Desktop/JY/LG U+/20250228_project/dataverse_files_2000-2008/plane-data.csv")
# variable-descriptions는 분석 참고용으로 불러올 수 있음 (필요시)
var_desc_df = pd.read_csv("C:/Users/Admin/Desktop/JY/LG U+/20250228_project/dataverse_files_2000-2008/variable-descriptions.csv")





































