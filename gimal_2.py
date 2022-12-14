#라이브러리 import
import requests
import pprint
import json
import pandas as pd
import streamlit as st
import altair as alt

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=파주&dataTerm=DAILY&pageNo=1&numOfRows=100&returnType=json&serviceKey=FJ1n8Qg%2BskwumolGLdjbe0XiIBDwGE6onuyuuJ7DE%2FKp3mbiQ%2BC%2BjY5vCqZDpME18GxK%2Bw8bq%2BBj904iugdaSg%3D%3D"

image2 = 'https://github.com/jkdk9810/stream/blob/main/mise.png?raw=true'
image1 = 'https://github.com/jkdk9810/stream/blob/main/ozon.png?raw=true'

response = requests.get(url)

contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents))

## json을 DataFrame으로 변환하기 ##

#문자열을 json으로 변경
json_ob = json.loads(contents)
# print(type(json_ob)) #json타입 확인

# 필요한 내용만 꺼내기
body = json_ob['response']['body']['items']
# print(body)

# # Dataframe으로 만들기
dataframe = pd.DataFrame(body)

# # key 값 int으로 만들기
for i in range(len(dataframe['o3Value'])):
    if dataframe['o3Value'][i] == '-':
        dataframe['o3Value'][i] = '0'
        
for i in range(len(dataframe['pm10Value'])):
    if dataframe['pm10Value'][i] == '-':
        dataframe['pm10Value'][i] = '0'


dataframe['O3_Value'] = pd.to_numeric(dataframe['o3Value'])
dataframe['Dust_Value'] = pd.to_numeric(dataframe['pm10Value'])
time = dataframe['dataTime']
total = dataframe['O3_Value']
dust = dataframe['Dust_Value']

# # 바차트 올리기
#st.write(total)
st.image(image1)
st.bar_chart(total)
st.image(image2)
st.bar_chart(dust)

