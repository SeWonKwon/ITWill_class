# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:28:02 2020

@author: neva
"""

a = 1
b = 2
print(a+b)

#%%
# 문제1. 답

for i in [ 1, 2, 3, 4, 5, 6, 7]:
    print (i)
    
#%%

#문제2. 답

for i in [ 2, 3 ,4]:
    print (i)

#%%
#문제3. 답

import keyword
print (keyword.kwlist)


#%%
#문제4.

False = 1
True = 2
print(False+True)

#%%
#예제

a = 1
b = 'scott'
print(b)

#%%
#파이썬의 철학

import this

#%%
#문제5

b = 'scott'
print (b)
print (type(b))  # <class 'str'>

#%%
#문제6

a = 5
print (a)
print (type(a))  # <class 'int'>

#%%
#예제
""" 아래의 프로그램은 a 변수에 1를 할당해서 프린트하는 
     프로그램 입니다. """

# 변수 a 에 숫자 1을 할당합니다.

#%%
#실습

d = [ 1, 2, 3]
print(d)
print(d[0]) # d 리스트에서 첫번째 요소를 프린트해라 

c = { 1, 2, 3 }
print( c ) 
# print(c[0]) 딕셔너리 형은 순서가 없어서 이런식으로 쓸수가 없다.

a = {1,1,2}
print(a)    # 딕셔너리 형은 중복된 자료를 제거하여 저장한다.
#%%
m = { 'i' : '나는', 'am':'입니다', 'boy':'소년' }
print (m)


#%%
#문제7

mmm = [ 'a', 'b', 'd', 'e', 'k', 'm', 'n', 'z' ]
print(mmm[-4])
print(mmm[4])

#%%
#문제8
import random # random 이라는 모듈을 이 코드에서 쓰겠다.
coin = ['앞면', '뒷면']
print ( random.choice(coin) )

#%%
#문제9

import random
	
dice = [ 1, 2, 3, 4, 5, 6 ]
print (random.choice(dice) )

#%%
#예제1

listdata = ['a', 'b', 'c']  # listdata 라는 변수로 리스트를 생성
if 'a' in listdata: # listdata 리스트 변수에 'a' 요소가 있다면
    print ( 'a 가 listdata 에 있습니다.' )  # 실행문을 실행해라~~

#%%
#문제10


dice = [ 1, 2, 3, 4, 5, 6, ]

if 5 in dice:
    print(' 주사위의 눈에 숫자 5가 있습니다.' )
    

#%%
#문제11

a = int(input(' 숫자를 입력하세요 ~') )
dice = [ 1, 2, 3, 4, 5, 6, ]                
if a in dice:
    print(' 주사위의 눈에 숫자 ', a, ' 가 있습니다.' )

#%%
#예제

a = int( input ( '숫자를 입력하세요 ~') )
if a%2 == 0:  # % 는 나눈 나머지값을 출력하는 연산자
	                  # ==는 equal (같다) 연산자 입니다.
			    #  =  은 할당 연산자 입니다.
	print('짝수 입니다')
else:
    print('홀수 입니다')


#%%
#문제12
a = int(input('숫자를 입력하세요~' ) )
d_list = [1,2,3,4,5,6]
if a in d_list:
	print (  a,' 가 주사위의 눈에 있습니다.' )
else:
    print (  a,' 가 주사위의 눈에 없습니다. ')

#%%
#문제13.

a = int(input('첫번째 숫자를 입력하세요'))
b = int(input('두번째 숫자를 입력하세요'))

if a > b:
    print( a,'는 ', b,' 보다 큽니다.' )
else:
    print( a,'는 ', b,' 보다 작습니다.' )


#%%
#예제

a = int(input('첫번째 숫자를 입력하세요'))
b = int(input('두번째 숫자를 입력하세요'))

if a > b:
    print( a,'는 ', b,' 보다 큽니다.' )
elif a==b:
    print('서로 같습니다.')
else:
    print( a,'는 ', b,' 보다 작습니다.' )

#%%
#예제
for i in [ 1, 2, 3 ] : #리스트
    print ( i )
    
for i in ( 1, 2, 3 ) : # 튜플
    print ( i )
    
for i in range(10): #range
    print (i)

m = { 'i' : '나는', 'am' : ' 입니다', 'boy':'소년'}
for i in m: #사전형
    print (i) # 키값만 출력되고 있습니다.


for i in 'i am a boy':  #문자형
    print (i)
#%%
for i in range(6):
	print(i) # 0부터 5까지 출력.
for i in range(1, 6):
	print(i) # 1부터 5까지 출력.
for i in range(1, 6, 2):
	print(i) # 1, 3 , 5 를 출력한다.
for i in range(6, 1, -1):
	print(i) # 6부터 1씩 차감해서 2까지 출력한다.



#%%
#문제14

print('★'*5)

#%%
#문제15

a = int(input('별을 몇개 넣을꺼니?'))

for x in range(a+1):
    print('★'*x)

#%%
#문제16

import random
dice = [ ds for ds in range(1,7) ]
for x in range(1,11):
    print(x, '번째는', random.choice(dice))

#%%
#문제17

import random  # random 모듈의 코드를 지금 현재 코드창에서 사용하겠다.
coin = ['앞면','뒷면']
for i in range(1,11):
    print ( i, random.choice(coin))

#%%
#문제18

import random  # random 모듈의 코드를 지금 현재 코드창에서 사용하겠다.

coin = ['앞면','뒷면']
cnt = 0 # cnt 라는 변수에 0을 할당한다.

for i in range(1,11): # 1부터 10까지 루프문을 10번 실행한다.
    result = random.choice(coin) # 동전 던진 결과를 result 변수에 할당한다.
    if result == '앞면':
        cnt = cnt +1 # 할당연산자 오른쪽 부터 실행하고 실행한 결과를 
        print(cnt) # 변수에 할당해 준다.

        #%%
#문제19

import random

dice = [nd for nd in range(1,7)]
cnt = 0
for a in range (1,101):
    result = random.choice(dice)
    if result == 3:
        cnt = cnt +1
print(cnt)

#%%
#문제20

import random

dice = [nd for nd in range(1,7)]
cnt = 0
for a in range (1,1001):
    result = random.choice(dice)
    if result == 5:
        cnt = cnt +1
print(cnt/1000*100,'%')

#%%
#문제21 동전을 10000번 던져서 앞면이 나올 확률을 출력하시오 !

import random

coin = ['앞면','뒷면']
cnt = 0
cntc = 0
for a in range (1,10001):
    result = random.choice(coin)
    cntc = cntc + 1
    if result == '앞면':
        cnt = cnt +1
print(cnt/cntc*100,'%')

#%%
#문제22.

import random

coin = ['앞면','뒷면']
dice = [n for n in range(1,7)]

cnt = 0
cntc = 0
for a in range (1,10001):
    result = random.choice(coin)
    result2 = random.choice(dice)
    cntc = cntc + 1
    if result == '앞면' and result2 == 5:
        cnt = cnt +1
print(cnt/cntc)

#%%
#문제21. drill

import random

num = int(input('시행횟수는?'))
coin = ['앞면','뒷면']
dice = [n for n in range(1,7)]

cnt = 0
cntc = 0
for a in range (1,num):
    result = random.choice(coin)
    result2 = random.choice(dice)
    cntc = cntc + 1
    if result == '앞면' and result2 == 5:
        cnt = cnt +1
print(cnt/cntc*100) 
