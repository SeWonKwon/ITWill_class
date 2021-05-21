# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:41:15 2020

@author: STU-14
"""

#%%모듈을 생성하기

def add_number(n1, n2):
    result = n1 + n2
    return result

print ( add_number(1,2))


# c:\\Users\\STU-14\\Desktop\\20201202.py
# 비교: c:\\users\\std\\.spyder-py3\\temp.py
#                       .의 의미는 숨김폴더라는 것이다.



#C:\\Users\\STU-14\\Desktop\\my_cal.py
    
def add_number(n1, n2):
    result = n1 + n2
    return result

# 위의 함수 스크립트를  c:\\Users\\std\\ 밑에 my.cal.py라는 이름으로
# 저장을 함


#메뉴에 새로운창을 여세요~~
#새로운 창에서 아래와 같이 임폴트를 합니다.

import my_cal #my_cal 모듈을 임폴트합니다.

print ( my_cal.add_number(1,2)) # my_cal 모듈안에 add_number 함수를
                                  # 실행해라~
                                  
#설명 : 이번창에서는 def 로 add_number 함수를 만드는 코드는 없습니다.
#       my_cal.py 모듈안에 있는데 그 모듈을 이 창에서 사용할수 있도록 import 했습니다.

#%% 문제148 my_cal.py 모듈 스크립트 안에 곱하기를 하는 아래의 함수를 추가하시오!

def gob_number(n1, n2)
    result = n1*n2
    return result

#%% 문제149. 다른 새로운 창에서 my_cal 모듈을 임폴트하고 gob_number 함수를 실행하시오!

print ( my_cal.gob_number(1,2) )

#%%문제150. 이번에는 나누기를 하는 함수를 my_cal.py 에 저장하고
#           다른 새로운 창에서 아래와 같이 import 하고 실행 될수 있도록 하시오.

def devide(n1, n2):
    result = n1/n2
    return result

print ( my_cal.devide(10,2)) 

#%% 파이썬 패키지를 만드는 단계


# 	1. 아래의 디렉토리에 my_loc 라는 폴더를 생성한다.
# 	
# C:\\Users\\stu-14\my_loc

# 	2. my_loc 폴더 안에 my_cal.py 를 옮겨 놓는다.
# (my_cal.py 를 my_loc 폴더에 복사하고 기존에 있던 my_cal.py는 지우시오 )

# 	3. 이 평범한 폴더가 패키지로 인정을 받으려면 반드시 갖고 있어야하는 파일이 있습니다.
# 	그 파일이 __init__.py 라는 파일입니다.
# 	c:\\Users\\STU-14\my_loc
# 						   |
# 						   |
# 						   1. __init__.py
# 						   2. my_cal.py
# 	4. 새로운 창에서 아래와 같이 스크립트를 수행합니다.

	from my_loc import my_cal # from 패키지 import 모듈
	
	print ( my_cal.add_number(1,2)) # my_cal 모듈 안에 있는 add_number 함수를 실행해라~
	print ( my_cal.gob_number(1,2) )
	print ( my_cal.devide(10,2)) 

#%% import 를 이해하기

#파이썬 내장 모듈이 무엇이 있는지 확인하는 방법
import sys
print ( sys.builtin_module_names)

print ( len(sys.builtin_module_names) )
# 65개

#%% sys.path 에 정의된 디렉토리가 무엇인지 확인하는 방법

import sys

for i in sys.path:
    print(i)

#%%

  

#	1. 리스트로만 했을때

a = [ [1,2], [4,7] ]

print(a)

#   2. numpy  array 로 했을때

import numpy as np

a = [ [1,2], [4,7] ]
a2 = np.array(a)  # a 리스트를 numpy 배열로 구성함

print(a2)

#%%문제152. 아래의 행렬의 합을 출력하시오!

import numpy as np

a = [[1,2],[4,5]]
b = [[3,1],[6,2]]

a2 = np.array(a)
b2 = np.array(b)

print(a2+b2)

#%%문제153. 아래의 행렬의 합을 출력하시오!

a = [[6,3,4],[5,1,7]]
b = [[4,5,7],[9,20,4]]

a2 = np.array(a)
b2 = np.array(b)

print(a2+b2)

#%%문제154. 아래의 행렬의 곱을 먼저 손으로 구하시오!


#%%문제154-1 numpy를 이용해서 해보기

import numpy as np

a = [[1,2],[4,3]]
b = [[2,1],[3,4]]

a2 = np.array(a)
b2 = np.array(b)

print( np.dot(a2,b2) )

#%%문제155. 아래의 행렬의 곱을 출력하시오!

a = [[3,4,1],[2,4,3]]
b = [[2,1],[4,3],[6,7]]

a2 = np.array(a)
b2 = np.array(b)

print( np.dot(a2,b2) )

#%%예제1. 아래의 리스트에서 최대값을 출력하시오!

a = [28,23,21,29,30,40,23,21]

import numpy as np
a2 = np.array(a)
print( np.max(a2))

#예제2 . 아래의 리스트에서 최대값, 최소값, 평균값, 최빈값, 중앙값을 출력하시오!

a = [28,23,21,29,30,40,23,21,21]

import numpy as np
from scipy.stats import mode
a2 = np.array(a)

print (np.max(a2))
print (np.min(a2))
print ( np.mean(a2))  #평균값
print ( np.median(a2)) # 중앙값             
print ( mode(a) ) # 최빈값

#%% 이미지 파일을 파이썬에서 여는 방법
# 1. lena.png 파일을 내려받아 c:\\data\\ 밑에 저장합니다.

# 2. 아래의 코드를 실행합니다.
       
              
       	
import PIL.Image as pilimg # 이미지를 파이썬에서 시각화 하기 위한 모듈
import numpy as np
import matplotlib.pyplot as plt #데이터 시각화 전물 모듈을 임폴트합니다.
	
im = pilimg.open('c:\\data\\lena2.png') # lena.png 파일을 읽어서 im 에 입력
pix = np.array(im) #넘파이 배열로 변환
plt.imshow(pix) #화면에 띄웁니다.

#%%문제156. 폐사진을 파이썬에서 시각화 하시오!
              
import PIL.Image as pilimg
import numpy as np
import matplotlib.pyplot as plt

im = pilimg.open('c:\\data\\1.png')
pix = np.array(im)              
plt.imshow(pix)              
print(pix) 

#%%클래스 생성
# 예제1. 총 클래스(설계도) 를 생성하시오!

# 총의 기능 :  1.  총알을 장전하는 기능
# 		       2.  총알을 쏘는 기능
		
class Gun(): # 권장사항으로 첫번째를 대문자 하기를 권장함: 왜냐? 클래스임을 구분짓기 위해
    def charge( self, num): # 총알을 충전하는 함수
        self.bullet = num
    
    def shoot(self, num ): # 총을 쏘는 함수
        for i in range(num):
            if self.bullet > 0:
                print('뿅!')
                self.bullet -= 1
            elif self.bullet  == 0:
                print('총알이 없습니다.')
                break

# 예제2. 위에서 만든 총설계도를 가지고 총을 한정 만드시오!

gun1 = Gun()

#gun1 = 제품(객체)
#Gun() 클래스(총 설계도)

# 예제3. gun1 이라는 제품에 총알 10발 충전합니다.

gun1.charge(10)

#%%
# 예제4. 총을 쏴보시오 ~

gun1.shoot(3)

#설명 : 파이썬 클래스를 만들때 self 키워드는 필수입니다. 안쓰면 에러놥니다.
# self 의 뜻은 자기자신입니다. 이 총설계도로 총을 만들고 그 총을 사용할때
# charge 와 shoot 기능을 사용할 것인데 이 때 이 총이 내꺼라는 의미가 바로
# self 입니다.

총을 생산하는 명령어 --> gun1 = Gun() #준혁이
                        gun2 = Gun() #한결
                        gun3 = Gun() #세원

# 준혁이가 gun1 총을 사서 다음과 같이 충전했습니다.

gun1.charge(100)

# 실제로 총설계도에는 charge(self,num) 이라고 해서 
# 입력 매개변수가 2개인데 총을 사용할 때 충전 할때는 
# gun1.charge(100) 이렇게 매개변수 하나에 값을 입력했습니다.
# 그러면 self 입력매개변수에는 자동으로 gun1 이 들어갑니다.

#%%문제157. 총설계도를 수정해서 총알을 아래와 같이 충전하면
#        몇발이 충전되었습니다. 라는 메세지가 출력되게 하시오!

class Gun(): 
    def charge( self, num): 
        self.bullet = num
        for i in range(1,num+1):
            print(i,'발이 충전되었습니다.')
        print('충전이 완료되었습니다.')
            
    def shoot(self, num ): # 총을 쏘는 함수
        for i in range(num):
            if self.bullet > 0:
                print('뿅!')
                self.bullet -= 1
            elif self.bullet  == 0:
                print('총알이 없습니다.')
                break


gun1 = Gun()

gun1.charge(10)

#%%문제158. 이번에는 총을 쏘면 총아리 뿅! 뿅! 하면서 아래쪽에 몇발 남았습니다.
# 라는 메세지가 출력되게 하시오!

class Gun(): 
    def charge( self, num):
        self.bullet = num
        for i in range(1,num+1):
            print(i,'발이 충전되었습니다.')
        print('충전이 완료되었습니다.')
            
    def shoot(self, num ): 
        for i in range(num):
            if self.bullet > 0:
                print('뿅!')
                self.bullet -= 1
            elif self.bullet  == 0:
                print('총알이 없습니다.')
                break
        print('총알이', self.bullet,'발이 남았습니다.')       

gun1 = Gun()

gun1.charge(10)

gun1.shoot(3)


#%%문제159. 총을 처음 생산했을때 총알이 반드시 0발 장전되겠금 하시오!

class Gun():
    def __init__(self): # 초기 함수 생성시에 조건을 설정하는 함수
        self.bullet = 0  # 설계도를 가지고 처음 만들때만 작동하고 그다음엔 작동안함
        print('딱총이 만들어졌습니다.',self.bullet,'발 장전 되었습니다.')
        # class 를 만들때 자동으로 작동된다.
    def charge( self, num):
        self.bullet = num
        for i in range(1,num+1):
            print(i,'발이 충전되었습니다.')
        print('충전이 완료되었습니다.')
            
    def shoot(self, num ): 
        for i in range(num):
            if self.bullet > 0:
                print('뿅!')
                self.bullet -= 1
            elif self.bullet  == 0:
                print('총알이 없습니다.')
                break
        print('총알이', self.bullet,'발이 남았습니다.')

gun1 = Gun()

gun1.charge(100)

gun1.shoot(3)
#%%문제160. 총클래스를 이용해서 아래와 같이 카드 클래스를 만들고 아래와 같이 카드를 충전하고 사용하시오!

# 카드가 발급되었습니다.


# 10000원 충전 되었습니다.


# 1000원이 사용되었습니다.

class Card():
    def __init__(self):
        self.money = 0
        print('카드가 발급되었습니다.')
    def charge(self,num):
        self.money = num
        print(num,'원 충전 되었습니다.')
    def consume(self,num):
        if self.money -num >= 0:
            self.money -= num
            print(str(num)+'원이 사용되었습니다.')
            print(self.money,'원 남았습니다.')
        elif self.money == 0:
            print('잔액이 없습니다.')
        else :
            print('잔액이 부족합니다.')
card1 = Card()
# # 카드가 발급되었습니다.

card1.charge(10000)
# # 10000 원 충전 되었습니다.
#%%
card1.consume(3000)
# # 1000원이 사용되었습니다.

# 0원일때 를 체크해서 다시 조정해!

#%%class 에 import 넣기
import time

class Gun():
    def __init__(self): # 초기 함수 생성시에 조건을 설정하는 함수
        self.bullet = 0  # 설계도를 가지고 처음 만들때만 작동하고 그다음엔 작동안함
        print('딱총이 만들어졌습니다.',self.bullet,'발 장전 되었습니다.')
        # class 를 만들때 자동으로 작동된다.
    def charge( self, num):
        self.bullet = num
        for i in range(1,num+1):
            print(i,'발이 충전되었습니다.')
            time.sleep(0.3)
        print('충전이 완료되었습니다.')
            
    def shoot(self, num ): 
        for i in range(num):
            if self.bullet > 0:
                print('뿅!')
                self.bullet -= 1
            elif self.bullet  == 0:
                print('총알이 없습니다.')
                break
        print('총알이', self.bullet,'발이 남았습니다.')

gun1 = Gun()

gun1.charge(10)

gun1.shoot(3)

print(type(gun1))
#%%예: 
a = [1,2,3,4]
print( type(a) ) # <class 'list'>

#
#card1.charge(1000)

#객체   메소드 (기능)


a.append(5)
# a -> 객체, append()-> 메소드(기능) 
print(a)



#%%리스트 객체의 유용한 메소드

# let's get it drileddddd!

#list.count(obj) : returns count of how many times obj occurs in list
a = [1,2,3,1,2,2,2,3,4] # a 라는 리스트 객체(제품)가 생성됨
print(a.count(2)) # a 리스트에 숫자 2가 몇개가 있는지 조회

# list(seq) : Converts a tupll into list
a = ('a','b','c')
print(a)

a = list(a)
print(a)

#list.append(obj) : Appends object obj to list
a.append('d')
print(a)

#list.extend(seq) : 리스트에 리스트 붙이기
b = [1,2,3,4,5]
a.extend(b)
print(a)

#list.index(obj) : Returns the lowest index in list that obj appears
# 처음 등장 하는 index 값 찾기
print(a.index('b'))
print(a.index(1))

#list.insert(index, obj) : insert obj into list at offset index
a.insert(3,'new one')
print(a)

#list.pop(obj = list[-1]) : remove and returns last object or obj from the list
a.pop()
print(a)

a.pop(-6)
print(a)

#list.remove(obj) : removes the given object from th list
a.remove('d')
a.remove('a')
print(a)

## 비교 pop vs remove : pop 은 index no로 remove는 특정 수치로

#list.reverse() : reverses objects order of list in place
a.reverse()
print(a)

#list.sort() : ascending order, default setting
a.remove('b')
a.remove('c') # 문자와 숫자가 섞여 있으면 에러남
a.sort()
print(a)
a.sort(reverse=True)
print(a)



#%%문제161. 초등학생 키에 대한 모집단을 생성하세요! ( 천만개로 구성)
# 키의 평균값은 140, 표준편차 5로 해서 생성하시오

import numpy as np

avg = 140
std = 5
N = 10000000
height = np.random.randn(N)*std + avg

#%%문제162. 위의 모집단에 표본을 100개를 추출해서 표본의 평균을 출력하시오.

import numpy as np

avg = 140
std = 5
N = 10000000
height = np.random.randn(N)*std + avg

print(np.random.choice(height,100).mean())

#%% 문제163. 위에서 표본 100개를 뽑아서 평균값을 구해서 a 라는 비어 있는 리스트에 담는 작업을 10000번 수행하시오.

import numpy as np

avg = 140
std = 5
N = 10000000
height = np.random.randn(N)*std + avg

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean())

print(len(a))

#%% 문제164. 위에서 구한 표본 평균값들 10000개의 평균값과 표준편차를 
# s_avg 와 s_std 변수에 각각 담으시오!


import numpy as np

avg = 140
std = 5
N = 10000000
height = np.random.randn(N)*std + avg

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean())

s_avg = np.mean(a)
s_std = np.std(a)

print(s_std)

#%% 문제165. 초등학생 키 데이터를 120부터 160까지 0.001 간격으로 생성하시오!



x = np.arange(120,160,0.001)

print(x)

#%%문제166. 위에서 만든 x 에 있는 키값들을 x 축으로 두고 
#  확률 밀도함수 그래프를 생성하는데 y축의 확률밀도함수값을 구할때
# 문제 164번에서 구한 평균값, 표준편차를 이용하시오~

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
avg = 140
std = 5
N = 10000000
height = np.random.randn(N)*std + avg

a = []
for i in range(10000):
    a.append(np.random.choice(height,100).mean())

s_avg = np.mean(a)
s_std = np.std(a)

x = np.arange(138,142,0.001)
y = norm.pdf(x,s_avg,s_std)

plt.plot(x,y,color='purple')
plt.fill_between(x,y,interpolate = True, color ='orange', alpha = 0.34)
plt.show()

#%%(오늘의 마지막 문제) 문제167.
# 어느 도시의 초등학생의 수는 전체 10만명입니다. 학생들의 평균키는 140이고 표준편차는 5입니다.
# 이 도시의 10만명의 초등학생 중 무작위로 한명을 추출했을때 키가 145 ~ 150 사이에 있을 확률은 어떻게 될까요?
import random as r
import numpy as np

heihgt = np.random.randn(100000)*5 + 140

cnt = 0
cnts = 0
for i in range(10000):
    result = r.choice(height)
    cnts += 1
    if 145<=result<150:
        cnt += 1

print(cnt/cnts)