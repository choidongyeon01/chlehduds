# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:25:09 2025

@author: choi dong yean
"""

import pandas as pd
import os
import chardet  # 인코딩 자동 감지 라이브러리

folder_1 = "dataverse_files_1987-1999"
output_1 = "merged_1987_1994.csv"
first_file = True  # 첫 번째 파일 여부

def detect_encoding(file_path, num_bytes=100000):
    """파일에서 일부 데이터를 읽어 인코딩을 감지하는 함수"""
    with open(file_path, 'rb') as f:
        raw_data = f.read(num_bytes)
    result = chardet.detect(raw_data)
    return result['encoding']  # 감지된 인코딩 반환

def optimize_dtypes(df):
    """데이터프레임의 데이터 타입을 최적화하여 메모리 사용 줄이기"""
    for col in df.select_dtypes(include=["int64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast='integer')  # 정수형 데이터 다운캐스팅
    for col in df.select_dtypes(include=["float64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast='float')  # 실수형 데이터 다운캐스팅
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype("category")  # 문자열을 category로 변환
    return df

# 1987~1994년 데이터만 병합
for file in sorted(os.listdir(folder_1)):  
    if file.endswith(".csv") and int(file.split(".")[0]) >= 1987 and int(file.split(".")[0]) <= 1994:  
        file_path = os.path.join(folder_1, file)
        print(f"Processing: {file_path}")

        # 인코딩 자동 감지
        encoding_type = detect_encoding(file_path)
        print(f"Detected Encoding: {encoding_type}")

        # 감지된 인코딩으로 CSV 파일 읽기
        chunk_iter = pd.read_csv(file_path, chunksize=50000, encoding=encoding_type)  # 50,000개씩 처리 (메모리 절약)

        for chunk in chunk_iter:
            # 필요 없는 컬럼이 있다면 제거하는 코드 추가
            # chunk = chunk[['필요한 컬럼1', '필요한 컬럼2']]  # 예시로 필요한 컬럼만 선택

            # 데이터 타입 최적화
            chunk = optimize_dtypes(chunk)

            chunk["Year"] = int(file.split(".")[0])  # 파일명에서 연도 추출
            chunk.to_csv(output_1, mode="w" if first_file else "a", index=False, header=first_file)
            first_file = False  

print(f"병합 완료: {output_1}")






































