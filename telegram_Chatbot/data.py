import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from io import BytesIO
import datetime

# 현재시간
now = datetime.datetime.now()
nowdate = now.strftime('%Y%m%d')

# api요청

ServiceKey = 'vF9w%2FEtQmlLZaLXPV6ZrrOzZtZuMl9p0hGmz4PFW6DDnUGw0x4ob6HzuYwVct3EdVEbpxbdAEJukvJluA56gjA%3D%3D'
pageNo = 1
numOfRows = 1
startCreateDt = int(nowdate)
endCreateDt = int(nowdate) #오늘시간으로 자동업데이트

url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={ServiceKey}&pageNo={pageNo}&numOfRows={numOfRows}&startCreateDt={startCreateDt}&endCreateDt={endCreateDt} '
r = urllib.request.urlopen(url)
result = r.read()
soup = BeautifulSoup(result, 'lxml-xml')
list = ['gubun','gubunCn','incDec']
for items in soup.find_all(list):

    print(items.text)
    print("-----")#구분선


