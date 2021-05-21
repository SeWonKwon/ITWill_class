# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:27:28 2020

@author: bigne
"""

#%% find

txt = 'A lot of things occur each day'
word_count1 = txt.find('o')
print( word_count1) #3이 출력되는데 'o' 라는 철자가 위치하는 인덱스 번호를 리턴합니다.

word_count2 = txt.find('day')
print (word_)count2

#%%문제284. 우리반 데이터(emp122.csv)를 파이썬으로 로등해서 이메일만 출력하시오!

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list)
    
#%%문제285. 위에서 출력한 이메일에서 @의 위치 인덱스 번호를 출력하시오!

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6].find('@'))

#%%문제286. 그러면 이번에는 이메일에서 . 의 위치도 같이 출력하시오!import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6].find('.'))

#%%문제287. 이번에는 이메일을 출력하는데 이메일의 첫번째 철자부터 세번째
#세번째 철자까지만 출력하시오!

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6][:3])
#%%
#문제288. 우리반 데이터 이메일을 출력하는데 이메일에서 도메인만 출력하시오.

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6][emp_list[6].find('@')+1:])

#%% 
import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    a = emp_list[6].find('@')+1
    b = emp_list[6].rfind('.')
    print(emp_list[6][a:b])
    
#%%문제290. rfind도 domain.co.kr 같은 곳은 domain.co 까지 끊겨서 생기지 않을까요?
import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    a = emp_list[6].find('@')+1
    b = emp_list[6][a:].find('.')
    print(emp_list[6][a:a+b])
#%%

import csv
file = open("c:\\data\\emp123.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    a = emp_list[6].find('@')
    result = emp_list[6][a:]
    b = result.find('.')
    print(result[1:b])

#%%

a = '''1,"이준혁",29,"남","경영학과"'''
print(a) # 1,"이준혁",29,"남","경영학과" 
print(a.split(','))

# 설명: 1,"이준혁",29,"남","경영학과" <- 이 데이터를 문자열 변수에 
# 할당하고 싶은데 문자열들 중에 더블 쿼테이션 마크가 있다면 양쪽에 
# (''') 싱글 쿼테이션 마크를 3개를 써서 둘러줘야 합니다.
# print(a.split('",'|',"'))
   

#%%문제291 아래의 url 변수에 있는 문자열은 슬래쉬(/)로 구분되어 있는데 
# 이 문자열의 요소를 아래의 리스트처럼 구성하시오!

url ='http://www.naver.com/news/today=20191204'

url = url.split('/')
print(url) # ['http:', '', 'www.naver.com', 'news', 'today=20191204']

#%%join
a = ['http:', '', 'www.naver.com', 'news', 'today=20191204']
bond = '/'

url = bond.join(a)
print(url) # http://www.naver.com/news/today=20191204

# 설명: 문자열 함수인 join 을 이용해서 리스트의 요소를 불러와서 다시 문자열로 만들수 있습니다.

#%%문제292. 우리반 데이터에서 이름만 출력하시오!

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1])
    
#%%문제293. 위에서 출력된 이름을 a리스트에 담고 a 리스트를 출력하시오!

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)

a =[]
for emp_ename in emp_csv:
    a.append(emp_ename[1])
    
print(a)

#%%문제294. 위의 a 리스트에 담겨진 이름을 하나씩 뽑아서 콤마(,) 로 연결해서 아래와 같이 
#문자열로 출력되게 하시오.

#이준혁,한결,...

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)

a =[]
for emp_ename in emp_csv:
    a.append(emp_ename[1])

bond = ','

aa = bond.join(a)

print(aa)

#%%문제295. 위의 결과가 김씨부터 출력되게 하시오~
# (ㄱ,ㄴ,ㄷ,ㄹ 순서로~)
import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)

a =[]
for emp_ename in emp_csv:
    a.append(emp_ename[1])

bond = ','

a.sort() # 왜? a = a.sort  하면 에러가 나는데  그냥 a.sort()를 하나요?!

aa = bond.join(a)

print(aa)

#%% replace

txt = 'My password is 1234'
result = txt.repalce('1','0') # txt 문자열의 1를 0으로 변경해라~
print(result)

#%%문제296 emp2.csv 에서 이름과 월급을 출력하는데 월급을 출력할 때 0대신에 *로
# 출력하시오!

#SCOTT 3***
  
import csv

file = open('c:\\data\\emp2.csv')
emp = csv.reader(file)

for i in emp:
    print(i[1],i[5].replace('0','*'))

#%%문제297 아래의 리스트를 가지고 아래와 같이 출력하시오!

a = ['name:홍길동','age:17','major:경영학','nation:한국']

for i in a:
    print(i.replace(':',' ---> '))
     
#%%예제

# A는 숫자 65입니다. a 는 숫자 97 입니다.

#예제: chr 함수를 이용해서 숫자 65부터 127까지가 어떤 문자인지 출력하시오!

for i in range(65,128):
    print(i, '---->',chr(i))

#%%문제298. (점심시간 문제) 우리반 데이터에서 이름을 출력하는데 아래와 같이 출력되게 하시오!

#구윤모(26),권세원(34), 
import csv
file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)

a=[]
for i in emp:
    a.append(i[1]+'('+i[2]+')')

a.sort()
bond =','
print(bond.join(a))

#%%

import csv
file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)
a=[]

for i in emp:
    a.append(i+'('+i+')')
print(emp)
a.sort()
bond =','
print(bond.join(a))


#%% decode

txt = 'A'
b_txt = txt.encode()
print(b_txt) # b'A' --> binary(이진) 'A' 라는 뜻 --> 0과 1로 표현하는 데이터
                            # --> 컴퓨터가 알아볼수 있는 바이너리 데이터
print(txt) # A 사람이 알아볼수 있는 언어인 알파벳 A
c_txt = b_txt.decode() # 컴퓨터가 알아볼 수 있는 언어--> 사람이 알아볼수 있는 언어로 변경


print(c_txt) # A
file= opne("c:\\data\\emp1222.csv",encoding="UTF8")
#설명:  emp1222.csv 를 파이썬으로 로드하는데 파이썬으로 load 하려면
      # 컴퓨터가 알아볼 수 있는 언어로 변경해야 합니다. 
      # 이때 문자 집합셋을 유니코드 문자집합셋인 UTF8을 이용해서 인코딩 
      # 즉 컴퓨터가 알아볼 수 있는 언어로 변경하겠다는 것입니다.
#%%  range()

print(     range(1,11))
print(list(range(1,11)))
print(type(range(1,11)))

#%%문제299. 아래와 같이 주사위의 눈을 담은 리스트를 만드시오!

# 결과: [1,2,3,4,5,6]

dice = (list(range(1,7)))

print(dice)

#%%문제300. 주사위 2개를 만들고 주사위 2개를 동시에 던져서 두 주사위의 눈의 합이 10이 나오는 확률을 구하시오!
import random as r

dice1 = list(range(1,7))
dice2 = list(range(1,7))
cnts = 0
cnt = 0
for i in range(10000):
    result1 = r.choice(dice1)
    result2 = r.choice(dice2)
    cnts += 1
    if result1 + result2 == 10:
        cnt += 1
print(cnt/cnts)

#%%문제301. 아래의 결과를 출력하시오!

#  [2,4,6,7,10,12,14,16,18] 

a = list( range(2,20,2)) # range(시작숫자,끝숫자,스텝)
                         # 시작숫자부터 끝숫자 미만까지 스텝만큼 증가해서
                         # 출력한다.

print(a)

#%% 리스트에서 특정 위치의 요서 얻기

a = [1,2,'a','b','c',[4,5,6]]

print(a)

# 예제1. 위의 리스트 a 에서 숫자2를 출력하시오!

print(a[1]) # index를 활용한다.

# 예제2. 위의 리스트 a에서 숫자4를 출력하시오!

print(a[-1][0])

#%%문제302. 아래의 리스트에서 숫자 7을 출력하시오!

b = [2,3,4,[5,6],[7,8],9]
print(b[4][0])

#%% index

a = [1,2,'a','b','c',[1,2,3]]

print(a.index(2))
print(a[-1].index(2))
print(a.index('a'))

#%%

list_a = ['a','b','c','d','e','f','g']
print( list_a[0]) #a

list_a[0] = 'z'
print(list_a)

#%%문제304. list_a 의 알파벳 d 를 k로 변경하시오!

list_a = ['a','b','c','d','e','f','g']

list_a[list_a.index('d')] = 'k'
print(list_a)
#%%
list_a = ['a','b','c','d','e','f','g']
print(list_a[0:4]) # 
print(list_a[2:]) #
print(list_a[:3]) #

#%%문제305. 위에는 알파벳 a 부터 g 까지 담은 리스트 만들었는데
# 이번에는 알파벳 a 부터 z까지를 담는 리스트를 list_a 로 생성하시오~

import string

print( string.ascii_lowercase)

list_a =[]
for i in string.ascii_lowercase:
    list_a.append(i)

print(list_a)

list_b=list(string.ascii_lowercase)
print(list_b)

#%%문제306. 위에서 만든 list_a에서 요소를 검색하는데 맨끝에 알파벳 z빼고 모든 요소를 다 출력하시오!
# ['a', 'b', 'c', ... 'x', 'y', 'z']

import string

list_a =[]
for i in string.ascii_lowercase:
    list_a.append(i)

print(list_a[0:list_a.index('z')])
print(list_a[0:-1])

#%% 짝수번쨰

list_a = ['a','b','c','d','e','f','g','h']
print( list_a[1::2]) # ['b','d','f','h']

# 문제307. 1부터 100까지의 숫자중에 짝수만 아래의 list_a 에 담아서 출력하시오.

list_a = (list(range(1,101)))

print(list_a[1::2])

#%% 역순

list_a = ['a','b','c','d','e','f','g','h']  
list_a.reverse()
print(list_a)   

#%%문제308. 우리반 테이블에서 이름을 출력하는데 ㅎ 부터 ㄱ 까지 출력될수 있도록 하시오.

import csv

file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)

a = []
for i in emp:
    a.append(i[1])

a.sort()
a.reverse()

print(a)

#%%문제309. emp2.csv 에서 이름과 월급을 출력하시오!

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    print(i[1],i[-3])
    
#%%문제310. 위의 데이터 중 월급을 비어있는 리스트인 a 리스트에 담으시오.
import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

a = []
for i in emp:
    a.append(i[-3])

print(a)

#%%문제311. 위의 a 리스트에 있는 월급을 월급이 높은 순서대로 정렬해서 a 리스트에 들어있게 하시오.

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

a = []
for i in emp:
    a.append(int(i[-3]))

a.sort() # 순으로 정렬하고
a.reverse() # 역순
print(a)

#%% reversed

list_a = ['a','b','c','d','e','f','g','h']
list_b = ['a','b','c','d','e','f','g','h']

list_a.reverse() # 원본을 바꾸는 함수
print(list_a)

result = reversed(list_b) # 원본 데이터를 그대로 유지 한채로 다른곳에 저장.
print(list_b)
print(list(result))

#%% ( + ) 리스트 더하기

a = ['a','b','c','d']
b = ['e','f','g','h']
c = a + b

print (c)

#%%문제312. 아래와 같이 엄마와 아기가 함께하는 수영교실 나이 리스트를 생성하시오!

# [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] 
# 34 10개, 2 10개

a = []
for i in range(10):
    a.append(34)
for i in range(10):
    a.append(2)
print(a)

listdata1 = [34]
listdata2 = [2]
listdata3 = listdata1*10 + listdata2*10
print(listdata3)

#%% 리스트 반복하기 (*)

listdata = list(range(3))
result = listdata*3
print(result)

#%%문제313. 아래의 엄마와 아기가 함꼐하는 수영교실의 나이의 평균값을 출력하시오!

import numpy as np

swim_age = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

a = np.array(swim_age) # numpy array (배열) 로 만들어준다.
b = np.mean(a)
print(b)  #18.0

print(sum(swim_age)/len(swim_age))

#%%문제314. 아래의 엄마와 아기의 수영교실의 중앙값을 출력하시오 !
# ( 중앙값은 가운데 있는 값)

import numpy as np

swim_age = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
a = np.array(swim_age) # numpy array (배열) 로 만들어준다.
b = np.median(a)
print(b)  #18

#%%문제315. 엄마와 아기가 함꼐하는 수영교실 나이에서 최빈값을 출력하시오.
swim_age = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

from scipy import stats
import numpy as np
a = np.array(swim_age)
result = stats.mode(a)
print(result)

#%%문제316. 우리반 나이 데이터를 비어있는 리스트 a 에 담으시오.
import csv

file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)

a=[]
for i in emp:
    a.append(int(i[2]))

#%%문제317. 우리반 나이 데이터의 평균값과 중앙값과 최빈값을 출력하시오!

import csv
import numpy as np

file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)

a=[]
for i in emp:
    a.append(int(i[2]))

print(a)

aa = np.array(a)

mean_a = np.mean(aa)
medi_a = np.median(aa)
most_a = stats.mode(aa)

print ('평균값 '+ str('%.2f'%mean_a),'중앙값 '+ str(medi_a),'최빈값 '+ str(most_a))

#%%파이썬으로 히스토그램 그래프 그리기
# 예제1: 평균이 150이고 표준편차가 5인 초등학생 10만명의 키를 생성한다.

import numpy as np

height = np.random.randn(100000)*5 + 151

#.2 계급의 크기를 나타내는 가로의 길이를 설정.
bins = list(range(142,162,2))
# 3. 히스토그램 그래프의 세로 데이터와 가로 데이터를 만드는 작업
hist, bins = np.histogram(height, bins) # 단지 도수분포로 뽑아 준다.
print(hist,bins)

# 4. 위의 데이터를 가지고 히스토그램 그래프를 그린다.

import matplotlib.pyplot as plt

plt.hist( height, bins)

#%% 5 . 모양 다듬기및 정리
import matplotlib.pyplot as plt
import numpy as np


height = np.random.randn(100000)*5 + 151
bins = list(range(142,162,2))
plt.grid()
# plt.figure(figsize=(12, 10))
plt.hist( height, bins, rwidth=0.8, alpha=0.7, color='orange')

#%%문제318. (오늘의 마지막 문제) 우리반 나이 데이터를 가지고 히스토그램 그래프를 그리시오!

# x 축의 계급(간격)은 24~44(2살 간격으로)

import matplotlib.pyplot as plt
import numpy as np
import csv

file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)

age = [ int(i[2]) for i in emp ]
bins = [ i for i in range(24,45,2)]
plt.grid()
plt.hist(age, bins, rwidth= 0.8, alpha = 0.8, color='orange')

plt.title('12') 
plt.xlabel('cnt')               
plt.ylabel('age')    

#%% 결이 답

import csv
import numpy as np
import matplotlib.pyplot as plt

emp12 = open("c:\\data\\emp1222.csv")
emp12 = csv.reader(emp12)
next(emp12)               # 컬럼명 날리기
a=[]
for i in emp12:
    a.append(int(i[2]))
x_val = list(range(int(min(a)),int(max(a))+1,2))
a = np.array(a)

plt.xticks(x_val)         # x축 눈금 조절. 검색해서 찾았습니다.
plt.yticks(range(0,12))   # y축 눈금 조절.
plt.hist(a,x_val,rwidth = 0.8,)
















