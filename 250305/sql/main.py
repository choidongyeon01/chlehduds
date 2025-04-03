# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 09:40:18 2025

@author: choi dong yean

파이썬 크롤러 제작
    yfinance를 호출하여 데이터를 수집하고 가공하여,
    MySQL 서버로 데이터를 저장하는 역할.
    
작업 순서
1. 파이썬 패키지 임포트
2. MySQL 접속 정보
3. 실제 주식 데이터를 가져오는 함수 생성 : getStock() <= getCompany()에서 호출
   데이터 가공 및 MySQL에 저장   
4. 크롤링 할 기업의 목록을 데이터베이스로 읽어 오는 함수 생성 : getCompany()
5. 파일을 실행할 때 처음 실행되는 코드
   if __name__ == '__main__': 
    
"""
### 1. 파이썬 패키지 임포트
from datetime import datetime, timedelta

import pymysql
import yfinance as yf
import pandas as pd

### 2. MySQL 접속 정보
hostName = 'localhost'
userName = 'root'
password = 'dongyean0525!'
dbName = 'us_stock'

mysql_conn = pymysql.connect(host = hostName,
                             user = userName,
                             password = password,
                             db = dbName)

### 3. 실제 주식 데이터를 가져 오는 함수 생성 : getStock(종목코드, 시작날짜, 종료날짜)
def getStock(_symbol, _start_date, _end_date):
    mysql_cur = mysql_conn.cursor()
    print('1' * 20)
    mysql_cur.execute("delete from us_stock.stock where date >= %s and date <= %s and symbol = %s", (_start_date, _end_date, _symbol))
    mysql_conn.commit()
    
    try:
        stock_price = yf.download(_symbol, start = _start_date, end = _end_date)
        print(stock_price)
        
        
        for index, row in stock_price.iterrow():
            _date = index.strftime('%Y-%m-%d')
            _open = float(row['Open'])
            _high = float(row['High'])
            _low = float(row['Low'])
            _close = float(row['Close'])
            _adj_close = float(101309500)
            _volume = float(row['Volume'])
            
            mysql_cur.execute("insert into us_stock.stock (date, symbol, open, high, low, close, adj_close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (_date, _symbol, _open, _high, _low, _close, _adj_close, _volume))
        mysql_conn.commit()
        
        mysql_cur.execute("update us_stock.nasdaq_company set open = %s, high = %s, low = %s, close = %s, adj_close = %s, volume = %s, last_crawel_date_stock = %s where symbol = %s", (_open, _high, _low, _close, _adj_close, _volume, _date, _symbol))
        mysql_conn.commit()

        
    except Exception as e:
        print('error for getStock() : ' + str(e))
        print('2' * 20)
        mysql_conn.commit()
        mysql_conn.close()
        
        return {'error for getStock() ': str(e)}


### 4. 크롤링 할 기업의 목록을 데이터베이스로 읽어 오는 함수 생성 : getCompany()
def getCompany():
    mysql_cur = mysql_conn.cursor()
    
    today = datetime.today() + timedelta(days = 1)

    try:
        mysql_cur.execute("select symbol, company_name, ipo_year, last_crawel_date_stock from us_stock.nasdaq_company where is_delete is null;")
        results = mysql_cur.fetchall()
        print(results)
        print('3' * 20)
        
        for row in results:
            _symbol = row[0]
            _company_name = row[1]
            
            if row[2] is None or row[2] == 0:
                _ipo_year = '1970'
            else:
                _ipo_year = row[2]
                
            if row[3] is None:
                _last_crawel_date_stock = str(_ipo_year) + '-01-01'
            else:
                _last_crawel_date_stock = row[3]
                
            print(_symbol)
            print('4' * 20)
            
            if "." in _symbol:
                print(_symbol)
                print('5' * 20)
            else:
                if "/" in _symbol:
                    print(_symbol)
                    print('6' * 20)
                else:
                    print(_last_crawel_date_stock)
                    print('7' * 20)
                    getStock(_symbol, _last_crawel_date_stock, today.strftime('%Y-%m-%d'))
        
    
    except Exception as e:
        print("error for getCompany(): " + str(e))
        print('8' * 20)
        mysql_conn.commit()
        mysql_conn.close()
        
        return {'error for getCompany() ': str(e)}


### 5. 파일을 실행할 때 처음 실행되는 코드
if __name__ == '__main__':
    getCompany()















