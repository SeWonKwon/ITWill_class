# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:04:34 2020

@author: bigne
"""

# 문제423. 어제 조선일보에서 봉사로 검색했을 때 다운 받았던 기사에서 가장 많이 나오는 단어(어절)가 무엇인가?

stev = open("c:\\data\\bongsa.txt",encoding="UTF8")
stev2 = stev.read().split()
stev2.sort()
print(stev2)

from collections import Counter

count_list = Counter(stev2)
print(count_list)
#%%
result = count_list.most_common(30) # top 30개만 추출

print(result)

#%%문제424. 위의 결과를 for loop 문을 이용해서 아래와 같이 출력하시오 !
    # 수 33
    # 있다. 28
    # 했다. 24
    # 등 22
    # – 19
    # 더나은미래 17
    # 비자 17

for i in result:
    print(i[0],i[1])
#%%문제425. 어제 마지막 문제로 스크롤링 했던 형화 평가 게시글들에서 위와 같이 가장 많이 나오는 어절이 무엇인지 
# 출력하시오 !
from collections import Counter

movieco_greatexc = open("c:\\data\\GreatExpectations.txt", encoding="UTF8")
movieco_greatexc = movieco_greatexc.read().split()
print(movieco_greatexc)

count_list_movieco_greatexc = Counter(movieco_greatexc)
print(count_list_movieco_greatexc)
#%%
result = count_list_movieco_greatexc.most_common(30)
print(result)

#%%문제426. 웹스크롤링을 한 데이터로 감정분석(긍정적, 부정적)을 하기 위해 신성 이 형의 라라랜드 영화 평가를
#  다운로드 해서 c 밑에 data 밑에 두고 가장 많이 나오는 단어가 무엇인지 확인합니다.

from bs4 import BeautifulSoup
import urllib.request

def lalaland_review(num):
    f = open("c:\\data\\sample6_laland_review.txt",'w', encoding='utf8')    

    for i in range(1,num+1):
        url_str = 'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=134963&target=after&page='+str(i)
        url = urllib.request.Request(url_str)
        res = urllib.request.urlopen(url).read().decode('ansi')
        stuff = BeautifulSoup(res, 'html.parser')
        
        res1 = stuff.find_all('td', class_ = "title")
        
        for i in res1: 
            #time.sleep(1)    # 부하가 크지 않으므로 sleep 메소드는 껐다. 대용량 스크래핑시 켜주자
            f.write(str(i.get_text(' ', strip = True)[12:-2]) + '\n' )
    
    f.close()
    
    
lalaland_review(25) 

#%%

stev = open("c:\\data\\sample6_laland_review.txt",encoding="UTF8")
stev2 = stev.read().split()
stev2.sort()
print(stev2)

from collections import Counter

count_list = Counter(stev2)
print(count_list)
#%%
result = count_list.most_common(30) # top 30개만 추출

for i in result:
    print(i[0],i[1])
    
#%%문제427.  영화 라라랜드에서 긍정적인 단어가 몇건이 나오는지 출력하시오!

stev = open("c:\\data\\jobs.txt", encoding='UTF8')
stev2 = stev.read().split()              # 리스트
positive = open("c:\\data\\worddataset\\positive-words.txt")
pos = positive.read().split('\n')      # 리스트
cnt = 0

for k in stev2:
    if k.lower() in pos:
        cnt += 1

print(cnt)

#%% 문제428. 라라랜드 영화 평가에 부정단어는 몇개가 있고 단어들은 무엇인지 출력하시오!
stev = open("c:\\data\\jobs.txt", encoding='UTF8')
stev2 = stev.read().split()              # 리스트
negative = open("c:\\data\\negative-words.txt")
nega = negative.read().split('\n')      # 리스트
cnt = 0

for k in stev2:
    if k.lower() in nega:
        cnt += 1

print(cnt)

#%%

# 텍스트마이닝 데이터 정제

from wordcloud import WordCloud, STOPWORDS # 구두점 데이터 정제
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 , 데이타 클렌징
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정, 연산을 빠르게 하기위해 도와줌
usa_mask = np.array(Image.open("c:\\project\\usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'sample6_laland_review.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("c:\\project\\")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()

# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('c:\\project\\word.txt', 'r', encoding = 'utf-8') # 자주 나오지만 의미 없는 단어 리스트: word.txt
word = file.read().split(' ')
for i in word: # word 안에 있는 단어를 제거한다.
    text = re.sub(i,'',text) #re.sub('있다',",'있다') # < -- 라라랜드 게시글의 있다를 ''으로 대체하겠다.

# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=1000, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 100, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('c:/project/lalaland_cloud3.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
                  # 'jet' 클라우드 모양
plt.figure(figsize=(15,15))  #가로,세로 15size
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off") # 축표시 없음

#%%문제430. (점심시간 문제) 어제 마지막 문제로 받았던 영화 평가들 또는 어제 스크롤링했던 기사들을
#하나 선택해서 워드 클라우드로 그리고 그림을 올리고 검사받으세요~~~

from wordcloud import WordCloud, STOPWORDS # 구두점 데이터 정제
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 , 데이타 클렌징
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정, 연산을 빠르게 하기위해 도와줌
usa_mask = np.array(Image.open("c:\\project\\usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'GreatExpectations.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("c:\\project\\")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()

# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('c:\\project\\word.txt', 'r', encoding = 'utf-8') # 자주 나오지만 의미 없는 단어 리스트: word.txt
word = file.read().split(' ')
for i in word: # word 안에 있는 단어를 제거한다.
    text = re.sub(i,'',text) #re.sub('있다',",'있다') # < -- 라라랜드 게시글의 있다를 ''으로 대체하겠다.
# for i in list(word):  
#     if len(i) <= 1:
#         word.remove(i)
# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=400, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 150, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('c:/project/lalaland_cloud3.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
                  # 'jet' 클라우드 모양
plt.figure(figsize=(15,15))  #가로,세로 15size
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off") # 축표시 없음

#%%











#%%
stev = open ("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos= []
nag=[]
for i in stev2:
    if int(i[6:8])>=6:
        pos.append(i[8:])
    else:
        nag.append(i[8:])
print(pos)

# 문제434. 위의 pos 에 들어 있는 긍정 들을 c 드라이브 밑에 project 밑에 pos_lala.txt로 저장하시오.
f = open("c:\\project\\pos_lala.txt",'w',encoding='UTF8')
f.writelines(pos)
f.close()

#%%문제435. 6점 미만인 글들은 nag_lala.txt.로 c 드라이브 밑에 project 밑에 저장되게 하시오!

f = open("c:\\project\\nag_lala.txt",'w',encoding='UTF8')
f.writelines(nag)
f.close()

#%%문제436. 그러면 위의 pos_lala_txt 의 글과 nag_lala.txt 의 글을 워드 클라우드로 각각 시각화 하시오.



from wordcloud import WordCloud, STOPWORDS # 구두점 데이터 정제
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 , 데이타 클렌징
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정, 연산을 빠르게 하기위해 도와줌
usa_mask = np.array(Image.open("c:\\project\\usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
# script = 'pos_lala.txt'
script = 'nag_lala.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("c:\\project\\")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()

# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('c:\\project\\word.txt', 'r', encoding = 'utf-8') # 자주 나오지만 의미 없는 단어 리스트: word.txt
word = file.read().split(' ')
for i in word: # word 안에 있는 단어를 제거한다.
    text = re.sub(i,'',text) #re.sub('있다',",'있다') # < -- 라라랜드 게시글의 있다를 ''으로 대체하겠다.
# for i in list(word):  
#     if len(i) <= 1:
#         word.remove(i)
# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=400, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 150, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('c:/project/nag_lalaword.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
                  # 'jet' 클라우드 모양
plt.figure(figsize=(15,15))  #가로,세로 15size
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off") # 축표시 없음

#%%문제437. 종미누나 코드

from bs4 import BeautifulSoup
import urllib.request

a = []
b = []

def cinema():
    for i in range(1,25):
        list_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page='+str(i)
        # f = open("c:\\data\\cinema1.txt",'w',encoding = 'UTF8')
        url = urllib.request.Request(list_url)
        result = urllib.request.urlopen(url).read().decode("cp949")
        soup = BeautifulSoup(result,"html.parser")
           
        result1 = soup.find_all('td',class_ ="title")                   
        for i in result1:
            a.append(str(i.get_text(" ",strip=True)) + "\n")

        for j in a:
            b.append( [ (j.split('-')[0][:-4]),(j.split('-')[1][9:11]),(j.split('-')[1][12:-3])  ]  ) 
    
cinema()
for i in range(len(b)): 
    print(b[i][1],b[i][0])

#%%
pos= []
nag=[]
for i in range(len(b)):
    if int(b[i][1].replace('점','0').replace('리고','0'))>=6:
        pos.append(b[i][0])
    else:
        nag.append(b[i][0])
print(pos)
print(nag)
#%%
# 문제434. 위의 pos 에 들어 있는 긍정 들을 c 드라이브 밑에 project 밑에 pos_lala.txt로 저장하시오.
f = open("c:\\project\\pos_lala.txt",'w',encoding='UTF8')
f.writelines(pos)
f.close()


stev = open("c:\\data\\cinema1.txt", encoding="UTF8")
stev2 = stev.readlines()
stev3= []
for i  in stev2:
    # stev3.append=list(i)
    print(i)
#     print(i[1])
# print(stev2)



#%%

######################################################

import urllib.request # 웹 url을 파이썬이 인식 할 수 있게하는 패키지
from  bs4 import BeautifulSoup # html에서 데이터 검색을 용이하게 하는 패키지
from selenium import webdriver  
# selenium : 웹 애플리케이션의 테스트를 자동화하기 위한 프레임 워크 
# 손으로 클릭하면서 컴퓨터가 대신하면서 스크롤링하게 하는 패키지

from selenium.webdriver.common.keys import Keys
import time       # 중간중간 sleep 을 걸어야 해서 time 모듈 import

########################### url 받아오기 ###########################

# 웹브라우져로 크롬을 사용할거라서 크롬 드라이버를 다운받아 아래 파일경로의 위치에 둔다
# 팬텀 js로 하면 백그라운드로 실행할 수 있음
binary = 'c:\\chromedriver\\chromedriver.exe'

# 브라우져를 인스턴스화
browser = webdriver.Chrome(binary)

# 구글의 이미지 검색 url 받아옴(아무것도 안 쳤을때의 url) 
browser.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl") 

# 구글의 이미지 검색에 해당하는 input 창의 id 가 '  ?  ' 임(검색창에 해당하는 html코드를 찾아서 elem 사용하도록 설정)
# input창 찾는 방법은 원노트에 있음

# elem = browser.find_elements_by_class_name('gLFyf gsfi') # Tip : f12누른후 커서를 검색창에 올려두고 id를 찾으면 best

elem = browser.find_element_by_xpath("//*[@class='gLFyf gsfi']")  # 위의 코드대로 하거나 이렇게 하거나 둘 중 하나 select


########################### 검색어 입력 ###########################

# elem 이 input 창과 연결되어 스스로 햄버거를 검색
elem.send_keys("고양이") # 여기에 스크롤링하고싶은 검색어를 입력

# 웹에서의 submit 은 엔터의 역할을 함
elem.submit()

# 현재 결과 더보기는 구현 되어있지 않은상태 -> 구글의 경우 400개 image가 저장됨.

########################### 반복할 횟수 ###########################

# 스크롤을 내리려면 브라우져 이미지 검색결과 부분(바디부분)에 마우스 클릭 한번 하고 End키를 눌러야함

for i in range(1, 6): # 5번 스크롤 내려가게 구현된 상태 range(1,5)
    browser.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(2)          # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌 / 키보드 end키를 총 5번 누르는데 end1번누르고 10초 쉼

time.sleep(2)                      # 네트워크 느릴까봐 안정성 위해 sleep 해줌(이거 안하면 하얀색 이미지가 다운받아질 수 있음.)
html = browser.page_source         # 크롬브라우져에서 현재 불러온 소스 가져옴
soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정


browser.find_element_by_xpath("//*[@class='mye4qd']").click()  # 여기가 결과 더보기 코드입니다

for i in range(1, 5): # 4번 스크롤 내려가게 구현된 상태 range(1,5)
    browser.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(2)          # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌 / 키보드 end키를 총 5번 누르는데 end1번누르고 10초 쉼

time.sleep(2)                      # 네트워크 느릴까봐 안정성 위해 sleep 해줌(이거 안하면 하얀색 이미지가 다운받아질 수 있음.)
html = browser.page_source         # 크롬브라우져에서 현재 불러온 소스 가져옴
soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정

########################### 그림파일 저장 ###########################

### 검색한 구글 이미지의 url을 따오는 코드 ###
def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="rg_i Q4LuWd")  # 구글 이미지 url 이 있는 img 태그의 _img 클래스에 가서 (f12로 확인가능.)
    for im in imgList:
        try :
            params.append(im["src"])                   # params 리스트에 image url 을 담음.
        except KeyError:
            params.append(im["data-src"])
    return params

# except부분
# 이미지의 상세 url 의 값이 있는 src 가 없을 경우
# data-src 로 가져오시오 ~  


def fetch_detail_url():
    params = fetch_list_url()

    for idx,p in enumerate(params,1):
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "c:\\gimages\\" + str(idx) + "_google.jpg")

# enumerate 는 리스트의 모든 요소를 인덱스와 쌍으로 추출
# 하는 함수 . 숫자 1은 인덱스를 1부터 시작해라 ~

fetch_detail_url()

# 끝나면 브라우져 닫기
browser.quit()

#%%

import  urllib.request
from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

binary = 'c:\\chromedriver\\chromedriver.exe'

browser = webdriver.Chrome(binary)

browser.get("https://search.naver.com/search.naver?where=image&amp;sm=stb_nmr&amp;")

elem = browser.find_element_by_id("nx_query")
#<input type="text" id="nx_query" name="query" class="box_window" 

#find_elements_by_class_name("")
#클래스 이름으로 찾을때.

# 검색어 입력
elem.send_keys("아이언맨")

elem.submit()

# 반복할 횟수

for i in range(1,2):

    browser.find_element_by_xpath("//body").send_keys(Keys.END)

    time.sleep(5)

time.sleep(5)

html = browser.page_source
soup = BeautifulSoup(html,"lxml")

#print(soup)

#print(len(soup))



def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="_img")
    for im in imgList:
        params.append(im["src"])
    return params

def fetch_detail_url():

    params = fetch_list_url()

    #print(params)

    a = 1

    for p in params:

        # 다운받을 폴더경로 입력

        urllib.request.urlretrieve(p, "d:/naverImages/"+ str(a) + ".jpg" )
        a = a + 1
    params = fetch_list_url()
    #print(params)
    a = 1
    for p in params:
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "c:\\naverImages\\"+ str(a) + ".jpg" )
        a = a + 1

fetch_detail_url()

browser.quit()


#%%
import  urllib.request

from  bs4  import  BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

import time



binary = 'c:\\chromedriver\\chromedriver.exe'

browser = webdriver.Chrome(binary)

browser.get("https://search.naver.com/search.naver?where=image&amp;sm=stb_nmr&amp;")

elem = browser.find_element_by_id("nx_query")

#find_elements_by_class_name("")

browser.maximize_window()  

# 검색어 입력

elem.send_keys("아이언맨")

elem.submit()

action = ActionChains(browser)

# 반복할 횟수

for i in range(1,2):

    browser.find_element_by_xpath("//body").send_keys(Keys.END)

    time.sleep(10)
    
    # action.move_to_element_by_xpath("//body")
    
    # time.sleep(5)
    
    

time.sleep(10)

html = browser.page_source

soup = BeautifulSoup(html,"lxml")

#print(soup)

#print(len(soup))



def fetch_list_url():

    params = []

    imgList = soup.find_all("img", class_="_img")

    for im in imgList:

        params.append(im["src"])

    return params

time.sleep(3)



def  fetch_detail_url():

    params = fetch_list_url()

    #print(params)

    a = 1

    for p in params:

        # 다운받을 폴더경로 입력

        urllib.request.urlretrieve(p, "c:/naverImages/ion"+ str(a) + ".jpg" )

        time.sleep(0.5)

        a = a + 1

        

fetch_detail_url()



browser.quit()


#%%문제439. (오늘의 마지막 문제)  마이크로 소프트 회사에서 만든 
#            검색 페이지인 bing 에서 이미지 검색을 할 수 있도록 하는
#            웹스크롤링 코드를 작성하시오 ! 
#            ( 네이버 코드를 좀 수정하면 됩니다.)

# 딥러닝 수업 전까지 학습하고 싶은 이미지 두가지를 정해서 사진을 
# 스크롤링하세요 ~ ( 한클래스 당 2000장)

■ bing 이미지 url 주소  
https://www.bing.com/images?FORM=Z9LH

#%% 빙 이미지 다운로드

import  urllib.request
from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time



binary = 'c:\\chromedriver\\chromedriver.exe'

browser = webdriver.Chrome(binary)

browser.get("https://www.bing.com/images?FORM=Z9LH")


elem = browser.find_element_by_id("sb_form_q")
time.sleep(2)
elem.send_keys("고양이")

elem.submit()

# xpath = '//a[@class onclick href="https://adcr.naver.com/adcr?x=0vrusjBLl4SAHvcIKI0hzf///w==k8LqFWS871wbVskrJsdbLXxoqlUO2/qsIY3JBmzxbUfI+yNYBQ9M2iWMhAFzh0bpZOA6VkOAvbnudq0ZRs6FNwfOyyec0TOs1t49bESKQzJ9GTJDhqhC1V4zybxCMs9tWInEUrzC6XZoUn4QkW6RIMWYwF1mrHB6DvftAviikh7o0PowK6rmwDcC8NL+s1ilpTv+CPzNh4mdS1ycNgfTaQZYrnRAhXp78lJjanVYk5uBTqrwq3fmNbXjponkQWIPgghW5U37WZFXVIM//lrBJpWl8lKoJD23Dei1GlxChk2q9Ddz5l3PlfupE3GcaNOAvCv0IuHX5UNdf7kr6wdKGweT0AGstTWQXi5HbXgDnNNwraAa/5Omd70r3KGwtT4WV9QRJoAYo5gDd6itvl62zlge+ILDRTlBn20ZK3FkRFUqb6qnzARmm5P55F0bVOHWNEwUgkZX4YJY9kb4ylIJ9LwxtPN9vDu3txjTVsNL37P1mqrcuLbMmwHl93HRA5vc/Xwud19elePff9ZTRaFKbZaFxQGDGpb4a94pK/wIgQLYFsnsbVlFZpl7pDlDkpLsowru9VhdWOHkbNgHlt4gwFWZRHvf719ezFYGYvLzOWRq4sqsHIhtsJd+Kf4dli2GAzW/l6kISr21bJ9SFrPYv6CATLOO1o7TQshGd1wwpKT1jTJFmrmbC8zPKBNMs+JWbncap9Bfc/daKZFvF9bXNuZH6ZSoXOwtyCcuf6PLG3mdGEStnAFIZPJqpbSE3BfLS"]'
# movetoimage = browser.find_element_by_xpath(xpath)
# movetoimage.click()

#%%
<li class="" data-menuurl="" id="b-scopeListItem-images"><a target="" aria-current="false" href="/images/search?q=%ea%b3%a0%ec%96%91%ec%9d%b4&amp;FORM=HDRSC2" h="ID=SERP,5020.1">이미지</a></li>
<a class="" onclick="" href="https://adcr.naver.com/adcr?x=0vrusjBLl4SAHvcIKI0hzf///w==k8LqFWS871wbVskrJsdbLXxoqlUO2/qsIY3JBmzxbUfI+yNYBQ9M2iWMhAFzh0bpZOA6VkOAvbnudq0ZRs6FNwfOyyec0TOs1t49bESKQzJ9GTJDhqhC1V4zybxCMs9tWInEUrzC6XZoUn4QkW6RIMWYwF1mrHB6DvftAviikh7o0PowK6rmwDcC8NL+s1ilpTv+CPzNh4mdS1ycNgfTaQZYrnRAhXp78lJjanVYk5uBTqrwq3fmNbXjponkQWIPgghW5U37WZFXVIM//lrBJpWl8lKoJD23Dei1GlxChk2q9Ddz5l3PlfupE3GcaNOAvCv0IuHX5UNdf7kr6wdKGweT0AGstTWQXi5HbXgDnNNwraAa/5Omd70r3KGwtT4WV9QRJoAYo5gDd6itvl62zlge+ILDRTlBn20ZK3FkRFUqb6qnzARmm5P55F0bVOHWNEwUgkZX4YJY9kb4ylIJ9LwxtPN9vDu3txjTVsNL37P1mqrcuLbMmwHl93HRA5vc/Xwud19elePff9ZTRaFKbZaFxQGDGpb4a94pK/wIgQLYFsnsbVlFZpl7pDlDkpLsowru9VhdWOHkbNgHlt4gwFWZRHvf719ezFYGYvLzOWRq4sqsHIhtsJd+Kf4dli2GAzW/l6kISr21bJ9SFrPYv6CATLOO1o7TQshGd1wwpKT1jTJFmrmbC8zPKBNMs+JWbncap9Bfc/daKZFvF9bXNuZH6ZSoXOwtyCcuf6PLG3mdGEStnAFIZPJqpbSE3BfLS" h="ID=SERP,5561.1,Ads">고양이모래</a>
#%%
#
# action = webdriver.common.action_chains.ActionChains(driver)
# action.move_to_element_with_offset(el, 5, 5)
# action.click()
# action.perform()
# action = ActionChains(browser)
# 
# HTML < button class="closeBtn">
# 태그[@속성="속성값"]
# # 반복할 횟수
# borwer.execute_script("window.scrollTo(0, Y)") 
# brower.body.scrollHeight
#
#
for i in range(1,3):

    browser.find_element_by_xpath("//body").send_keys(Keys.END)

    time.sleep(1)
    
    # action.move_to_element_by_xpath("//body")
    
    # time.sleep(5)
    
    

time.sleep(5)

html = browser.page_source

soup = BeautifulSoup(html,"lxml")

#print(soup)

#print(len(soup))



def fetch_list_url():

    params = []

    imgList = soup.find_all("img", class_="mimg")

    for im in imgList:

        params.append(im["src"])

    return params

time.sleep(3)



def  fetch_detail_url():

    params = fetch_list_url()

    #print(params)

    a = 1

    for p in params:

        # 다운받을 폴더경로 입력

        urllib.request.urlretrieve(p, "c:/bing/cat_bing_"+ str(a) + ".jpg" )

        time.sleep(0.5)

        a = a + 1

        

fetch_detail_url()



browser.quit()

#%% 빙 이미지 스크롤링 

import  urllib.request
from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time



binary = 'c:\\chromedriver\\chromedriver.exe'

browser = webdriver.Chrome(binary)

browser.get("https://www.bing.com/images?FORM=Z9LH")

# 검색어 입력
elem = browser.find_element_by_id("sb_form_q")
time.sleep(2)
elem.send_keys("cat")
elem.submit()



#브라우저 내려서 확인하기.
for i in range(1,15):

    browser.find_element_by_xpath("//body").send_keys(Keys.END)

    time.sleep(3)

#브라우져상의 소스 지정
html = browser.page_source

soup = BeautifulSoup(html,"lxml")

#이미지 주소 url 긁어오는 함수 정의
time.sleep(5)

def fetch_list_url():

    params = []

    imgList = soup.find_all("img", class_="mimg")

    for im in imgList:

        params.append(im["src"])

    return params

# 이미지 저장하는 함수 정의
def  fetch_detail_url():

    params = fetch_list_url()
    
    time.sleep(5)
    
    a = 1

    for p in params:

        # 다운받을 폴더경로 입력

        urllib.request.urlretrieve(p, "c:/Images/Cat/Bing/cat_bing_"+ str(a) + ".jpg" )

        time.sleep(0.3)

        a = a + 1

fetch_detail_url()

browser.quit()

