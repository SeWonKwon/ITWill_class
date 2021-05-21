# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:30:47 2020

@author: neva
"""

#%%예제:이스케이프 문자
    
print('나는 파이썬을 배웁니다. \n 파이썬은 자바보다 \
훨씬 쉽습니다.')

#%%%예제:리스트형

k = [ 'a', 'b', 'c', 'd', 'e' ]
print ( k )
print( type(k))
print(k[1]) # 인덱
print(k[0:2]) # 슬라이싱


#%%문제122. 동전의 앞면과 뒷면을 포함하는 리스트 coin을 만드시오!

coin = ['앞','뒤']

#%%문제123. 위에서 만든 coin 의 요소를 10000개로 늘려서 coin_10000 변수에 담으시오!

coin = ['앞','뒤']

coin_10000 = coin*10000

print(len(coin_10000))

#%%문제124. 위에서 만든 coin_10000 리스트에서 표본을 10개를 랜덤 추출하시오!

import numpy as np

coin = ['앞','뒤']
coin_10000 = coin*10000


r = np.random.choice(coin_10000,10)
# r = np.random.choice(coin,10)
print(r)

#설명: np.random.choice 은 numpy 모듈안에 random 코드 안에 choice 함수를 사용하겠다.
# np.random.choice(모집단 리스트, 샘플 갯수)

#%%문제125. 위에서 추출한 샘플 10개에서 앞면이 몇번 나오는지 출력하시오!

import numpy as np

coin = ['앞','뒤']
coin_10000 = coin*10000


r = np.random.choice(coin_10000,10)

cnt = 0
for i in r:
    if i == '앞':
        cnt += 1

print(cnt)

a = '앞'and'앞'and '앞' in r
print(a)
    


#%%list와 튜플 비교

a = [ 1,2,3,4,5 ]
print( type(a))
print(a[0])

a[0] = 7
print (a) # a리스틔 0번째 요소가 7로 변경이 됨

#%%문제126. a 리스트에 인덱스 번호 3번을 17로 변경하시오 !

a = [ 1,2,3,4,5 ] 
a[0] = 7

a[3] = 17 # 인덱스 번호 0 1 2 3 4 5  0부터 시작한다. 즉 3번은 4번째 이다.

print (a)

#%% 튜플은 데이터를 변경할 수 없습니다.

b = (1,2,3,4,5)
print(b[0])

b[0] = 7 # TypeError: 'tuple' object does not support item assignment

#설명 : 회사에서 변경이 되어서는 안되는 데이터는 프로그래밍 할때 튜플로 만들어서 관리한다.

# 예를 들어 신세계 백화점, 이마트에서 사용하는 포인트 적립 카드에서 포인트 적립시 구매금액의 0.01%로 적립을 해준다고 하면
# 이 0.01 은 절대로 프로그램에서 변경이 되어서는 안되는 데이터 이므로 튜플로 관리해야 합니다. 

#%%문제127. 아래의 숫자 데이터들을 튜플로 생성하시오! 튜플 변수 이름은 point 라고 하세요!

# 0.01, 0.02, 0.03, 0.04, 0.05

point = ( 0.01, 0.02, 0.03, 0.04, 0.05) 
print(type(point))

#%%문제128. 위의 튜플 point 의 요소중 0.03 만 뽑아서 출력하시오!

point = ( 0.01, 0.02, 0.03, 0.04, 0.05) 
print(type(point))

print(point[2])

#%%문제129. 위의 튜플의 모든 요소를 다 출력하시오!
point = ( 0.01, 0.02, 0.03, 0.04, 0.05) 
print(type(point))

for i in point:
    print(i)
    
for j in 'scott':
    print(j)

#%%예제: 사전형

a = { 'apple':'사과','banana':'바나나','peach':'복숭아','pear':'배'}
#        키     값
b = { 'a':1,'b':2,'c':3,'d':[1,2,3],'e':(1,2,3)}
# print (a)
# print ( type(a) ) # <class 'dict'>
# print(a.keys())  # 키값들만 출
# print(a.values()) # 값들만 출력
print(a['apple'])
print(sum(b['d'])/len(b['d']))
#%% 

a['grape'] = '포도' #새로운 키와 값을 추가하는 방법
print(a)

#%%예제:
b = { } # 비어있는 딕셔너리 생성한다.

b['apple'] = '사과'
b['pear'] = '배'
b['grape'] = '포도'
print(b)
print(b.keys())
print(b.values())


#%%문제130. 아래의 두개의 리스트를 각각 만들고 아래와 같이 fruit 라는 딕셔너리를 생성하시오!

a = ['사과','배','포도','복숭아','바나나']
b = ['apple','pear', 'grape', 'peach','banana']

fruit = {}
for i,j in zip(a,b):
    fruit[i] = j

print(fruit)

#%%내장함수

# 예제: 아래의 SQL을 파이썬으로 구현하시오!
# SQL> select lower(ename)
#       from emp;

# pandas>
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
    print(i.lower(), type(i)) # lower 사용법 : 변수값.lower()
    
#%%문제131. (점심시간 문제) 아래의 SQL을 파이썬으로 구현하시오 !

# SQL> select lower(ename),lower(job)
#        from emp;

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
for i,j in zip(emp['ename'],emp['job']):
    print(i.lower(),j.lower())

#%% 함수를 생성하는 방법
# 	def 함수이름(매개변수1,매개변수2,….):
# 		실행문
#         return 출력값이 있는 변수명

def add_number( n1, n2 ):
    result = n1 + n2 # n1 에 입력된 값과 n2에 입력된 값을 더해서 result 에 입력한다.
    return result # result 에 입력된 값을 출력한다.

#위에서 만든 함수를 실행하는 방법

print(add_number(1,2))

#  설명: 위와 같이 만들고 컴퓨터를 껏다가 켠다음 다시 아래와 같이 
#        함수를 실행만 하게 되면 실행되지 않는다. 다시 add_number 함수를 생성해줘야 합니다.


# * 콜론(:) 으로 끝을 맺는 경우 4가지

# 1. if 문 종료시 예: if 조건:
# 2.for 문 종료시 예: for i in range(1,11):
# 3. 함수 생성시 예: def 함수이름(입력 매개변수):
# 4. 클래스 생성시 예: class 클래스 이름:

#%%문제132. 1부터 10까지 출력하시오 !

for i in range(10):
    print(i+1)

#%%문제133. 1부터 10까지 다 더한 값을 출력하시오 !

a = 0
for i in range(10):
    a = a + i + 1
print(a)

#%%문제134. 위의 코드를 이용해서 함수를 생성하는데 아래와 같이 숫자를 입력하고
#           함수를 실행하면서 해당 숫자까지 1부터 다 더한 값이 출력되게 하시오!

def all_add(n):
    a = 0
    for i in range(n):
        a = a + i + 1
    return a # 함수 생성시 return 절은 필수 입니다~~~~
    
print(all_add(10))

#%%문제135. 다음의 문자열 변수를 생성하고 문자열 변수의 문자를 소문자로 출력하시오 !

a = 'SCOTT'

print(a.lower()) # scott
print('SCOTT'.lower()) # scott

#%%문제136. 아래의 문자열을 대문자로 출력하시오!

a = 'scott'

print(a.upper())
print('scott'.upper())

#%%문제137. 아래의 문자열에서 첫번째 철자만 출력하시오 !

a = 'scott'

print(a[0])

#%%문제138.
#%%문제139.
#%%문제140. 아래의 함수를 생성하시오! (첫번째 철자 대문자 나머지 소문자로 출력되게 하는 함수)

def initcap(val):
    return val[0].upper() + val[1:].lower()
     
print( initcap('scott') )

#%%예제:

def add_text( t1, t2 ):
    return t1 + '  ' + t2

print(add_text('파이썬','자바'))

# 매개변수에 아무것도 입력하지 않고 실행하면 기본값이 출력되겠금 함수를 생성하는 방법

def add_text(t1,t2 ='최고'):
    return t1 + ' ' + t2

print( add_text('파이썬','자바'))
print( add_text('파이썬'))

# 설명: t2에 값을 아무것도 안넣었더니 기본값으로 지정한 최고가 출력되었습니다.

#%%예제:
    
strdata = '전역변수' # func1 함수 외부에 있는 변수 (텀블러)

def func1():
    strdata2 = '지역변수' # func1 함수 내부에 있는 변수 : 스타벅스 머그컵
    return strdata2

print(func1())

# * 설명: 대부분 많은 코드들이 지역변수를 사용합니다.
#         그러면 '전역변수'를 사용하는 경우는 언제 입니까?

pi = 3.141592653689793

def cycle_func1( num1 ): # 원의 넓이를 구하는 함수
    global pi # 전역변수 pi를 함수내부로 가져올 수 있습니다.
              # global 이라는 키워드를 앞에 쓰면 됩니다.
    return pi*num1*num1

def cycle_func2( num1 ):
    global pi
    return 1/4*pi*num1*num1


print(cycle_func1(5))
print(cycle_func2(5))

#%%

pi = 3.141592653689793

def cycle_func2( num1 ):
    global pi
    return 1/4*pi*num1*num1

print (cycle_func1(5)) # 함수를 호출하는 호출자 코드입니다.

*절대값을 출력하는 함수 (무조건 양수로 출력하는 함수)

print ( abs(-9) ) # 9
print ( abs( 9) ) # 9

#%%문제141. abs 함수를 사용하지 말고 if 문을 이용해서 절대값을 출력하는 my_abs 라는 함수를 생성하시오!

 
# if를 사용
# def my_abs(num):
#     if num < 0 :
#         return num *(-1)
#     else:
#         return num

# while 을 사용
def my_abs(num):
    while num < 0 :
        num = num*(-1)
    return num

print ( my_abs(-9) ) # 9
print ( my_abs( 9) ) # 9

#%% 예제

import time
print('5초간 프로그램을 정지합니다.')
time.sleep(4.999999)
print('5초가 지났습니다.')

#%%예제: 평균이 30이고 표준편차가 5인 가우시안 정규분포를 따르는 모집단을 백만개 구성하는 코드


import numpy as np # numpy 모듈을 임폴트를 합니다.

avg = 30
std = 5
N = 10000000
mogip = np.random.randn(N)*std + avg
print( mogip )

#%%문제142. 서울시 초등학생의 키를 백만명의 모집단을 구성하는데 평균키가 148.5이고
#           표준편차가 30인 모집단을 만드시오!
import numpy as np

avg = 148.5
std = 30
N = 1000000
height = np.random.randn(N)*std*avg
print(len(height))


#%%문제143. 위의 모집단에 100명을 표본으로 추출하여 100명의 평균키를 
#           비어있는 리스트 a 에 입력하는 작업을 10000번 수행하여 
#           a 리스트에 10000개의 표본의 평균키가 입력되게 하시오!

import numpy as np

avg = 148.5
std = 30
N = 1000000
height = np.random.randn(N)*std+avg
print(height)

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean()) # 모집단에서 100개를 평균값을 취해라~
    
print(a)

#설명: 초등학생 100만명의 키 모집단에서 표본을 100개 추출해서 표본 평균을 10000개 모았음

#%%문제144. 통계구현을 전문으로 구현하는 모듈인 scipy 모듈을 임폴트하여 
#            위의 표본의 평균키값에 대한 확률밀도 값을 출력하시오!
import numpy as np
from scipy.stats import norm # scipy의 stats 패키지로 부터 
                             # norm이라는 모듈을  import 해라~ 

avg = 148.5
std = 30
N = 1000000
height = np.random.randn(N)*std+avg
print(height)

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean()) 

x = np.arange(140, 160, 0.001) #140~160까지 0.001 간격으로 숫자를 생성
y = norm.pdf( x, np.mean(a), np.std(a))
# y = norm.pdf( x, 표본평균값들의 평균값, 표본평균값들의 표준편차)
#초등학생 키의 표본평균값들에 대한 확률 밀도함수 값이 출력됩니다.
print(y)


#%%문제145. 데이터 시각화 전문 모듈인 matplotlib 을 import 하여 위의
#  표본 평균값 10000개의 데이터에 대한 확률 밀도함수 값으로 정규분포 그래프를 그리시오!

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt #matplotlib 모듈안에 pyplot 라는 함수를
                                #임폴트하는데 별칭을 plt 로 해라~

avg = 148.5
std = 30
N = 1000000
height = np.random.randn(N)*std+avg

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean()) 

x = np.arange(140, 160, 0.001)
y = norm.pdf( x, np.mean(a), np.std(a))

plt.plot(x,y,color='blue')
plt.show()

#%%문제146. 위의 확률밀도함수 그래프의 아래쪽 영역도 색깔로 채우시오~

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt #matplotlib 모듈안에 pyplot 라는 함수를
                                #임폴트하는데 별칭을 plt 로 해라~

avg = 148.5
std = 30
N = 1000000
height = np.random.randn(N)*std+avg

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean()) 

x = np.arange(140, 160, 0.001)
y = norm.pdf( x, np.mean(a), np.std(a))

plt.plot(x,y,color='purple')
plt.fill_between( x,y, interpolate = True, color = 'skyblue',alpha = 0.7)
# 설명: plt 모듈안의 fill_between 함수를 이용해서 확률밀도함수 그래프의 아래영역을
# 색깔로 채우는데 interpolate = True 를 이용해서 아래의 영역이 색깔로 채워지게 되고
#  color를 지정하고, alpha 는 투명도(0~1) 사이로 기술 할수 있습니다.
plt.show()

#%%문제147. 위에서 그린 확률밀도함수 그래프의 색깔을 변경하고 그래프를 사진으로 첨부해서 올리세요~

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt 

avg = 148.5
std = 30
N = 1000000
height = np.random.randn(N)*std+avg

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean()) 

x = np.arange(140, 160, 0.001)
y = norm.pdf( x, np.mean(a), np.std(a))

plt.plot(x,y,color='darkmagenta')
plt.fill_between( x,y, interpolate = True, color = 'orange',alpha = 0.34)
plt.show()














