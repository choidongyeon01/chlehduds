# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 09:20:02 2025

@author: choi dong yean
"""

import yfinance as yf
import FinanceDataReader as fdr

df = fdr.StockListing('KRX') # NASDAQ
stock = yf.download(종목코드, start = 시작날짜, end = 종료날짜)
