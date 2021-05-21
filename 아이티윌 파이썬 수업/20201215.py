# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:51:57 2020

@author: bigne
"""

#%% map(a,b)

def gob(x):
    return x*x

a =[1,2,3,4,5]
result = map(gob,a) # map(함수명, 리스트명)
print(list(result))

# 설명: map 함수가 리턴해주는 결과를 보려면 반드시 
# list 함수로 리턴된 값을 변환해서 리스트형태로 봐야합니다.

# 설명: 리스트의 요소 하나하나를 함수에 입력값으로 입력한다(mapping)

#%%문제391. 숫자를 입력해서 해당 숫자가 3000보다 크면 1을 리턴하게 하고
# 입력하는 숫자가 3000보다 작다면 0을 리턴하는 함수를 생성하시오.

def high_income(num):
    if num > 3000:
        return 1
    else:
        return 0
    
print( high_income(3500))

print( high_income(2000))

#문제392. 위에서 만든 함수를 map 함수에 적용해서 아래의 리스트의 요소를
# high_income 함수의 입력 매개변수로 입력해서 아래의 결과가 출력되게 하시오!

a = [4000, 5000, 2000, 3500, 1000]

# 결과: [1,1,0,1,0]

result = map(high_income, a)
print(list(result))

#%%문제393. 동전을 지정된 숫자만큼 던져서 앞면이 나오는지 뒷면이 나오는지 출력하는 함수를 생성하시오!

num = int(input('코인을 던질 횟수를 정해주세요.'))
import random as r
def coin_cnt(a):
    for i in range(a):
        print(r.choice(['앞','뒤']))
        
coin_cnt(num)
        
#%%문제394. 위의 함수를 수정해서 숫자를 입력하면 해당 숫자만큼 동전을 던져서
# 동전이 앞면이 나오는 확률을 출력하시오!

num = int(input('코인을 던질 횟수를 정해주세요.'))
import random as r
def coin_cnt(a):
    cnt = 0
    cnts = 0
    for i in range(a):
        cnts += 1
        result = r.choice(['앞','뒤'])
        if result == '앞':
            cnt += 1
    return print(cnt/cnts)
        
coin_cnt(num)
        
#%%문제395. 위에서 만든 coin_cnt 함수에 아래의 a 리스트의 요소들을 적용해서 
# 결과로 확률이 출력되게하시오.


# 결과: [0.5, 0.53, 0.497, 0.5041, 0.5028]      
        

import random as r
def coin_cnt(a):
    cnt = 0
    cnts = 0
    for i in range(a):
        cnts += 1
        result = r.choice(['앞','뒤'])
        if result == '앞':
            cnt += 1
    return cnt/cnts

a = [10,100,1000,10000,100000] 

a_result = map( coin_cnt,a)

print(list(a_result))        

#%%396. 주사위를 던져서 주사위의 눈이 5가 나올 확률을 출력하는 함수를 만들고
# 아래의 a 리스트의 주사위를 던지는 횟수를 map 함수로 적용해서 확률이 점점 1/6로
# 근사해지는지 실험하시오!

a = [10, 100, 1000, 10000, 100000]
import random as r
def dice_cnt(a):
    cnt = 0
    cnts = 0
    for i in range(a):
        cnts += 1
        result = r.choice([a for a in range(1,7)])
        if result == 5:
            cnt += 1
    return cnt/cnts

result = map( dice_cnt,a) 
print (list(result))     
        
#%%397. 아래의 불량품이 들어 있는 박스에서 제품을 3개를 뽑았을때 
       # 3개중에 2개가 불량품일 확률을 출력하는 삼수를 만드시오 ~(복원)
box = ['정상','정상','불량품','정상','불량품','정상','정상','불량품']
import numpy as np
def box_cnt(a):
    cnt = 0
    cnts = 0
    for i in range(a):
        cnts += 1
        result = list(np.random.choice(box,3))
        if result.count('불량품') == 2:
            cnt += 1
    return cnt/cnts
print( box_cnt(100))

#문제398. 위에서 만든 box_cnt 함수에 아래의 a 리스트의 횟수를 map 함수로 적용해서 
# 확률이 출력되게 하시오!

a = [10,100,1000,10000,100000] 
result = map(box_cnt,a)
print (list(result))       

#%%
f = open('c:\\data\\jobs.txt', encoding='UTF8')
data = f.read()
print( data )
f.close()

#설명: 스티븐 잡스 연설문은 길지 않으니까 한번에 읽어와도 관계 없는데 텍스트 
# 파일의 용량이 매우 클 경우 read()로 한꺼번에 파일의 내용을 읽어 들이는것은
# 메모리 문제를 야기 시킬수 있습니다.

#웹에서 스크롤링한 데이터를 분석하고자 할때 위와 같이 open 함수를 이용해서 파이썬으로 데이터를 불러옵니다.

#%%문제399.중앙일보에서 인공지능으로 검색한 기사인 mydata3.txt를 파이썬으로 불러서 출력하시오!

f = open('c:\\data\\mydata3.txt', encoding='UTF8')
data = f.read()
print( data )
f.close() # 파일을 닫느다. 닫는 코드를 안쓰면 스파이더를 실행하고 있으면
        # 계속 파일이 열려있게 됩니다. 파일을 계속 열면 메모리를 계속 차지하고 
        # 사용하고 있게 됩니다.
        # 텍스트 파일의 크기가 크면 메모리를 많이 사용하고 있게 됩니다.
        # 그래서 사용이 끝났으면 반드시 close()로 닫습니다.
        
#%%400. 위의 중앙일보 기사에서 빅데이터 라는 단어가 몇번 나오는지 count 하시오!

f = open('c:\\data\\mydata3.txt', encoding='UTF8')
data = f.read()
print( data.count('빅데이') )
print( data.count('인공지능'))
f.close()


#%% 
f = open("c:\\data\\jobs.txt", encoding='UTF8')
data = f.readline()
print(data) # steve jobs'2005 stanford commencement address
f.close()

#%%문제401. 위의 스티븐 잡스 연설문 데이터를 모두 읽어 오시오!
    # (readline() 함수를 이용하세요~)
    
f = open("c:\\data\\jobs.txt", encoding='UTF8')
data = f.readline()
while data:
    print(data)
    data = f.readline()
f.close()

# 설명: 맨 위에 data = f.readline() 코드는 처음에 딱 한번만 실행되고
#       그 다음에는 실행되지 않습니다. 그 다음부터는 while  문 안에 있는
#       data = f.readline() 가 작동되어서 반복적으로 스티븐 잡스의 연설문을
#       한줄씩 읽어서 data 변수에 넣습니다.

#%%
f = open("c:\\data\\jobs.txt", encoding='UTF8')
data = f.readline()
n=1
for i in f:
    print(i,n)
    n+=1
    # data= f.readline()
#%%문제402.인공지능이 몇번씩 들어 있는지 카운트 하시오.
f = open("c:\\data\\mydata3.txt", encoding='UTF8')
data = f.readline()
while data:
    print(data.count('인공지능'))
    data = f.readline()
f.close()
#%%문제403. 위의 count 한 건수를 다 누적시켜서 출력하시오!
f = open("c:\\data\\mydata3.txt", encoding='UTF8')
data = f.readline()
cnt=0
while data:
    cnt += data.count('인공지능')
    data = f.readline()
f.close()

print(cnt)

#%%문제404. 위의 코드를 수정해서 단어를 물어보게하고 단어를 입력하면 해당 단어가
# 몇건 나오는지 출력되게 하시오!
a = input('단어를 입력하세요~')

f = open("c:\\data\\mydata3.txt", encoding='UTF8')
data = f.readline()
cnt=0
while data:
    cnt += data.count(a)
    data = f.readline()
f.close()

print('이기사에서',a,'는',cnt,'번 나왔습니다.')
#%% open 함수

# r	읽기모드 - 파일을 읽기만 할 때 사용
# w	쓰기모드 - 파일에 내용을 쓸 때 사용
# a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
#%%실습해 보자 winter 에 elsa 와 anna 의 갯수를 구하는 여러가지 방식!
#%% scrip를 가져오는 방식1
f = open("c:\\data\\winter.txt")
for i in f:
    print(i)
#%% 방식2 read()
f = open("c:\\data\\winter.txt")
data = f.read()
print(data)
#%% 방식3 readline() 한줄을 읽고 다음 줄로 시작점을 만든다.
f = open("c:\\data\\winter.txt")
while 1:
    data = f.readline()
    print(data)
    if not data:
        break
#%% 방식4 readlines() 한줄씩 읽어서 메모리에 넣는다.
f = open("c:\\data\\winter.txt")
data = f.readlines()
for i in data:
    print(i)
#%%#%% lower로 바꿔보자.를 가져오는 방식1
f = open("c:\\data\\winter.txt")
for i in f:
    print(i.lower())
#%% 방식2 read()
f = open("c:\\data\\winter.txt")
data = f.read()
print(data.lower())
#%% 방식3 readline() 한줄을 읽고 다음 줄로 시작점을 만든다.
f = open("c:\\data\\winter.txt")
while 1:
    data = f.readline()
    print(data.lower())
    if not data:
        break
#%% 방식4 readlines() 한줄씩 읽어서 메모리에 넣는다.
f = open("c:\\data\\winter.txt")
data = f.readlines()
for i in data:
    print(i.lower())
#%% elsa 를 찾아 보자.
f = open("c:\\data\\winter.txt")
data = f.read().split()
cnt = 0
for i in data:
    if 'elsa' in i.lower():
        cnt += 1
print(cnt)

#%% 방식4 readlines() 와 count 방식
f = open("c:\\data\\winter.txt")
data = f.readlines()
cnt = 0
for i in data:
    cnt += i.lower().count('elsa')

print(cnt)
#%%
#%%

a = '인공지능'

f = open("c:\\data\\mydata3.txt", encoding='UTF8')
data = f.readline()
cnt=0
while data:
    cnt += data.count(a)
    if data.count(a)>0:
        print(data, cnt)
    data = f.readline()
f.close()

# print('이기사에서',a,'는',cnt,'번 나왔습니다.')

#%% write

text = input('파일에 저장할 내용을 입력하세요~')
f = open('c:\\data\\mydata.txt','w')

f.write(text)
f.close()

# 설명: 위에 w 는 write 의 약자입니다. c 드라이브 밑에 data 밑에 mydata.txt
# 파일로 쓰겠다는 뜻입니다.

# 설명: 위의 코드는 웹에서 스크롤링한 데이터를 파일로 저장할 때 응용되게 됩니다.

#%%(점심시간 문제) 문제405. 아래의 파란색 공과 빨간색 공이 들어 있는 박스에서 
# 5개의 공을 뽑았을때 그중 2개가 파란색 공일 확률을 출력하는 함수를 만들고 
# 공을 뽑는 횟수를 10,100,1000,10000,10000 했을때 의 확률을 map 함수를 이용해서 출력하시오!

a = [10,100,1000,10000,10000]

box = ['red']*26+['blue']*24

import numpy as np

def box_cnt(a):
    cnt = 0
    cnts = 0
    for i in range(a):
        cnts += 1
        result = list(np.random.choice(box,5))
        if result.count('blue') == 2:
            cnt += 1
    return cnt/cnts

print( list(map(box_cnt,a)))

#%%writelines
listdata = [ 2, 2, 1, 3, 8, 5, 7 ]
result = sorted( listdata )  # 리스트의 요소를 정렬한다. 
print (result) # [ 1, 2, 2, 3, 5, 7, 8 ]
f = open("c:\\data\\mydata22.txt", "w") # mydata2.txt 를 생성하겠다.
f.write( str(result) )  # result 에 있는 내용을 mydata2.txt 로 생성한다. 
f.close()                 # result 에 있는 내용을 문자로 변환해야 한다. 

#%%문제406. 아래의 리스트를 mydata9.txt 로 저장하시오 !

listdata2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
result = sorted( listdata2 )  
print (result) # [ 1, 2, 2, 3, 5, 7, 8 ]
f = open("c:\\data\\mydata9.txt", "w") 
f.write( str(result) ) 
f.close()     
#%%

data = [] # data 라는 비어 있는 리스트 생성
while True: # 무한루프를 수행합니다.
    text = input('저장할 내용을 입력하세요')
    if text =='': # text에 아무것도 입력하지 않으면
        break
    data.append(text + '\n')
    
f = open('c:\\data\\mydata99.txt','a') # mydata99.txt를 생성하겠다.
#  'a' 는 추가하기, 'w' 는 덮어쓰기.
f.writelines(data)
f.close()

#%%

f = open('c:\\data\\mydata99.txt') # mydata99.txt를 생성하겠다.
data=f.read()
print(data)
f.close()

#%% read, write

f = open("c:\\data\\mydata.txt",'r')
h = open("c:\\data\\mydata77.txt",'w')
data =f.read()
h.write(data)
f.close()
h.close()

#%% 바이너리 read,write

bufsize = 1024
f = open('c:\\data\\lena.png','rb') # rb 는 read binary 의 약자입니다.
h = open('c:\\data\\lena_copy.png','wb') # wb 는 write binary 의 약자
data = f.read(bufsize) # 이미지를 1kb을 읽어서 data 에 저장합니다.
while data: # data에 data가 발견되는 동안에 루프문을 수행합니다.
    h.write(data) # lena_copy.png 에 1kb의 데이터씩 write 합니다.
    data = f.read(bufsize) # lena.png 에서 1kb 의 데이터를 read 합니다.

f.close()
h.close()

# 설명: lena.png 의 총크기가 334kb 이므로 1kb 씩 읽어 들여서 쓰는 작업을 총 334번 수행합니다.


#%% with ~ as
# 1. with ~ as 를 사용하지 않았을때
f = open('c:\\data\\mydata.txt','r')
data = f.readlines()
print(data)
f.close()

# 2. with ~ as 절을 사용했을
with open('c:\\data\\mydata.txt','r') as f:
    data = f.readlines()
    print(data)
    
# 설명 : with ~ as 절을 사용하면 자동으로 파일 close를 해줍니다.~

#%% HTML

# 예제1. 아주 간단한 html 문서를 만들어 봅니다.

# 메모장을 열고 아래와 같이 코딩을 하세요~

<html><head><title> 양건준님의 오늘 일정</title></head>
<body>
<p class="title"> 양건준님은 오늘 점심시간에 우육탕을 먹었습니다.</p>
</body>
</html>

# 메모장의 파일이름을 a.html 로 바탕화면에 저장하세요~
#  저장할 때 모든 파일 로 저장하세요~

# 예제2. 위의 글씨를 진하게 해보시요.

<html><head><title> 양건준님의 오늘 일정</title></head>
<body>
<p class="title"> <b> 양건준님은 오늘 점심시간에 우육탕을 먹었습니다.</b> </p>
</body>
</html>

# 글씨를 진하게 하려면 b 테그를 사용합니다.

# 예제3. 위의 글씨에 밑줄을 그어 보시오.

<html><head><title> 양건준님의 오늘 일정</title></head>
<body>
<p class="title"> <b> <u> 양건준님은 오늘 점심시간에 우육탕을 먹었습니다.</u></b> </p>
</body>
</html>

# 밑줄은 <u> </u>  테그 u를 사용합니다. 

# 예제4. 위의 글씨를 이텔릭체로 변경하시오 !

<html><head><title> 양건준님의 오늘 일정</title></head>
<body>
<p class="title"> <b> <u> <i> 양건준님은 오늘 점심시간에 우육탕을 먹었습니다.</i></u></b> </p>
</body>
</html>

# 설명: 글씨를 이텔릭체로 변경하려면 테그 i 를 이용합니다.

# 예제5. p 테그를 추가해서 제목과 내용을 나누시오!

<html><head><title> 양건준님의 오늘 일정</title></head>
<body>
<p class="title"> <b> <u> <i> 양건준님의 오늘 점심 </i></u></b> </p>
<p class="content"> 양건준님은 오늘 점심에 지하식당으로 내려가서 반 친구들과같이
                    우육탕을 먹었습니다. 코로나에 대한 걱정도 있었지만 용기내서
                    먹었습니다. </p>
</body>
</html>

# 설명: 제목은 class title 에 적고 내용은 class content에 적습니다.

# 예제6. 위에서 만든 html 문서의 본문에 링크를 거시오 !

<html><head><title> 양건준님의 오늘 일정</title></head>
<body>
<p class="title"> <b> <u> <i> 양건준님의 오늘 점심 </i></u></b> </p>
<p class="content"> 양건준님은 오늘 점심에 지하식당으로 내려가서 반 친구들과같이
                    우육탕을 먹었습니다. 코로나에 대한 걱정도 있었지만 용기내서
                    먹었습니다. 
<a href="http://cafe.daum.net/oracleorcle" class="cafe1" id="link1"> 바로가기 </a>

</body>
</html>
# 설명: 워드 문서를 만들때도 그 문서내에 단원도 있고 세부 목차도 있듯이
#  class 에 그 html 문서의 특정 단원이라고 보면 되고 id 는 링크를 줄때 부여하는
#  제목인데 id 는 값이 unique 합니다.





#문제407. 다음과 같이 내용과 링크를 수정하시오~ 바로가기를 생성해보세요.

<html><head><title> 양건준님의 오늘 일정</title></head>
<body>
<p class="title"> <b> <u> <i> 양건준님의 오늘 점심 </i></u></b> </p>
<p class="content"> 양건준님은 오늘 점심에 지하식당으로 내려가서 반 친구들과같이
                    우육탕을 먹었습니다. 코로나에 대한 걱정도 있었지만 용기내서
                    먹었습니다. 우육탕집 식당 홈페이지는 바로 가기를 누르세요.
<a href="http://naver.com" class="cafe1" id="link1"> 바로가기 </a>
                    
</body>
</html>
#%%beautiful soup

# 예제1. ecologicalpyramid.html 코드를 beautiful soup 모듈에서 사용할수 있도록 파싱을 하고
# 파싱된 내용을 출력하시오 !

from bs4 import BeautifulSoup as bs

f = open("c:\\data\\ecologicalpyramid.html")
soup = BeautifulSoup(f, "html.parser")
print(soup)
#%%
#예제2. ecologicalpyramid.html 코드에서 class 이름 name 에 접근해서 데이터를 긁어 오시오!

f = open("c:\\data\\ecologicalpyramid.html")
soup = bs(f, "html.parser")
result = soup.find_all(class_="name")
print(result)

#%%
#예제3. 위에서 긁어온 데이터에서 html 코드 말고 text만 출력하시오!

f = open("c:\\data\\ecologicalpyramid.html")
soup = bs(f, "html.parser")
result = soup.find_all(class_="name")

for i in result: # result 리스트 안의 요소를 하나씩 가져옵니다.
    print(i.get_text())
    
#설명: get_text() 함수를 사용하면 html 코드 말고 텍스트만 가져옵니다.

#%%문제408. ecologicalpyramid.html 문서에서 number 클래스에 있는 숫자들만 긁어와서 출력하시오!
f = open("c:\\data\\ecologicalpyramid.html")
soup = bs(f, "html.parser")
result = soup.find_all(class_="number")

for i in result: 
    print(i.get_text())

#%%문제409. 위에서 긁어온 숫자들을 a 라는 비어있는 리스트에 저장한후 a 안의 요소들을 정렬하고 a 리스트를 출력하시오.
from bs4 import BeautifulSoup as bs
f = open("c:\\data\\ecologicalpyramid.html")
soup = bs(f, "html.parser")
result = soup.find_all(class_="number")
a=[]
for i in result: # result 리스트 안의 요소를 하나씩 가져옵니다.
    a.append(int(i.get_text()))

# a.sort()
# print(a)
print(sorted(a))

#%%문제410. 중앙일보사 홈페이지로 가서 신문기사 하나를 보시오.
ctl+s 로 기사의 html 문서를 aa77.html로 저장합니다.
#%%문제411. aa77.html을 BeautifulSoup 모듈의 함수를 쓸 수 있도록 파싱하고
#  파싱된 결과를 출력하시오.
from bs4 import BeautifulSoup as bs
f = open("c:\\data\\aa.77.html", encoding="UTF8")
soup = bs(f, "html.parser")
print(soup)

#%%문제412. 위의 기사의 본문을 가져오기 위해서 기사 본문의 class 이름이 무엇인지 확인하세요~
# 개발자 모드인 F12를 누르면 html 코드 창이 나오면서 개발자 모드 화면이 열립니다.
#그러면 위쪽에 화살표를 클릭하고 기사본문을 클릭하면 html 문서에 class 이름을 확인 할수 있는
# html 문서쪽으로 바로 이동합니다.

<h1 class="headline mg" id="article_title"> 증인 빠진 심재철, 尹의견서는 냈다···尹측 "위증죄 회피 꼼수"</h1>


#%%문제413. 클래스 이름 article_body mg fs4 로 접근하여 text 를 긁어 오시오
f = open("c:\\data\\aa.77.html", encoding="UTF8")
soup = bs(f,"html.parser")
result = soup.find_all(class_='article_body mg fs4')
for i in result:
    print(type(i.get_text()))
    
# get_text : <> 따위는 테그를 삭제하고 본문만 긁어 오는 예약어.

#%%문제414. (오늘의 마지막 문제) 위에서 스크롤링한 중앙일보 기사를 c 드라이브 밑에 mytext23.txt 로 저장하시오!
# (반드시 저장해서 기사를 워드 클라우드로 시각화를 할 수 있으니까 오늘 배운 내용을 저장하세요~)
#%
from bs4 import BeautifulSoup as bs
f = open("c:\\data\\aa.77.html", encoding="UTF8")
soup = bs(f,"html.parser")
result = soup.find_all(class_='article_body mg fs4')
a=[]
for i in result:
    a.append(i.get_text())

h = open("c:\\data\\mytext23.txt",'w',encoding='UTF8')
h.write(str(a))
h.close()

#%%
f = open("c:\\data\\aa.77.html", encoding="ANSI")
soup = bs(f,"html.parser")
result = soup.find_all(class_='article_body mg fs4')
h = open("c:\\data\\mytext23.txt",'w')

h.write(i.get_text())
print(h)   

# h.write(data)
# h.close()

# f = open("c:\\data\\mydata.txt",'r')
# h = open("c:\\data\\mydata77.txt",'w')
# data =f.read()
# h.write(data)
# f.close()
# h.close()
