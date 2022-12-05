#라이브러리 import
import requests
import pprint
import json
import pandas as pd
import streamlit as st
import altair as alt
file_path = "C:\\Users\hojin\Desktop\gwajea\python\gimal\simple.txt"
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=구로&dataTerm=DAILY&pageNo=1&numOfRows=100&returnType=json&serviceKey=KQRR%2BJLPRITcRv6CvRB1QUxmDQ%2BKmcKWMjK1A19g%2BiHLEbXTpqjWmut5pwHfKkH6O7KfqLSXxEmrLt6Ctooliw%3D%3D"

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
dataframe['total'] = pd.to_numeric(dataframe['khaiValue'])
dataframe['dust'] = pd.to_numeric(dataframe['pm10Value'])
time = dataframe['dataTime']
total = dataframe['total']
dust = dataframe['dust']
# # 바차트 올리기
st.write(total)
st.bar_chart(total)
st.bar_chart(dust)
