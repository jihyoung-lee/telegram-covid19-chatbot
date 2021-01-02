import urllib.request
from bs4 import BeautifulSoup
import datetime

# 현재시간
now = datetime.datetime.now()
nowdate = now.strftime('%Y%m%d')  # 시간형식 변경
nowdate2 = now.strftime('%Y년 %m월 %d일')
# api 요청

ServiceKey =''
pageNo = 1
numOfRows = 1
startCreateDt = int(nowdate)
endCreateDt = int(nowdate)  # 오늘시간으로 자동업데이트

url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={ServiceKey}&pageNo={pageNo}&numOfRows={numOfRows}&startCreateDt={startCreateDt}&endCreateDt={endCreateDt} '
r = urllib.request.urlopen(url)
result = r.read()
soup = BeautifulSoup(result, 'lxml-xml')

# 리스트


gubun_list = []  # 지역 이름
defCnt_list = []  # 누적 확진자
incDec_list = []  # 신규 확진자

# column

gubun = soup.find_all('gubun')
defCnt = soup.find_all('defCnt')
incDec = soup.find_all('incDec')

for items in gubun:
    gubun_list.append(items.text)

for items in defCnt:
    defCnt_list.append(items.text)

for items in incDec:
    incDec_list.append(items.text)
