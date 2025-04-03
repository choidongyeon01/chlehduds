# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:24:08 2025

@author: tuesv
"""

import pandas as pd
import folium
import json

seoul_sgg_stat = pd.read_excel('data_files/starbucks_location/files/seoul_sgg_stat.xlsx',
                               thousands = ',')

# 서울시 시군구 행정 경계 지도 파일
sgg_geojson_file_path = 'data_files/starbucks_location/maps/seoul_sgg.geojson'

seoul_sgg_geo2 = json.load(
    open(sgg_geojson_file_path, encoding = 'utf-8'))

starbucks_choropleth = folium.Map(location = [37.573050, 126.979189], 
                              tiles = 'CartoDB dark_matter',
                              zoom_start = 11)

folium.Choropleth(geo_data = seoul_sgg_geo2, 
                  data = seoul_sgg_stat,
                  columns = ['시군구명', '주민등록인구'],
                  fill_color = 'YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on = 'properties.SIG_KOR_NM').add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_choropleth_pop.html')


# 서울시 시군구별 사업체 수
sgg_geojson_file_path = 'data_files/starbucks_location/maps/seoul_sgg.geojson'

seoul_sgg_geo2 = json.load(
    open(sgg_geojson_file_path, encoding = 'utf-8'))

starbucks_choropleth = folium.Map(location = [37.573050, 126.979189], 
                              tiles = 'CartoDB dark_matter',
                              zoom_start = 11)

folium.Choropleth(geo_data = seoul_sgg_geo2, 
                  data = seoul_sgg_stat,
                  columns = ['시군구명', '사업체수'],
                  fill_color = 'YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on = 'properties.SIG_KOR_NM').add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_choropleth_biz.html')





















