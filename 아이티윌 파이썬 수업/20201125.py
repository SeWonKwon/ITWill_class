# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:42:37 2020

@author: STU-14
"""

#%%
#문제23

for a in range(1,10): # 1부터 10미만까지
    print('2 x', a,' = ', a*2) # , 는 단지 구분점

#%%
#문제24

for a in range(1,10): 
    print('2 x', a,' = ', a*2)
for a in range(1,10): 
    print('3 x', a,' = ', a*3)
for a in range(1,10): 
    print('4 x', a,' = ', a*4)
for a in range(1,10): 
    print('5 x', a,' = ', a*5)
for a in range(1,10): 
    print('6 x', a,' = ', a*6)
for a in range(1,10): 
    print('7 x', a,' = ', a*7)
for a in range(1,10): 
    print('8 x', a,' = ', a*8)
for a in range(1,10): 
    print('9 x', a,' = ', a*9)
#%%
#예제
for j in range(1,10):
    for i in range(1,10):
         print('2 x', i,' = ', i*2)
         
   
         
for j in range(2,10):
    for i in range(1,10):
         print( j,'x', i,' = ', i*j)
         

for j in range(2,10):
    for i in range(10):
        if i == 0:
            print(j,'단')
        else:
            print( j,'x', i,' = ', i*j)
         
         
#%%
#문제25.

import random

dice = [1,2,3,4,5,6]
for i in range(1,11):
    print(random.choice(dice))
#%%
#나온 주사위의 숫자를 모은 리스트
import random

dice = [1,2,3,4,5,6]

d_list = []
for i in range(1,11):
    d_list.append(random.choice(dice))
    
print(d_list)
 #%%
#문제26.   

import random

cnt = 0
dice = [1,2,3,4,5,6]
for i in range(1,11): # 10번
    result = random.choice(dice) #주사위의 눈이 result 변수에 할당이 된다.
    if (result)%2 == 0: #짝수
        cnt = cnt + 1 # 숫자 세는 도구
    
print( cnt ) # for 에 맞추어서 가장 앞에 둔다.

#%%
#문제27.   
    
import random

dice = [1,2,3,4,5,6]

for j in range(5):
    cnt = 0 # 초기화
    for i in range(1,11): # 10번
        result = random.choice(dice) #주사위의 눈이 result 변수에 할당이 된다.
        if (result)%2 == 0: #짝수
            cnt = cnt + 1 # 숫자 세는 도구
    
    print( cnt ) # for 에 맞추어서 가장 앞에 둔다  

#%%
#문제28.

import random

coin = ['앞면','뒷면']
cnts = 0
cnt  = 0
for i in range(100):
    result = random.choice(coin)
    cnts = cnts + 1
    if result == '앞면':
        cnt = cnt + 1

print ( cnt/cnts)

#%%
#문제29.

import random

coin = ['앞면','뒷면']

for j in range(50):   
    cnts = 0
    cnt  = 0
    for i in range(100):
        result = random.choice(coin)
        cnts = cnts + 1
        if result == '앞면':
            cnt = cnt + 1
    
    print ( cnt/cnts)
#%%
#append 활용법
a = [ ] #비어 있는 리스트 a를 생성합니다.
a.append(7) # a 리스트에 숫자 7을 넣는다.
print (a)
a.append(8) # a 리스트에 숫자 8을 넣는다.
print (a) 
    
#%%
#문제30

import random

coin = ['앞면','뒷면']
cp_list = [] #비어 있는 리스트를 생성한다.

for j in range(50):   
    cnts = 0
    cnt  = 0
    for i in range(100):
        result = random.choice(coin)
        cnts = cnts + 1
        if result == '앞면':
            cnt = cnt + 1
    print (cnt/cnts)
    cp_list.append(cnt/cnts) # 확률을 입력한다.

print (cp_list) #list에 담겨있는 값들을 출력한다.

#%%
#문제31.

import random

coin1 = ['앞면','뒷면']
coin2 = ['앞면','뒷면']

cnt = 0
for i in range(1,301):
    result1 = random.choice(coin1)
    result2 = random.choice(coin2)
    if result1 == '앞면' and result2 == '앞면':
        cnt = cnt + 1
print (cnt)
    

#%%
#문제32

import random

coin1 = ['앞면','뒷면']
coin2 = ['앞면','뒷면']

x = [ ]
for i in range(1000):
    cnt = 0
    for i in range(1,301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if result1 == '앞면' and result2 == '앞면':
            cnt = cnt + 1
    x.append(cnt)   
    
print(x)




#%%
#문제33

import random
import numpy as np  # 넘파이 모듈을 이용하여 
                    # 평균, 표준편차, 분산

coin1 = ['앞면','뒷면']
coin2 = ['앞면','뒷면']

x = [ ]
for i in range(1000):
    cnt = 0
    for i in range(1,301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if result1 == '앞면' and result2 == '앞면':
            cnt = cnt + 1
    x.append(cnt)   
    
print(np.mean(x)) 
print(np.var(x))
print(np.std(x))

#%%
#34

import random as r
import numpy as np

dice = [1,2,3,4,5,6]

x=[]

for i in range(1000): # 1000번 반복수행하는 for loop 문 작성
    cnt = 0 # cnt 에 0을 할당합니다.
    for i in range(360): # 360번 반복수행하는 for loop문 작성
        result = r.choice(dice) # 주사위에서 눈을 하나 출력해서 result 에 담는다.
        #if result%3  == 0:// if result in 3,6:
        if result == 3 or result == 6: # 3의 배수
            cnt = cnt +1 #카운트를 하나씩 올린다.
    x.append(cnt) # x 리스트에 담는다.
    
print(x)
print(np.mean(x)) 
print(np.var(x))
print(np.std(x))

#%%
#문제35: for~ continue~ break

for i in range(1,11):
    print(i)

#%%
#문제36

for i in range(1,11):
    if i ==5:
        continue # 이 부분을 그냥 지나치고 
    print(i)      # 다음 루프 실행문을 계속 실행해라.

#%%
#문제37 for continue

for i in range(1,11):
    if i%2 == 1: # i 가 홀수이면  재껴라~
        continue
    print(i)
    
    #%%
    #문제37

for i in range(1,11):
    if i == 5: # i 가 5이면  그만 돌려라~
        break
    print(i)
    
#%%
# 문제38
a = 0
for i in range(1,11):
    a = a + i
print(a)

#또는

x = []
for i in range(1,11):
    x.append(i)
print(sum(x))

#또는

print(sum([a for a in range(1,11)]))

#%%
#예제
for i in range(1,11): # 1부터 10까지 루프를 돌리는데
    print(i) # i를 출력을 하다가
    if i == 3: # i가 3이면
        break  # 루프문을 종료시켜라~
        
#%%
#문제39.

a = int(input('숫자를 입력하세요~'))

for i in range(1,101):
    print (i)
    if i == a:
        break

#%%
#문제40.

a = int(input('숫자를 입력하세요~'))
b = int(input('숫자를 입력하세요~'))

x_list = []
if a > b:
    for i in range(1,a+1):
        if a%i == 0 and b%i ==0:
            x = i
            x_list.append(i)
elif a == b:
    x_list.append(a)
elif b > a: 
    for i in range(1,b+1):
        if a%i == 0 and b%i ==0:
            x = i
            x_list.append(i)      
        
print(max(x_list))

#%%
#문제40-1
a = int(input('숫자를 입력하세요~'))
b = int(input('숫자를 입력하세요~'))

for i in range(max(a,b),0,-1):          # max 함수를 써서 a,b의 대소 비교를 바로 할수 있다.
    if a%i == 0 and b%i == 0:
        c = i
        break
print('최대공약수는',c,'입니다.')

#%%
#문제40-2
#최대 공약수
a = int(input('숫자를 입력하세요~'))
b = int(input('숫자를 입력하세요~'))

i = max(a,b) + 1
while i > 0:
    i = i - 1
    if a%i == 0 and b%i == 0:
        c = i
        break
print(c)

#%%
#문제40-3 최소 공배수

a = int(input('숫자를 입력하세요~'))
b = int(input('숫자를 입력하세요~'))
        
for i in range(a+b,0,-1):
    if a%i == 0 and b%i == 0:
        c = i
        break
print(a*b/c)       
        
#%%
#예제

for i in range(1,11):
    print(i)
else:
    print('Perfect') # break 에 의해서 루프문이 중단되면
    #else 다음에 실행문이 실행되지 않습니다."""
    
    
#%%
#문제41.

a = int(input('숫자를 입력하세요~'))

for i in range(1,1+a):
    print (i)

#%%
#문제42

a = int(input('숫자를 입력하세요~'))

for i in range(1,1+a):
    print (i)
else:
    print('퍼펙트')

#%% for 
#문제42-1

a = int(input('숫자를 입력하세요~'))

for i in range(1,1+a):
    if i%2 == 0:    
        continue
    print (i)
    if i == 13:
        break
else:
    print('퍼펙트')

#%%
#문제43


a = int(input('숫자를 입력하세요~'))
b = int(input('숫자를 입력하세요~'))
for i in range(1,1+a):
    print (i)
    if i == b:
        break
else:
    print('퍼펙트')
    
    
#%%
#예제

print('for loop')
for i in range(10):
    print(i)
    
print('while loop')
x = 0 
while x < 10:
    print(x)
    x = x + 1
    
#%%
#문제44

b = int(input('숫자를 입력하세요~'))
a = 0

while a <  b:
    a = a + 1
    print(a,'♥'*a)
    
#%%
#문제45

b = int(input('숫자를 입력하세요~'))

while b > 0:
    print('♥'*b)
    b = b - 1

#%%
#문제46
import random

coin = [a for a in range(6)]
a_list = []

x = 1
while x < 10001:
    resulta = random.choice(coin)
    resultb = random.choice(coin)
    x = x + 1
    a_list.append(resulta + resultb)
    
print(a_list)
print(len(a_list))

#%%
#문제47
import random as r

coin = [1,2,3,4,5,6]
a_list = []

x = 1
while x < 10001:
    resulta = r.choice(coin)
    resultb = r.choice(coin)
    x = x + 1
    if resulta + resultb ==10: #두개의 주사위의 눈의 합이 10이면
        a_list.append(resulta + resultb) #리스트에 추가해라 ~
    
print(len(a_list)/x)

#%%
#예제

print(2**31)

#%%
#문제48

for i in range(11):
    a = i**i
    print (a)



#%%
#문제49 

print(3**2)

#%%
#문제50

import math

print( math.sqrt(4) )

#%%
# 난수 구하기
import random 
print(random.uniform(0,1))

#%%
#문제51

import random as r

cnt = 0
p_list = []

for i in range(10000000):
    x = r.uniform(0,1)
    y = r.uniform(0,1)
    if x**2 + y**2 <= 1 :
        p_list.append((x,y)) #부채꼴 안의 점이라면
    cnt = cnt +1   
    
print(len(p_list)*4/cnt)

#%%
#예제

print(43.2-43.1)

c1 = 1 +7j
print( c1.real ) # 복소수형 자료에서 실수부만 취한다.
print( c1.imag ) # 복소수형 자료에서 허수부만 취한다.

c2 = complex(2,3) # 실수부가 2이고 허수부가 3인 복소수를 만든다.
print(c2)

#%%
#문제52

c1 = 1 -2j

print(c1**2 -2*c1-12)

c2 = complex(1,-2)

print(c2**2 -2*c2-12)
#%%
#









    