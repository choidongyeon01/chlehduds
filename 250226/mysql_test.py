# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:01:46 2025

@author: choi dong yean

MySQL 연동

pip install pymysql
"""

import pymysql
import pandas as pd

# python mysql에 연결
host = 'localhost'
user = 'root'
password = 'dongyean0525!'
db_name = 'sakila'

# 접속 : pymysql.connect()
# host = 접속주고(IP)
# user = 사용자 아이디
# password = 비밀번호
# db = 데이터베이스
# charset = 인코딩 (utf8)

conn = pymysql.connect(host = host,
                       user = user,
                       password = password,
                       db = db_name,
                       charset = 'utf8')

# 커서 생성 : query를 실행하는 execute()
# key-value => DictCursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

query = """
        select * from customer;
        """
        
# execute()로 query 실행
cursor.execute(query)

# 결과로 반환된 테이블의 모든 행을 가져오기 : cursor.fetchall()
execute_result = cursor.fetchall()

# 데이터 프레임
execute_df = pd.DataFrame(execute_result)

# DB 연결 종료
conn.close()


# ------------------------------------------ #


host = 'localhost'
user = 'root'
password = 'dongyean0525!'
db_name = 'sakila'
cursor = conn.cursor(pymysql.cursors.DictCursor)

# category
category = """
        select * from category;
        """
cursor.execute(category)
category_result = cursor.fetchall()
category_df = pd.DataFrame(category_result)

# film_category
film_category = """
        select * from film_category;
        """
cursor.execute(film_category)
film_category_result = cursor.fetchall()
film_category_df = pd.DataFrame(film_category_result)

# payment
payment = """
        select * from payment;
        """
cursor.execute(payment)
payment_result = cursor.fetchall()
payment_df = pd.DataFrame(payment_result)

conn.close()


import pandas as pd
join = pd.read_csv('join.csv')
category = pd.read_csv('category.csv')

join.columns
join = join[['amount', 'category_id']]

payment = pd.merge(join, category)

payment = payment[['name', 'amount']]

sum = payment.groupby(payment['name']).sum()


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
    
# 데이터 설정
labels = [
    "액션", "애니메이션", "유아", "클래식", "코미디", "다큐멘터리", "드라마", 
    "가족", "외국 영화", "게임", "호러", "음악", "최신 영화", "SF", "스포츠", "여행"
]
sizes = [306.29, 93.57, 266.59, 181.68, 168.70, 206.26, 132.78, 433.00, 
         363.03, 84.89, 614.71, 317.01, 368.27, 380.95, 219.48, 90.79]

# 파이 차트 생성
plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("장르별 지불금액")

# 차트 표시
plt.show()









