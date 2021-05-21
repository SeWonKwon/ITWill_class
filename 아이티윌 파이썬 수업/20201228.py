# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 09:50:24 2020

@author: stu02
"""
print(len(bin(9)[2:]))

#%% 1. 문제를 이해하고 출력이 뭐가되는지 정확하게 이해해야합니다.

n  =	5
arr1  =	[9, 20, 28, 18, 11]
arr2  = [30, 1, 21, 17, 28]

print(secretmap(arr1,arr2,n))

# 출력	["#####","# # #", "### #", "# ##", "#####"]
#%%풀이를 번호 순서대로 한글로 적는다.(메모)
#  2.1 십진수를 이진수 변환한다.
#  2.2 두개의 이진수를 가지고 #과 공백을 나타낸다.


#%%문제525. 숫자 9를 이진수로 변환하시오.

print(bin(9))  # 0b1001 b는 binary 라는 뜻 2진법이라는 뜻

print(oct(9)) # 8진법
print(hex(9)) # 16진법

#%%문제526. 위의 결과에서 0b 는 안나오고 1001만 출력되게 하시오.

print(bin(9)[2:])

print((str(0)*(5-len(bin(9)[2:])))+str(bin(9)[2:]))

print((str(0)*(5-len(bin(30)[2:])))+str(bin(30)[2:]))

#%%문제527. 숫자 30의 이진수를 아래와 같이 출력하시오 !

print(bin(30)[2:])

#%%문제528. 아래와 같이 출력되는 change 함수를 생성하시오.

def change(num):
    return bin(num)[2:]

print(change(30))

#%%문제529.위에서 만든 change 함수에 숫자 9를 넣고 출력해보시오!
def change(num):
    return bin(num)[2:]

print(change(9))




#%%문제530. change 함수를 실행할때 아래와 같이 입력 매개변수를 하나 더 만들어서 입력 매개변수의 길이만큼
#  숫자 0이 채워져서 출력되게 하시오!
def change(num,n):
    a = bin(num)[2:]
    return (str(0)*(n-len(a)))+str(a)

print(change(9,5))

#%%

def change(num,n):
    return bin(num)[2:].rjust(n,'0')  

# 설명: rjust(5,'0') 은 출력되는 자리수를 전체 5자리로 잡고
# 나머지 왼쪽에 '0' 을 채워넣어라~ ljust 는 오른쪽에 넣는다.

print(change(9,6))
print(type(change(9,6)))

#%%문제531. 카카오 문제 예제를 가지고 아래의 결과를  출력하시오 !
n  =	5
arr1  =	[9, 20, 28, 18, 11]
arr2  = [30, 1, 21, 17, 28]

# 결과: 2진수로 다 바꿔서 나오게 하여라

def change(arr1,arr2,n):
    for i,k in zip(arr1,arr2):
        print(bin(i)[2:].rjust(n,'0'),bin(k)[2:].rjust(n,'0')) 

change(arr1,arr2,n)

#%%
n  =	5
arr1  =	[9, 20, 28, 18, 11]
arr2  = [30, 1, 21, 17, 28]

def change(num,n):
    return bin(num)[2:].rjust(n,'0') 

for i in range(n):
    print(change(arr1[i],n),change(arr2[i],n))

#%%문제532. 위에서 출력된 아래의 결과를 이용해서 두 지도의 
# 숫자가 둘다 0이면 공백(" ")을 출력하고 아니면 벽("#")을 출력하시오.

n  =	5
arr1  =	[9, 20, 28, 18, 11]
arr2  = [30, 1, 21, 17, 28]

def change(num,n):
    return bin(num)[2:].rjust(n,'0') 


for i in range(n):
    a1 = change(arr1[i],n)
    a2 = change(arr2[i],n)
    f = ' '
    for j in range(n):
        n2+= 1
        if a1[j] == '0' and a2[j] == '0':
            f = f + ' '
        else:
            f = f + '#'
            
    result.append(f)

#%%문제533. 위의 코드를 함수로 생성해서 아래와 같이 수행되게하시오 !

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

secretmap(arr1,arr2,n)

# 결과:
# ["#####","# # #", "### #", "# ##", "#####"]['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']

#%%


def change(num,n):
    return bin(num)[2:].rjust(n,'0') 

def secretmap(arr1,arr2,n):
    result= []
    for i in range(n):
        a1 = change(arr1[i],n)
        a2 = change(arr2[i],n)
        f = ''
        for j in range(n):
            if a1[j] == '0' and a2[j] == '0':
                f = f + ' '
            else:
                f = f + '#'
        result.append(f)
        
    return result
    
    
n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(secretmap(arr1,arr2,n))


#%%

def secretmap(arr1,arr2,n):
    result= []
    for i in range(n):
        a1 = change(arr1[i],n)
        a2 = change(arr2[i],n)
        f = ''
        for j in range(n):
            if a1[j] == '0' and a2[j] == '0':
                f = f + ' '
            else:
                f = f + '#'
        result.append(f)
        
    return result
    
    
n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(secretmap(arr1,arr2,n))

#%%도박사 이야기~ 통계 문제

#%%문제534. 동전 하나를 10000번 던져서 앞면이 나오는 횟수를 출력하시오!

import random

cnt = 0
for i in range(10000):
    cnt += (random.randint(0,1))
print(cnt)


#%%제538. (점심시간 문제)동전을 8번 던졌을때 뒷면이 0번 ~ 8번 나오는 횟수가 아래와 같이 ...


import random
result=[]
for j in range(9):
    cnts = 0
    for i in range(100000):
        cnt = 0
        for t in range(8):
            cnt += (random.randint(0,1))
        if cnt == j:
            cnts += 1
    result.append(cnts)

print(result)

#%%문제539. 위의 횟수를 가지고 아래와 같이 확률이 출력되게하시오!

import random
result=[]
for j in range(9):
    cnts = 0
    for i in range(100000):
        cnt = 0
        for t in range(8):
            cnt += (random.randint(0,1))
        if cnt == j:
            cnts += 1
    result.append(cnts)

print(result)

#%%문제 540

import random
result=[]
for j in range(9):
    cnts = 0
    for i in range(100000):
        cnt = 0
        for t in range(8):
            cnt += (random.randint(0,1))
        if cnt == j:
            cnts += 1
    result.append(cnts)

print(result)

coin_cnt = [i for i in range(9)]
b = [i/100000 for i in result]

import  matplotlib.pyplot  as  plt 

plt.bar( coin_cnt, b, tick_label= coin_cnt, align='center', color='red')
plt.show()

#%%문제541. coin_cnt 를 입력값으로 해서 coin_cnt 의 요소들의 평균값과 표준편차를 출력하시오 !

import numpy as np

coin_cnt = [i for i in range(9)]

c_m = np.mean(coin_cnt)
# c_m = np.mean(result)

c_s = np.std(coin_cnt)
# c_s = np.std(result)

print(c_m)
print(c_s)

#%%문제542. 위에서 구한 평균값과 포준편차를 이용해서 coin_cnt 의 요소값에 대한 확률밀도 함수 값을 출력하시오 !
# (scipy.stats 의 norm 사용)
# norm.pdf(입력값,평균값,표준편차)

from scipy.stats import norm

# result = norm.pdf(result,c_m,c_s)
result = norm.pdf(coin_cnt,c_m,c_s)

print(result)


#%%543. coin_cnt 를 x 축으로 두고 위의 확률밀도 함수값을 y 축으로 두어서 확률 밀도 함수 그래프를 그리시오!

plt.plot(coin_cnt,result,color='black')
plt.show()

#%%문제544. 위의 그래프에서 신뢰구간 68%에 해당하는 부분만 녹색으로 색칠하시오 !


plt.plot(coin_cnt, result, color='black')
plt.fill_between(coin_cnt,result, where=(coin_cnt<c_m+c_s)&(coin_cnt>=c_m-c_s), color='green')
plt.show()

#%%문제545. (파이썬 마지막 문제) 위의 코드들을 이용해서 아래와 같이 출력되게 하시오.

동전을 8번 던졌을 때 동전이 뒷면이 나오는 횟수가 신뢰구간 68% 안에 드는지 아닌지를 출력하는 함수를

생성하시오

print ( coin_hypo(동전 뒷면의 횟수) )

print ( coin_hypo(4) )

동전을  8번 던졌을 때 뒷면이 나오는 횟수가 4번이 나올 확률은 신뢰구간 68% 안에 있습니다. 

print ( coin_hypo(8) )

동전을  8번 던졌을 때 뒷면이 나오는 횟수가 8번이 나올 확률은 신뢰구간 68% 안에 없습니다.

#%%

import random
result=[]
for j in range(9):
    cnts = 0
    for i in range(100000):
        cnt = 0
        for t in range(8):
            cnt += (random.randint(0,1))
        # if cnt == j:
        #     cnts += 1
        result.append(cnt)

print(result)
# b = [ i/100000 for i in result]
# print(b)

#%%
# [0,   1,     2,    3,     4,      5,     6,    7,     8 ]
# [384, 3096, 10930, 22052, 27351, 21542, 11013, 3135, 397]

import numpy as np

coin_cnt = [i for i in range(9)]

# c_m = np.mean(coin_cnt)
c_m = np.mean(result)

# c_s = np.std(coin_cnt)
c_s = np.std(result)

print(c_m)
print(c_s)

result2 = norm.pdf(coin_cnt,c_m,c_s)

print(result2)

#%%
plt.plot(coin_cnt, result2, color='black')
plt.fill_between(coin_cnt,result2, where=(coin_cnt<c_m+c_s)&(coin_cnt>=c_m-c_s), color='green')
plt.show()
#%%
from scipy.stats import norm

# result = norm.pdf(result,c_m,c_s)
result2 = norm.pdf(result,c_m,c_s)

print(result2)

#%%
plt.plot(coin_cnt, result2, color='black')
plt.fill_between(coin_cnt,result2, where=(coin_cnt<c_m+c_s)&(coin_cnt>=c_m-c_s), color='green')
plt.show()

#%%
import random
result=[]
for j in range(9):
    cnts = 0
    for i in range(100000):
        cnt = 0
        for t in range(8):
            cnt += (random.randint(0,1))
        # if cnt == j:
        #     cnts += 1
        result.append(cnt)

print(result)

import numpy as np

coin_cnt = [i for i in range(9)]

c_m = np.mean(result)

c_s = np.std(result)

print(c_m)
print(c_s)

from scipy.stats import norm

result2 = norm.pdf(coin_cnt,c_m,c_s)

print(result2)


plt.plot(coin_cnt, result2, color='black')
plt.fill_between(coin_cnt,result2, where=(coin_cnt<c_m+c_s)&(coin_cnt>=c_m-c_s), color='green')
plt.show()

#%%
import random
import numpy as np

def coin_avg_std(num):             #동전을 몇번 던지냐에 따른 평균과 표준편차 를 생성
    result=[]
    for i in range(num):
        cnt = 0
        for t in range(8):
            cnt += (random.randint(0,1))
        result.append(cnt)
    return c_m = np.mean(result),c_s = np.std(result)

def coin_hypo(num):
    c_m,c_s = coin_avg_std(10000) # 동전 몇번 던진지를 선택
    if c_m-c_s<=num<=c_m+c_s:
        return f'동전을  8번 던졌을 때 뒷면이 나오는 횟수가 {num}번이 나올 확률은  신뢰구간 68%안에 있습니다.'
    else:
        return f'동전을  8번 던졌을 때 뒷면이 나오는 횟수가 {num}번이 나올 확률은  신뢰구간 68%안에 없습니다.'
    
print(coin_hypo(4))
print(coin_hypo(8)) 


#%%문제38. (오늘의 마지막 문제) 세원이 코드를 참고해서 신뢰구간 문제를 푸는데
#            동전을 10번을 던져서 뒷면이 0번 ~ 10번 나오는 횟수로 
#            신뢰구간 95% 에 속하는지의 여부를 출력되게하시오 !

# print(coin_hypo(4))

#  동전을  10번 던졌을 때 뒷면이 나오는 횟수가 4번이 나올 확률은  신뢰구간 95%안에 있습니다.'

# print(coin_hypo(10)) 

#  동전을  10번 던졌을 때 뒷면이 나오는 횟수가 10번이 나올 확률은  신뢰구간 95%안에 없습니다.'

import random
import numpy as np

def coin_avg_std(num):                    #동전을 몇번 던지냐에 따른 평균과 표준편차 를 생성
    result=[]
    for i in range(num):
        cnt = 0
        for t in range(10):
            cnt += (random.randint(0,1))
        result.append(cnt)
        c_m= np.mean(result) 
        c_s = np.std(result)
    print(c_m,c_s)
    return c_m,c_s 

def coin_hypo(num):
    c_m,c_s = coin_avg_std(10000)       # 동전 몇번 던질지를 선택
    if c_m-1.96*c_s<=num<=c_m+1.96*c_s: # 신뢰도 95% 1.96
        return f'동전을  10번 던졌을 때 뒷면이 나오는 횟수가 {num}번이 나올 확률은  신뢰구간 95%안에 있습니다.'
    else:
        return f'동전을  10번 던졌을 때 뒷면이 나오는 횟수가 {num}번이 나올 확률은  신뢰구간 95%안에 없습니다.'
    
# print(coin_hypo(4))
# print(coin_hypo(10)) 

for i in range(11):
    print(coin_hypo(i))
    
    #%%
    
import random
import numpy as np

def coin_avg_std(num):                    #동전을 몇번 던지냐에 따른 평균과 표준편차 를 생성
    result=[]
    for i in range(num):
        cnt = 0
        for t in range(10):
            cnt += (random.randint(0,1))
        result.append(cnt/10) # 나온 비율 값으로 변경
        c_m = np.mean(result)
        c_s = np.std(result)
    print(c_m,c_s)
    return c_m,c_s 

def coin_hypo(num):
    c_m,c_s = coin_avg_std(10000)       # 동전 몇번 던질지를 선택
    if c_m-1.96*c_s<=num/10<=c_m+1.96*c_s: # 신뢰도 95% 1.96 # num/10 은 뽑힌 비율?!
        return f'동전을  10번 던졌을 때 뒷면이 나오는 횟수가 {num}번이 나올 확률은  신뢰구간 95%안에 있습니다.'
    else:
        return f'동전을  10번 던졌을 때 뒷면이 나오는 횟수가 {num}번이 나올 확률은  신뢰구간 95%안에 없습니다.'
    
# print(coin_hypo(4))
# print(coin_hypo(10)) 

for i in range(11):
    print(coin_hypo(i))

    