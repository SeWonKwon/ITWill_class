# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:48:32 2020

@author: neva
"""

#%%문제53. 주사위 1개를 10번 던지시오 !

import random 

dice = [1,2,3,4,5,6]
for i in range(1,11): # 아래의 실행문을 10번 수행하겠다.
    result = random.choice(dice) # 실행문1
    print (result) # 실행문2 
    #Indentation 이 같은 라인에 있기 때문에 같은 실행문이다.
    
#%%비교 문제 53

import random 

dice = [1,2,3,4,5,6]
for i in range(1,11): # 아래의 실행문을 10번 수행하겠다.
    result = random.choice(dice) # 실행문1
print (result) # for loop 문의 실행문이 아니다
    #Indentation 이 같은 라인에 있지 않기 때문에 같은 실행문이다.
    
#%%문제54. 주사위를 10번던져서 주사위의 눈이 3이 나오는 
#횟수를 출력하시오!

import random

dice = [1,2,3,4,5,6]

cnt = 0 # 횟수를 담기 위한 변수를 cnt라는 이름으로 만들고
        #숫자 0을 할당한다.
        
for i in range(1,11):
    result = random.choice(dice)
    if result == 3:
        cnt = cnt + 1 # indentation 을 주어야 if 문의 영향권 안에 들어 간다.
print(cnt)

#%% 문제55. 주사위를 10번 던져서 주사위의 눈이 짝수가
#나오는 횟수를 출력하시오!

import random

dice = [a for a in range(1,7)]
cnt = 0 

for i in range(10):
    result = random.choice(dice)
    if result in (2,4,6):
        cnt += 1

print(cnt)

#%% 문제56. 주사위를 2개를 동시에 던져 두개의 
#눈의 합이 10이 되는 횟수를 출력하시오. (주사위 2개를 20번)

import random # random 이라는 모듈을 지금 이코드에서 사용하겠다.
              # 모듈이란? 특정 

dice = [a for a in range(1,7)]
cnt = 0

for i in range(20):
    result1 = random.choice(dice) # for 실행문1
    result2 = random.choice(dice) # for 실행문2
    if result1 + result2 == 10:   # for 실행문3
        cnt += 1 # if 실행문1

print(cnt) #독립적인 실행

#%% 문제 57. 주사위의 2개를 동시에 던져서 두 눈의 합이 10이 되는 확률을
#출력하시오!

import random

dice = [a for a in range(1,7)]
cnt = 0
cntsum= 0

for i in range(100):
    result1 = random.choice(dice)
    result2 = random.choice(dice)
    cntsum += 1
    if result1 + result2 == 10:
        cnt += 1

print(cnt/cntsum)

#%%예제1. 밑수가 10이고 진수가 10인 log 값을 출력하시오.
import math

a = math.log10(10) #모듈이름.함수이름(매개변수값)
print(a)

#%%문제58. 아래의 수학식을 파이썬으로 구현하시오 !
import math

a = 2 * math.log2(10) + (1/3)* math.log2(10)

print(a)

#%%문제59.  주사위를 10번 던져서 주사위의 눈이 3이 나오는 횟수를 
  # 출력하시오 ! (축약 연산자를 이용해서 출력하시오 ! )
import random

dice = [1,2,3,4,5,6]
cnt = 0

for i in range(10):
    result = random.choice(dice)
    if result == 3:
        cnt += 1
print(cnt)

#%% 예제 

a = True
b = False

print (a)
print ( 1 == 1 ) #결과가 True 로 출력됩니다.
print ( 1 == 3 ) #결과가 False 로 출력됩니다.

#%%문제60. 주사위를 20번 던져서 주사위의 눈이 4이상 나오는 횟수를 출력하시오!

import random 

dice = [1, 2, 3, 4, 5, 6]
cnt = 0

for i in range(20):
    result = random.choice(dice)
    if result >= 4:
        cnt += 1
print(cnt)

#%%문제61. (통계 정규분포 문제)주사위 한개를 288회 던져서 주사위의 눈이
   #5이상 나오는 횟수를 구하시오. 

import random

dice = [1,2,3,4,5,6]
cnt = 0
cntsum = 0

for i in range(288):
    result = random.choice(dice)
    cntsum += 1
    if result >= 5:
        cnt += 1
print(cnt)
print(cntsum)
print(cnt/cntsum)

#%%문제 62. 주사위 한개를 288회 던질 때, 5 이상의 눈이 나오는 횟수가 
#           90 이상 100이하 나올 확률을 구하시오


import random

dice = [1,2,3,4,5,6]
cnt = 0
cntsum = 0

for i in range(288):
    result = random.choice(dice)
    cntsum += 1
    if result >= 5:
        cnt += 1
print(cnt)
print(cnt/cntsum)
print(cntsum)


#%%문제 63. 주사위 한개를 288회 던질 때 5 이상의 눈이 나올 횟수를 출력하는데 이 
# 작업을 100번해서 얼마나 횟수가 나왔는지를 100개를 출력하시오

import random

dice = [1,2,3,4,5,6]



for i in range(100):
    cnt = 0
    cntsum = 0
    for i in range(288):
        result = random.choice(dice)
        cntsum += 1
        if result >= 5:
            cnt += 1
    print(cnt)
    print(cnt/cntsum)
    print(cntsum)

#%%문제64위에서 출력된 횟수 100개를 비어있는 리스트 
	    # a 리스트에 담고 a 리스트의 갯수를 출력하시오 !


import random

dice = [1,2,3,4,5,6]

a = [ ]


for i in range(100): #반복실행할 실행문을 100번 수행
    cnt = 0 # 실행문 1
    for i in range(288): #실행문 2 for 문 아래전부
        result = random.choice(dice)
        cntsum += 1
        if result >= 5:
            cnt += 1
    a.append(cnt) # 실행문 3

print(len(a))



#%%문제65. 동전을 100번 던져서 앞면이 나오는 횟수를 출력하시오!

import random as r

coin =['앞','뒤']

cnt = 0
for i in range(100):
    result = r.choice(coin)
    if result == '앞':
        cnt += 1
print(cnt)

#%%문제66. 문제66. 동전한개와 주사위 한개를 동시에 100번 던져서 동전이 앞면이 나오고
#                  주사위의 눈이 5가 나오는 횟수를 출력하시오 !
import random as r

coin =['앞','뒤']
dice = [1,2,3,4,5,6]

cnt = 0
for i in range(100):
    resultc = r.choice(coin)
    resultd = r.choice(dice)
    if resultc == '앞' and resultd == 5:
        cnt += 1

print(cnt)

#%%문제67. 동전한개와 주사위 한개를 동시에 100번 던져서 동전이 앞면이 나오고 
#          주사위의 눈이 5가 나오는 횟수를 출력하는 그 작업을 50번해서 횟수가
#          50개가 출력되게 하시오 !

import random as r

coin =['앞','뒤']
dice = [1,2,3,4,5,6]

for i in range(50):
    cnt = 0
    for i in range(100):
        resultc = r.choice(coin)
        resultd = r.choice(dice)
        if resultc == '앞' and resultd == 5:
            cnt += 1
    print(cnt)      

#%%문제68. 위의 횟수 50개를 a 리스트에 넣어 보시오~

import random as r

coin =['앞','뒤']
dice = [1,2,3,4,5,6]
a= []
for i in range(50):
    cnt = 0
    for i in range(100):
        resultc = r.choice(coin)
        resultd = r.choice(dice)
        if resultc == '앞' and resultd == 5:
            cnt += 1
    a.append(cnt)     

#%%문제69. a 리스트에 50개 담겨있는지 확인하시오~

import random as r

coin =['앞','뒤']
dice = [1,2,3,4,5,6]
a= []
for i in range(50):
    cnt = 0
    for i in range(100):
        resultc = r.choice(coin)
        resultd = r.choice(dice)
        if resultc == '앞' and resultd == 5:
            cnt += 1
    a.append(cnt)     

print(len(a))

#%% numpy 사용하기
# numpy란?  딥러닝에 필요한 수학 연산을 쉽게 구현하기 위해서 만들어 놓은 모듈(특정 목적을 위해 만든 코드의 집합)
#예제1. 아래의 리스트의 요소들의 평균값을 출력하시오 !

import numpy as np # 넘파이 모듈을 이 코드에서 사용하겠다.
                   # numpy의 별칭을 np 라고 하겠다.
                   
b = [7,4,5,3,2]

print( np.mean(b))

#예제2. 아래의 리스트의 요소들의 평균값을 출력하시오 !
#         (numpy 사용하지 않고 수행하시오 !)
cnt = 0
cnts = 0
for i in b:
    cnt = cnt + i
    cnts += 1
print(cnt/cnts)

np.mean(a)   #평균
np.var(a)       #분산
np.std(a)   #표준편차
#%%문제70. 위의 a 리스트의 요소들의 평균값을 출력하시오.
#           (numpy를 이용해서 구현하시오!)

import random as r

coin =['앞','뒤']
dice = [1,2,3,4,5,6]
a= []
for i in range(50):
    cnt = 0
    for i in range(100):
        resultc = r.choice(coin)
        resultd = r.choice(dice)
        if resultc == '앞' and resultd == 5:
            cnt += 1
    a.append(cnt)     

print(sum(a)/50)

#%%문제71. 64번 코드를 가져와서 a 리스트의 요소들의 평균과 분산과 표준편차를 출력하시오!
# 주사위를 288번 던져서 주사위의 눈이 5이상이 나오는 횟수를 
#구하는 작업을 100번 수행해서 100개의 횟수를 a 리스트에 담았음
import random
import numpy as np

dice = [1,2,3,4,5,6]

a = [ ]


for i in range(100): #반복실행할 실행문을 100번 수행
    cnt = 0 # 실행문 1
    cntsum = 0
    for i in range(288): #실행문 2 for 문 아래전부
        result = random.choice(dice)
        cntsum += 1
        if result >= 5:
            cnt += 1
    a.append(cnt) # 실행문 3

print(np.mean(a))
print(np.var(a))
print(np.std(a))

#%%문제72. 위의 a 리스트에 담긴 요소 100개를 출력하시오 !

import random

dice = [1,2,3,4,5,6]

a = [ ]


for i in range(100): #반복실행할 실행문을 100번 수행
    cnt = 0 # 실행문 1
    cntsum = 0
    for i in range(288): #실행문 2 for 문 아래전부
        result = random.choice(dice)
        cntsum += 1
        if result >= 5:
            cnt += 1
    a.append(cnt) # 실행문 3
    
print(a)

#%%문제73. 위의 a 리스트의 요소들을 하나씩 빼내서 출력하시오!

import random

dice = [1,2,3,4,5,6]

a = [ ]


for i in range(100): #반복실행할 실행문을 100번 수행
    cnt = 0 # 실행문 1
    cntsum = 0
    for i in range(288): #실행문 2 for 문 아래전부
        result = random.choice(dice)
        cntsum += 1
        if result >= 5:
            cnt += 1
    a.append(cnt) # 실행문 3
    
for k in a:
    print(k)
    
#%%문제74. 그러면 a 리스트의 요소들의 숫자가 90이상이고 106이하일 갯수를 출력하시오!

import random

dice = [1,2,3,4,5,6]

a = [ ]


for i in range(100): #반복실행할 실행문을 100번 수행
    cnt = 0 # 실행문 1
    for i in range(288): #실행문 2 for 문 아래전부
        result = random.choice(dice)
        if result >= 5:
            cnt += 1
    a.append(cnt) # 실행문 3

cnt1 = 0
cntsum2 = 0    
for k in a:
    cntsum2 += 1
    if k >= 90 and k <= 106: # 90<= k <= 106: 가능
        cnt1 += 1
        
print(cnt1)
print(cntsum2)


#%%문제75. 그러면 a 리스트의 요소들의 숫자가 90이상이고 106 이하인 요소들의 확률을 출력하시오!

import random

dice = [1,2,3,4,5,6]

a = [ ]


for i in range(100): #반복실행할 실행문을 100번 수행
    cnt = 0 # 실행문 1
    for i in range(288): #실행문 2 for 문 아래전부
        result = random.choice(dice)
        if result >= 5:
            cnt += 1
    a.append(cnt) # 실행문 3

cnt1 = 0
cntsum = 0    
for k in a:
    cntsum += 1
    if k >= 90 and k <= 106: # 90<= k <= 106: 가능
        cnt1 += 1
        
print(cnt1/cntsum)

#%% 예제1. emp3.csw 를 파이썬을 이용해서 판다스의 데이터 프레임으로 만드시오!
# 지금 까페에 올린 emp3.csw 와 dept3.csw 를 c 드라이브 밑에 data 라는 폴더를 만들고
# 그 밑에 복사해 둡니다.

# 윈도우 탐색기window 키 + e

import pandas as pd # 판다스 모듈을 현 코드에서 사용하겠다고 해줌

emp = pd.read_csv("c:\\data\\emp3.csv") # c 드라이브 밑에 emp3.csw를
print (emp)                             #를 읽어서 emp 변수에 넣는다.


"""
설명: 판다스의 read_csv 함수는 os 의 csv 파일을 읽어서 파이썬에서 
	판다스 데이터 프레임으로 만들겠다.

SQL---> 데이터에서 정보를 얻어내기 위해서 ( 데이터 검색 )
파이썬의 판다스 ---> 데이터를 검색하는 모듈 """

#%%

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','sal'] ] )

# 설명: 데이터프레임명[ ['컬럼명1', '컬럼명2'] ]

#%%문제77. 아래의 SQL을 판다스로 구현하시오 !

#sql> select ename, sal, job, hiredate
#	  from emp;
	
#판다스:
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp[['ename', 'sal', 'job', 'hiredate'] ] )

#%%문제78. 아래의 SQL 을 판다스로 구현하시오 !

# SQL> select ename, sal
#		from emp
#		where job='SALESMAN';
		
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','sal'] ] [ emp['job']=='SALESMAN' ]  )

#%%문제79. 월급이 3000 이상인 사원들의 이름과 월급을 출력하시오! 
#           SQL과 판다스 둘다 해보시오!

#   SQL > select ename, sal
#      		from emp
#       		where sal >= 3000;

# 판다스:

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','sal'] ] [ emp['sal']>=3000 ]  )

#%%문제80. 아래의 SQL을 판다스로 구현하시오 !

# SQL> select ename, sal
# 	  from emp
# 	  where sal between 1000 and 3000;

# 판다스 >
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','sal'] ] [ emp['sal'].between(1000,3000) ]  )

#%%문제81. 월급이 1000에서 3000 사이가 아닌 사원들의 이름과 월급을 출력하시오!

# SQL> select ename, sal
# 	   from emp
# 	   where sal < 1000 or sal > 3000;
# 	   where sal not between 1000 and 3000;
# 판다스:
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','sal'] ] [ ~emp['sal'].between(1000,3000) ]  )

#%%문제82. 직업이 CLERK, SALESMAN 인 사원들의 이름과 직업을 출력하시오!

# SQL> select ename, job
# 	  from emp
# 	  where job in ('CLERK', 'SALESMAN');
# 	
# 판다스:
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','sal'] ] [ emp['job'].isin(['CLERK', 'SALESMAN']) ] ) 

#%%문제83. 이번에는 직업이 CLERK, SALESMAN 이 아닌 사원들의 이름과 직업을 출력하시오 !
	 

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','sal'] ] [ ~emp['sal'].isin(['CLERK', 'SALESMAN']) ] )

#%%문제84. 커미션이 null 인 사원들의 이름과 커미션을 출력하시오!
# SQL> select ename, comm
# 	  from emp
# 	  where comm is null;

# 판다스>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','comm'] ] [ emp['comm'].isnull() ] ) 

# NaN 은 Null 값이다.

#%%문제85. 커미션이 null이 아닌 사원들의 이름과 커미션을 출력하시오 !

# SQL> select ename, comm
# 	   from emp
# 	   where comm is not null; 

# 판다스:
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print ( emp[ ['ename','comm'] ] [ ~emp['comm'].isnull() ] ) 

#%% 마지막 문제

import random as r

box = [ '정상', '정상', '정상', '정상', '불량', '불량' ]

cnt = 0
cnts = 0
for i in range(100000):
    cnts += 1
    a =[ ]
    for i in range(3):        # 3개를 뽑아서
        result = r.choice(box)
        a.append(result)
    if a == ['정상', '정상', '정상']: # 모두 정상일 사건 
        cnt += 1
print(1-(cnt/cnts)) # 1- 사건의 확률 = 여사건의 확률


import random as r

box = [ '정상', '정상', '정상', '정상', '불량', '불량' ]

cnt = 0
cnts = 0
for i in range(100000):
    cnts += 1
    a =[ ]
    for i in range(1,4):        
        result = r.choice(box)
        a.append(result)
    if a == ['정상', '정상', '정상']: 
        cnt += 1
print(1-(cnt/cnts))

#%%
#비복원

import random as r

box = [ '정상', '정상', '정상', '정상', '불량', '불량' ]

cnt = 0
cnts = 0
for i in range(100000):
    cnts += 1
    for i in range(1,4):        
        a = r.sample(box,3)
    if a == ['정상', '정상', '정상']: 
        cnt += 1
print(1-(cnt/cnts))
#%%
d = r.sample(range(1000),15)
print(d)
#%% 알고리즘 통계 문제 최종안

import random as r

box = [ '정상', '정상', '정상', '정상', '불량', '불량' ]
#복원
cnt = 0
cnts = 0
for i in range(100000):
    cnts += 1
    a1 = r.choice(box)        
    a2 = r.choice(box)
    a3 = r.choice(box)
    if a1==a2==a3=='정상': 
        cnt += 1
print(1-cnt/cnts)
#비복원
cnt = 0
cnts = 0
for i in range(100000):
    cnts += 1
    a = r.sample(box,3)
    if a == ['정상', '정상', '정상']: 
        cnt += 1
print(1-(cnt/cnts))