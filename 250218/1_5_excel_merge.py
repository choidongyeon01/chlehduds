# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:14:58 2025

@author: choi dong yean
"""

# 크롤링 결과가 담긴 멜론, 벅스, 지니 크롤링 엑셀 파일 통합
import pandas as pd

excel_names = ['./files/melon.xlsx',
               './files/bugs.xlsx',
               './files/genie.xlsx']

appended_data = pd.DataFrame()

for name in excel_names:
    pd_data = pd.read_excel(name)
    
    appended_data = pd.concat([appended_data, pd_data],
                              ignore_index = True)

appended_data.index

appended_data.to_excel('./files/total.xlsx', index = False)

'''
appended_data = appended_data.append(pd_data) <== ERROR
'''






















