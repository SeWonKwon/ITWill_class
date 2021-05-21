# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:30:41 2020

@author: bigne
"""

#%%예제1. ebs 레이디버그 시청자 게시판의 url 을 가지고 직접 html 문서를 내려 받을 수 있도록 
#  코드를 구현 ( 어제는 우리가 ctl + s 를 누르고 웹페이지를 우리 피씨에 저장하고 구현을 했는데
# 오늘은 그렇게 하지 않고 웹에서 바로 html 문서를 내려 받을 수 있도록 구현)

from bs4 import BeautifulSoup
import urllib.request  # 웹상의 url 을 파이썬이 인식 할 수 있도록 해주는 모듈

list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url) # 사람이 알아 볼수 있는 위의 url 을 
                                        # 파이썬이 알아 볼수 있도록 변환, 첫번째 작업 

result = urllib.request.urlopen(url).read().decode("UTF-8")
                                        # 두번째 작업 #위의 url의 html 문서들을 result 변수에 담았다.
                                                                              
print(result) # 위의 url 의 html 전체 문서가 다 출력되고 있음.

# 예제2. 위에서 긁어온 html 코드를  Beautiful soup 의 함수를 이용해서 
#        웹스크롤링 할 수 있도록 Beautiful soup을 이용해서 파싱 할수 있도록 

soup = BeautifulSoup(result,"html.parser")
print(soup)

#%%예제3. 지금 페이지의 시청자 게시판의 글 내용에 해당하는 부분의 테그와 클래스 이름을 알아내시오.
<p class='con'>
#%% p 테그중에서 class 가 con 에 해당하는 부분을 스크롤링 하시오 !

result = urllib.request.urlopen(url).read().decode("UTF-8")
soup = BeautifulSoup(result,"html.parser")
result2 = soup.find_all( 'p', class_ = 'con') # 비교 find_all 과 find 
print(result2)

# find 함수는 맨 처음 하나만 가져 오는데 find_all 은 p 테그에 class 이름 con 에 
#  해당하는 부분을 모두 가져온다.

#예제5 위의 결과에서 html 문서 말고 한글 텍스트만 가져오시오!

# result2 는 리스트 이기 때문에 get_text를 바로 못 써준다. for로 돌리자

for i in result2:
    print(i.get_text())
    
#예제6. 위에서 출력되고 있는 텍스트들이 좀더 깔끔하게 나오게 하시오!

for i in result2:
    print(i.get_text(" ",strip=True))


#%%예제7. 위에서 출력되고 있는 텍스트들이 params 라는 비어있는 리스트에 담기게 하시오!
params1 = []
for i in result2:
    params1.append(i.get_text(" ",strip=True))
print(params)
# !\r\n\r\n\r\n\r\n 이런 것들이 같이 나오기 때문에 정제가 필요하다. 나중에 한꺼번에 하자
#%%예제8. 게시글을 올린 날짜를 스크롤링하기 위해서 게시글 날짜가 있는 html 문서의 
# 테그 이름과 클래스 이름을 확인하시오 !
<span class="date"> # 테그 이름은 span 이고 클래스 이름 date 입니다.

#%%예제9. 위의 날짜를 모두 스크롤링해서 params2 라는 리스트에 담으시오~

result = urllib.request.urlopen(url).read().decode("UTF-8")
soup = BeautifulSoup(result,"html.parser")
result3 = soup.find_all( 'span', class_ = 'date') # 비교 find_all 과 find 
params2 = []
for i in result3:
    params2.append(i.get_text(" ",strip=True))
print(params2)

#%%예제10. 위의 날짜와 본문 내용이 아래와 같이 출력되게 하시오!
# 2020.12.11 19:52 재미있 다
# 2020.12.11 19:06 어제 흐름상 종영 같지 않았는데 갑자기 끝이네요??
# 2020.12.11 01:35 〈미라큘러스: 레이디버그와 블랙캣〉종영 안내!

for i,j in zip(params,params2):
    print(j+ '  ' +i)
    
#%%에제11. 아래와 같이 출력되게 하시오
# http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=1&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&
# http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=2&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&
# http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=3&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&   
# http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=22&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&
# page 번호만 다르고 나머지는 다 똑같다.

for page in range(1,23):
    print("http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(page)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&")

#%%예제12. (중요) 레이디 버그 게시판 전체의 글을 다 스크롤링해서 예제10번 결과처럼 전부 스크롤링 되게 하시오!
#%%예제13. 예제12번 코드를 예제 10번 코드에 적용해서 레이디 버그 전체 게시판의 글들이 날짜와 함께 출력되게 하시오.
# 예제10번 코드까지를 가져온다.

from bs4 import BeautifulSoup
import urllib.request  # 웹상의 url 을 파이썬이 인식 할 수 있도록 해주는 모듈

for page in range(1,23):
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(page)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    url = urllib.request.Request(list_url) # 사람이 알아 볼수 있는 위의 url 을 
                                           # 파이썬이 알아 볼수 있도록 변환, 첫번째 작업 
    
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    result2 = soup.find_all( 'p', class_ = 'con') # 게시글 본문
    result3 = soup.find_all( 'span', class_ = 'date') #게시글 날짜
    
    params1 = []
    for i in result2:
        params1.append(i.get_text(" ",strip=True))
    params2 = []
    for i in result3:
        params2.append(i.get_text(" ",strip=True))
    for i,j in zip(params1,params2):
        print(j+'    '+i) # 날짜와 본문 같이 출력
    
# 설명 : 위의 params1과 params2가 for 문 안쪾에 있기 때문에
 # 페이지 번호가 돌떄마다 params 리스트 안의 내용이 새로운 날짜와 내용으로 변경되게 됩니다. # 

#%% 예제14. params1과 params2 에 레이디 버그 시청자 게시판의 모든 게시날짜와 본문
#  내용이 들어가게 코드를 수정하시오!
from bs4 import BeautifulSoup
import urllib.request  # 0. 웹스크롤링에 필요한 모듈을 임폴트 합니다.

params1 = [] #1. 레이디 버그 게시판 게시날짜와 게시글 전체를 다 담은 리스트 2개를 만듭니다.
params2 = []
params_1n2 = []
for page in range(1,23):#2. 전체 페이지를 돌리기 위해서 1번부터 22번까지 돌리자.
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(page)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    url = urllib.request.Request(list_url) #3. 웹에서 html 문서를 가지고 와서 파싱
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    result2 = soup.find_all( 'p', class_ = 'con') # 게시글 본문
    result3 = soup.find_all( 'span', class_ = 'date') #게시글 날짜
    
    for i in result2:
        params1.append(i.get_text(" ",strip=True))
    for i in result3:
        params2.append(i.get_text(" ",strip=True))
for i,j in zip(params1,params2):
    params_1n2.append(j+'    '+i) # 날짜와 본문 같이 출력

print(params_1n2)    
# 예제 13번 코드의 변수와 indentation 위치를 바꾸어서 설정해준다.

#%% 정리 
#%%문제415. (점심시간문제) 레이디 버그 게시판의 전체 게시글은 총 몇건인가?
from bs4 import BeautifulSoup
import urllib.request

cnt= 0
for page in range(1,23):
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(page)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    result3 = soup.find_all( 'span', class_ = 'date') 
    for i in result3:
        cnt+=1
print(cnt)

#%%문제416. 게시글 429건 전체를 c 드라이브 밑에 mytext.txt 라는 이름으로 저장하시오.

from bs4 import BeautifulSoup
import urllib.request  # 0. 웹스크롤링에 필요한 모듈을 임폴트 합니다.

params1 = [] #1. 레이디 버그 게시판 게시날짜와 게시글 전체를 다 담은 리스트 2개를 만듭니다.
params2 = []
params_1n2 = []
for page in range(1,23):#2. 전체 페이지를 돌리기 위해서 1번부터 22번까지 돌리자.
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(page)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    url = urllib.request.Request(list_url) #3. 웹에서 html 문서를 가지고 와서 파싱
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    result2 = soup.find_all( 'p', class_ = 'con') # 게시글 본문
    result3 = soup.find_all( 'span', class_ = 'date') #게시글 날짜
    
    for i in result2:
        params1.append(i.get_text(" ",strip=True))
    for k in result3:
        params2.append(k.get_text(" ",strip=True))
for i,j in zip(params1,params2):
    params_1n2.append(j+'    '+i) # 날짜와 본문 같이 출력

print(params_1n2)  

f = open("c:\\data\\mytext35.txt",'w',encoding='UTF8')
for t in params_1n2:
    f.write(str(t))
f.close()

#%% 위의 방법과 비교해보기! 결과물을 이쁘게 나오게 하는 여러가지 방법(아래는 선생님방법)
from bs4 import BeautifulSoup
import urllib.request  # 0. 웹스크롤링에 필요한 모듈을 임폴트 합니다.

f = open("c:\\data\\mytext34.txt",'w',encoding='UTF8')
params1 = [] #1. 레이디 버그 게시판 게시날짜와 게시글 전체를 다 담은 리스트 2개를 만듭니다.
params2 = []
params_1n2 = []
for page in range(1,23):#2. 전체 페이지를 돌리기 위해서 1번부터 22번까지 돌리자.
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(page)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    
    url = urllib.request.Request(list_url) #3. 웹에서 html 문서를 가지고 와서 파싱
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    result2 = soup.find_all( 'p', class_ = 'con') # 게시글 본문
    result3 = soup.find_all( 'span', class_ = 'date') #게시글 날짜
    
    for i in result2:
        params1.append(i.get_text(" ",strip=True))
    for k in result3:
        params2.append(k.get_text(" ",strip=True))

for i,j in zip(params1,params2):
    f.write(j+'    '+i+'\n') # 날짜와 본문 같이 출력
f.close()
    
#%% 중앙일보사

# 예제1. 중앙일보사 홈페이지에서 인공지능으로 검색했을 때 나오는 url을 가져오시오!
# https://news.joins.com/Search/TotalNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews
# https://news.joins.com/Search/TotalNews?page=2&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews
# https://news.joins.com/Search/TotalNews?page=10&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews
# https://news.joins.com/Search/TotalNews?page=21&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews

#예제2. 위의 사이트에서 보이는 상세기사를 클릭해보시오!

# https://news.joins.com/article/23947044
# https://news.joins.com/article/23946979
# https://news.joins.com/article/23946876
# https://news.joins.com/article/23946841
# 규칙성이 딱히 없다.

#예제3. 인공지능으로 검색했을 때 나오는 상세기사들의 url 을 스크롤링 하시오 !
#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다.
from bs4 import BeautifulSoup
import urllib.request 

#2. 중앙일보에서 인공지능으로 검색했을때 나오는 첫페이지 html 코드를 
# Beautiful Soup 에서 이용할 수 있도록 파싱합니다.
list_url = "https://news.joins.com/Search/TotalNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews"
url = urllib.request.Request(list_url) #3. 웹에서 html 문서를 가지고 와서 파싱
result = urllib.request.urlopen(url).read().decode("UTF-8")
soup = BeautifulSoup(result,"html.parser")

#3. 상세기사 url 을 가져올 수 있도록 테그와 클래스를 찾습니다.
# 찾아보니 테그는 h2 이고 클래스 이름은 headline mg 입니다.
result1 = soup.find_all( 'h2', class_ = 'headline mg')
# print(result1)

#4. 위의 result1은 리스트 이므로 for loop 문을 이용해서 리스트에 있는 요소를 하나씩 빼냅니다.
for i in result1:
    print(i)
#%% 상세 url만 가져 오고 싶은데 형식이 href= 만 가져오고 싶다.
for i in result1:
    for k in i: # h2 테그 안의 a 테그의 html 코드를 가져오기 위한 코드
        print(k)

#%% 하나씩 태그를 제끼려면 포문을 돌려라~
print(result1)
for i in result1:
    print(type(i),i)
    for k in i: # h2 테그 안의 a 테그의 html 코드를 가져오기 위한 코드
        print(k)
        for j in k:
            print(j)
            
#설명: <h2 class="headline mg">
# <a href="https://news.joins.com/article/23947044" target="_blank">'AI 발전에 써라' 동원 김재철 명예회장, KAIST에 500억 기부
# </a>
# </h2> # h2 와 a 테그로 감싸져 있다. 
# 안쪽 코드의 안쪽을 가져 오는 게 2중 포문의 역활이다. 
#%% 5. href 부분만 가져오자.
for i in result1:
    for k in i: # h2 테그 안의 a 테그의 html 코드를 가져오기 위한 코드
        print(k.get('href'))

# https://news.joins.com/article/23947044
# https://news.joins.com/article/23946979
# https://news.joins.com/article/23946876
# https://news.joins.com/article/23946867
# https://news.joins.com/article/23946841
# https://news.joins.com/article/23946757
# https://news.joins.com/article/23946642
# https://news.joins.com/article/23946268
# https://news.joins.com/article/23946216
# https://news.joins.com/article/23946191

#%%  예제4. 위의 상세 기사 url 을 params 라는 비어 있는 리스트에 다 append 시키시오.
from bs4 import BeautifulSoup
import urllib.request 

#2. 중앙일보에서 인공지능으로 검색했을때 나오는 첫페이지 html 코드를 
# Beautiful Soup 에서 이용할 수 있도록 파싱합니다.
list_url = "https://news.joins.com/Search/TotalNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews"
url = urllib.request.Request(list_url) #3. 웹에서 html 문서를 가지고 와서 파싱
result = urllib.request.urlopen(url).read().decode("UTF-8")
soup = BeautifulSoup(result,"html.parser")

#3. 상세기사 url 을 가져올 수 있도록 테그와 클래스를 찾습니다.
# 찾아보니 테그는 h2 이고 클래스 이름은 headline mg 입니다.
result1 = soup.find_all( 'h2', class_ = 'headline mg')
params =[]
for i in result1:
    for k in i: # h2 테그 안의 a 테그의 html 코드를 가져오기 위한 코드
        params.append(k.get('href'))

print(params)
#%%
# 예제5. 상세기사 url 중에 하나를 복사해 오고 그 상세 기사 url의 페이지로 접속해서
# 본문 기사의 테그 이름과 클래스 이름이 무엇인지 확인하시오!

 <div id="article_body" itemprop="articleBody" class="article_body mg fs4">

# 테그 이름은 div 테그 이고 클래스 이름은 "article_body mg fs4
#%%예제6. 위의 상세기사의 본문 텍스트를 스크롤링 해서 

from bs4 import BeautifulSoup
import urllib.request 

list_url = "https://news.joins.com/Search/TotalNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews"
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("UTF-8")
soup = BeautifulSoup(result,"html.parser")


result1 = soup.find_all( 'h2', class_ = 'headline mg')
params =[]
for i in result1:
    for k in i: 
        params.append(k.get('href'))

list_url2 = params[0] # 상세기사 url 중 첫번째꺼
print(list_url2)
url_article=urllib.request.Request(list_url2) 
result_article=urllib.request.urlopen(url_article).read().decode("UTF-8")
soup_article = BeautifulSoup(result_article,"html.parser")

result1_article= soup_article.find_all('div', class_='article_body mg fs4')
params_article = []
for i in result1_article:
    params_article.append(i.get_text(" ",strip=True))
print(params_article)

#%%예제7. 상세기사 url 을 가져와서 params 리스트에 넣고 출력하는 예제4번 코드를 함수로 생성하시오!
from bs4 import BeautifulSoup
import urllib.request 

def j_scroll():
    
    list_url = 'https://news.joins.com/Search/TotalNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    
    result1 = soup.find_all( 'h2', class_ = 'headline mg')
    params =[]
    for i in result1:
        for k in i: 
            params.append(k.get('href'))
    return params

print(j_scroll())

#%%

from bs4 import BeautifulSoup
import urllib.request 

def j_scroll(word):
    word = input('검색어를 입력하세요')
    list_url = 'https://news.joins.com/Search/TotalNews?page=1&Keyword='+word+'&SortType=New&SearchCategoryType=TotalNews'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    
    result1 = soup.find_all( 'h2', class_ = 'headline mg')
    params =[]
    for i in result1:
        for k in i: 
            params.append(k.get('href'))
    return params

print(j_scroll('인공지능'))
#%%예제8. 상세기사 url 을 이용해서 기사를 가져오는 함수를 가져 오시오.
def j_detail_scroll():
    list_url2 = 'https://news.joins.com/article/23947044' # 상세기사 url 중 첫번째꺼
    url_article=urllib.request.Request(list_url2) 
    result_article=urllib.request.urlopen(url_article).read().decode("UTF-8")
    soup_article = BeautifulSoup(result_article,"html.parser")
    
    result1_article= soup_article.find_all('div', class_='article_body mg fs4')
    params_article = []
    for i in result1_article:
        params_article.append(i.get_text(" ",strip=True))
    return params_article

print(params_article)

#%%예제9. 지금 만든 j_detail_scroll() 함수는 상세기사 딱 한개의 본문을 출력하는 함수인데 이 
# j_detail_scroll()함수에 j_scroll() 함수를 실행했을때 나오는 상세 url 여러개를 제공할 수 있도록 코드를 수정하시오!

from bs4 import BeautifulSoup
import urllib.request 

def j_scroll():
    
    list_url = 'https://news.joins.com/Search/TotalNews?page=1&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    
    result1 = soup.find_all( 'h2', class_ = 'headline mg')
    params =[]
    for i in result1:
        for k in i: 
            params.append(k.get('href'))
    return params

def j_detail_scroll():
    params = j_scroll()
    params_article = []
    for i in params:
        url_article=urllib.request.Request(i) 
        result_article=urllib.request.urlopen(url_article).read().decode("UTF-8")
        soup_article = BeautifulSoup(result_article,"html.parser")
        result1_article= soup_article.find_all('div', class_='article_body mg fs4')
        for j in result1_article:
            params_article.append(j.get_text(" ",strip=True))
    return params_article

print(j_detail_scroll())

#%% 중앙일보의 가시를 스크롤링하는 내용 총정리

# 1. 검색 키워드(예:인공지능) 을 가지고 검색을 한후 그 url을 얻어낸다.
# 2. 상세기사 url 을 리스트에 담는 j_scroll() 함수를 생성한다.
# 3. 상세기사 url 로 기사본문을 스크롤링하는 j_detail_scroll() 함수를 생성한다.
# 4.  j_detail_scroll() 함수 안에서 j_scroll() 함수를 호출해서 상세기사 url 여러개를
# 받아오겠금 코딩하고 받아온 상세기사 url 로 본문 기사들을 params2 에 담겠금 코드를 수정한다.


#%%문제417. 동아일보에서 검색 키워드(예: 인공지능) 을 가지고 검색을 한후  url을 찾아보시오!

https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1
https://www.donga.com/news/search?p=16&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1
https://www.donga.com/news/search?p=31&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1


#%%문제418. 상세기사 url을 리스트를 담는 d_scroll() 함수를 생성하세요~

from bs4 import BeautifulSoup
import urllib.request 

def d_scroll():
    
    list_url = 'https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    
    result1 = soup.find_all( 'p', class_ = 'txt') # tit 는 이미지 
    params =[]
    for i in result1:
        for k in i: 
            params.append(k.get('href'))
    return params

print(d_scroll())

#%%문제419. 상세기사 url로 기사본문을 스크롤링하는 d_detail_scroll() 함수를 생성해라~

def d_detail_scroll():
    params = d_scroll()
    params_article = []
    for i in params:
        url_article=urllib.request.Request(i) 
        result_article=urllib.request.urlopen(url_article).read().decode("UTF-8")
        soup_article = BeautifulSoup(result_article,"html.parser")
        result1_article= soup_article.find_all('div', class_='article_txt')
        for j in result1_article:
            params_article.append(j.get_text(" ",strip=True))
    return params_article

print(d_detail_scroll())

#%%문제420. 한겨례 신문사에서 인공지능으로 검색했을때 나오는 기사 본문을 스크롤링하는
# 함수 두개를 생성하시오!
# 1. h_scroll() :  상세기사 url 을 가져오는 함수
# 2. h_detail_scroll() : 상세기사 url 로 기사본문을 가져오는 함수.

from bs4 import BeautifulSoup
import urllib.request 

def h_scroll():
    
    list_url = 'http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&sort=d&period=all&datefrom=1988.01.01&dateto=2020.12.16&media=news'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("UTF-8")
    soup = BeautifulSoup(result,"html.parser")
    
    result1 = soup.find_all( 'dt')
    params =[]
    for i in result1:
        for k in i: 
            params.append('http:'+ k.get('href'))
    return params

print(h_scroll())

def h_detail_scroll():
    params = h_scroll()
    params_article = []
    for i in params:
        url_article=urllib.request.Request(i) 
        result_article=urllib.request.urlopen(url_article).read().decode("UTF-8")
        soup_article = BeautifulSoup(result_article,"html.parser")
        result1_article= soup_article.find_all('div', class_='text')
        for j in result1_article:
            params_article.append(j.get_text(" ",strip=True))
    return params_article

print(h_detail_scroll())

#%%문제421. 오늘의 마지막 문제 전자신문사에서 여러분들이 스크롤링하고
#싶은 키워드를 넣고 검색했을때 나오는 본문기사들을 수집하는 
#함수 2개를 생성하시오~ (밑에 페이지 번호 1,2,3 만 스크롤링하세요)

# e_scroll()
# e_detail_scroll()