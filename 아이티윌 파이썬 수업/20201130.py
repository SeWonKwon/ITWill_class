# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:37:56 2020

@author: STU-14
"""

#%%
#복습

for i in range(1,11):
    print(i,'a') # <-- for loop 문의 관할하에 있는 실행영역
print('b')     # <-- for loop 문의 괄할하에 있는 실행 영역이 아닙니다.
                    # for loop 문이 다 끝나고 나면 작동되는 문장.
                    

#%% 문제86. 이름이 SCOTT 인 사원의 이름과 월급을 출력하시오 !

# SQL> select ename, sal
#         from emp
#         where ename = 'SCOTT';


import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp[['ename','sal']][emp['ename']=='SCOTT'])

#%% 시퀀스 자료형 이해하기

a = 'scott'
print (a)

#위의 scott 이라는 문자를 담은 a 변수에서 첫번쨰 요소만 출력

# s c o t t
# 0 1 2 3 4

print( a[0])
print( a[1])


#%%문제87. 위의 scott을 담은 문자형 변수 a에서 알파벳을 o를 출력하시오~
print ( a[2])

#%%문제88.아래의 문자형 변수에서 맨 끝의 철자인 h를 출력하시오 !

b = 'smith'

print ( b[4])
print (b[-1])

#%%문제89. 판다스를 이용해서 emp3.csv 에서 이름을 출력하는데 이름의 첫번쨰만 철자만 출력하시오!

# SQL > select substr(ename,1,1)
#         from emp;

# 판다스:
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']: # emp3.csv에서 ename만 가져와서
    print(i[0]) #ename의 갯수만큼 loop문을 수행하고 그중에 첫 글짜를 출력!
    print(type(i))

print( type(emp['ename'])) # <class 'pandas.core.series.Series'>
                            # Series 는 컬럼이다.
                            
 
# 설명: <class 'str'> 문자형으로 변경해줘야 문자형에서 특정
#     요소를  가져오는 문법을 사용할 수 있습니다.
#     예: a[0]
#     판다스의 <class 'pandas.core.series.Series'>를 문자형으로
#     변경하려면 for loop 문을 이용해서 하나씩 가져오면 됩니다.
#     예: for i in emp['ename']:
#             print(i)
#%%문제90. 판다스를 이용해서 emp3.csv를 가져와서 이름의 끝글자를 출력하시오!

import pandas as pd

emp = pd.read_csv("c\\data\\emp3.csv")
print(emp['ename'])
for i in emp['ename']:
    print(i[-1])
    
#%%문제91. 위의 결과에서 이름도 같이 출력하시오.
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp['ename'])
for i in emp['ename']:
    print(i,i[-1])

#%%문제92. 이름의 첫번째 철자가 S로 시작하는 사원들의 이름을 출력하시오!

# SQL> select ename
        # from emp
        # where ename like 'S%';
        
# 판다스:
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
    if i[0]=='S':
        print(i)
        
        
#%%문제93. 이름의 끝글자가 T로 끝나느 사원들의 이름을 출력하시오!


# SQL> select ename
        # from emp
        # where ename like '%T';
        
# 판다스:
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
    if i[-1]=='T':
        print(i)
        
        
        
        
        
        
        
        
        
#%% drill 의미는? <generator object <genexpr> at 0x000001D84D801DC8>

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print( i for i in emp['ename'])

#%%문제94. 이름이 두번째 철자가 M인 사원의 이름과 월급을 출력하시오

# SQL> select ename, sal
#        from emp
#        where substr(ename,2,1) = 'M';

# 판다스:
    
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

# for i in emp['ename']:
#     for j in emp['sal']:
#        print(i, j)
        
for i in emp['ename']:
    if i[1] == 'M':       
        print ( i )
        
        
#%%예제

a = 'scott'
print ( a[1:3])
# s c o t t
# 0 1 2 3 4 

# 설명: 1번째 자리부터 3미만의 자리까지 요소들을 출력

#%%문제95. 아래의 SQL을 판다스로 구현하시오!

#SQL> select substr(ename,1,3)
#       from emp;

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

for i in emp['ename']:
    print(i[0:3])

# 설명: SQL과 python 은 숫자를 세는 방식이 다르다. 

#%%문제96. 아래의 SQL을 판다스로 구현하시오!

# SQL> select substr(ename,-2,2)
#         from emp;
        
# 판다스:
    
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")

for i in emp['ename']:
    print( i[-2:]) # -2 부터 끝까지 (:) 다음에 아무것도 안넣으면 끝까지라는 의미~
    
#%%문제97. (점심시간 문제) 아래의 SQL을 판다스로 구현하시오!

# SQL> select substr(ename, 2, 3)
#       from emp;
      
      
# 판다스:
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

for i in emp['ename']:
    print(i[3:7])
#%%문제94. drill

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")


i_a = 0
for i in emp['ename']:
    i_a +=1
    j_a = 0
    for j in emp['sal']:
        j_a +=1
        if j_a == i_a:
            if i[1] == 'M':
                print(i, j)
                
#%% 예제 시퀀스 자료 연결 이해하기 (+)

a = 'i love  '
b = 'python'
print(a+b) # i love  python

#%%문제98.아래의 두개의 리스트를 연결하여 출력하시오.

a = [2, 3, 4, 5]
b = [9, 2, 4, 8]

print(a+b)

#%%문제99. 아래의 SQL을 판다스로 구현하시오!

# SQL> select ename || sal
#         from emp;

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

# print(emp['ename']+emp['sal']) 안된다.

for i, k in zip(emp['ename'], emp['sal']) :
    print (i + str(k)) #비교 print (i, k)
    
# 설명: zip 함수를 for loop 문에 사용하게 되면 
# 두개의 범위 데이터를 한번에 받아서 loop 를 수행할수 있습니다.
# str 함수를 사용한 이유는 문자형 + 문자형을 연결이 가능한데
#문자형 + 숫자형은 연결이 안됩니다. 그래서 숫자형을
#문자형으로 변환하기 위해서 str 함수를 사용했습니다.

#%%예제.

print('a'*7)

print([1,2,3]*5+[2,2,2])

#%%문제100. 주사위의 눈 6개를 100개 담은 리스트 dice 100을 만들고 dice100 리스트를 출력하시오!

a = [1,2,3,4,5,6]
dice100 = a*100

print (dice100)
print(len(dice100))

#%%문제101. 초등학생 키가 10개가 들어 있는 아래의 tall리스트의 요소
# 10개를 10000개로 증가시켜서 tall10000 리스트에 담고 출력하시오

tall = [ 129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
print(len(tall))
tall10000 = tall*1000
print(tall10000)

print(len(tall10000))

#%%문제102. 위의 모집단의 평균값, 분산, 표준편차를 출력하시오!
    # (numpy를 사용하세요~~)
tall = [ 129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
print(len(tall))
tall10000 = tall*10000
print(tall10000)

print(len(tall10000))

import numpy as np

print(np.mean(tall10000)) #136.66
print(np.var(tall10000))  #23.782399999999985
print(np.std(tall10000))  #4.876720209321013

print(type(tall10000))   # <class 'list'>

#%%문제103. 위의 모집단 tall10000에서 표본을 20개를 랜덤으로 추출하시오!

import random as r

tall = [ 129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000
a = []
for i in range(20):
    result = r.choice(tall10000)
    print(result)
        
#%%문제104. 위의 랜덤으로 추출한 표본 20개를 비어있는 a 리스트에 담으시오!

import random as r

tall = [ 129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000

a = []
for i in range(20):
    result = r.choice(tall10000)
    a.append(result)
    
print(a)


#%% 비교!! 문제104
import random as r

tall = [ 129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000

a = []
for i in range(20):
    print(r.choice(tall10000))
    a.append(r.choice(tall10000))
    
print(a)

#%%문제105. 위의 표본의 평균값을 출력하시오!

import random as r
import numpy as np

tall = [ 129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000

a = []
for i in range(20):
    result = r.choice(tall10000)
    a.append(result)
    
print(a)
print(np.mean(a)) # 모집단이랑 비슷허넹
print(np.var(a))

#%%예제

a = 'scott'
print (len(a)) #5

b = [2,3,4,5,1]
print( len(b)) # 리스트의 요소의 갯수가 출력됩니다.

#%%문제106. 아래의 SQL을 판다스로 구현하시오!

# SQL> select ename, length(ename)
#         from emp;
        
# 판다스:
    
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

for i in emp['ename']:
    print(i, len(i))

#%%예제

listdata = [1,2,3,4]

a = 5 in listdata
b = 4 in listdata

print(a)
print(b)


#%%문제107. 모평균이 30이고 모표준편차가 7인 모집단을 구성하시오!
import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg
print(mogipdan) 

print(len(mogipdan))
print(np.std(mogipdan))
print(np.mean(mogipdan))

#%%문제108. 위의 모집단의 모평균을 출력하시오!

import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg
print(mogipdan) 
a = 0
cnt = 0
for i in mogipdan:
    a += i
    cnt += 1

print(a/cnt)

#%%문제109. 아래의 SQL을 판다스로 구현하시오!

# SQL> select ename, job
#         from emp
#         where job in ('SALESMAN','ANALYST');
        
# 판다스:
    
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

print(emp[['ename','job']][emp['job'].isin(['SALESMAN','ANALYST'] )])

#%%문제110. 아래의 SQL을 판다스로 구현하시오!

# SQL> select ename, job
#         from emp
#         where job not in ('SALESMAN','ANALYST');

# Pandas>

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp[['ename','job']][~emp['job'].isin(['SALESMAN','ANALYST'])])

#%%예제

a = "My son's name is John"
print(a)

#문자에 아래와 같이 더블 쿼테이션 마크가 있으면 위의 세번째인 
#""" """ 더블 3개를 사용하면 됩니다.

b = """My son's name is "jone" """
print(b)

#%%문제111. 아래와 같은 글씨가 출력되게 하시오!

#"모집단"의 모평균은 
#"모집단"의 모분산은
#"모집단"의 모표준편차는

a ='"모집단"의 모평균은' 
b ='"모집단"의 모분산은'
c ='"모집단"의 모표준편차는'

print(a)
print(b)
print(c)

#%% 문제112. 모평균이 30이고 모표준편차가 7인 모집단 1000000개의 모평균과 모분산과
#모표준편차를 아래와 같이 출력하시오!

#"모집단"의 모평균은 30
#"모집단"의 모분산은 49
#"모집단"의 모표준편차는 7
import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg

a_1 = np.mean(mogipdan)
b_1 = np.var(mogipdan)
c_1 = np.std(mogipdan)

a ='"모집단"의 모평균은 ' 
b ='"모집단"의 모분산은 '
c ='"모집단"의 모표준편차는 ' 

print(a+str(a_1))
print(b+str(b_1))
print(c+str(c_1))

print(a, np.mean(mogipdan))
print(b, np.var(mogipdan))
print(c, np.std(mogipdan))

#%%문제 113 모평균이 30이고 모표준편차가 7인 모집단(10000000) 에서 표본을
#49개를 뽑으시오

import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg

print(r.choice(mogipdan))
print(np.random.choice(mogipdan,49))


#%%문제114 위에서 뽑은 49개의 평균값을 출력하시오 !
 

import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg

# print(np.mean(np.random.choice(mogipdan,49)))
print(np.random.choice(mogipdan,49).mean())

# numpy의 random 안의 choice 함수를 이용해서 mogipdan에서 49개를 표본 샘플링하고 그 표본의 평균 값을 출력한다.




#%%문제115. 위에서 출력한 표본의 평균값을 하나가 아니라 100개가 출력되게 하시오!


import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg

for i in range(100):
    print(np.random.choice(mogipdan,49).mean())
    
#%%문제116. 이번에는 100개를 출력하지 말고 비어있는 리스트 a를 선언하고 a에 100개를 담으시오!
import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg
a =[]
for i in range(100):
    a.append(np.random.choice(mogipdan,49).mean())

#%%문제117. 위에서 구한 표본평균의 평균값과 표준편차를 아래와 같이 출력하시오!

    # "표본 평균" 의 평균값은 ?
    # "표본 평균" 의 표준편차는 ?
    

import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg
a =[]
for i in range(100):
    a.append(np.random.choice(mogipdan,49).mean())   

aa = '"표준편차" 의 평균값은 '
ab = '"표본평균" 의 표준편차는 '
print(aa, np.mean(a))
print(ab, np.std(a))

#%%예제:
    

txt1 = '자바'
txt2 = '파이썬'

print ('나는 %s 보다 %s 에 더 익숙합니다.' %(txt1,txt2))
print ('나는', txt1, '보다', txt2, '에 더 익숙합니다.')


#%%문제118 아래의 변수를 이용해서 아래와 같이 결과가 출력되게 하시오!

# 결과: 5는 10보다 작습니다. 

num1 = 5

num2 = 10

print( '%d는 %d 보다 작습니다.' %(num1,num2) )

#%% 문제119. 문제117번의 결과가 아래와 같이 출력되게 하시오!
    #(문자열 포멧을 이용하세요)

# 표본평균의 평균값은 29.324235235 이고 분산값은 1.23423423523
# 이고 표준편차는 1.23423523523 입니다.


import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg
a =[]
for i in range(100):
    a.append(np.random.choice(mogipdan,49).mean())   

aa = '"표준편차" 의 평균값은 '
ab = '"표본평균" 의 표준편차는 '


m = np.mean(a)
std =  np.std(a)
var = np.var(a)

print ('표본평균의 평균값은 %f 이고 분산값은 %f 이고 표준편차는 %f 입니다.' %(m,var,std))
#%%문제120. 위의 결과가 아래와 같이 소수점 2번째 자리까지만 나오게 하시오!

import numpy as np
avg = 30
std = 7
N = 1000000

mogipdan = np.random.randn(N)*std + avg
a =[]
for i in range(100):
    a.append(np.random.choice(mogipdan,49).mean())   

aa = '"표준편차" 의 평균값은 '
ab = '"표본평균" 의 표준편차는 '


m = round(np.mean(a),2)
std =  round(np.std(a),2)
var = round(np.var(a),2)

print ('표본평균의 평균값은 %.2f 이고 분산값은 %.2f 이고 표준편차는 %.2f 입니다.' %(m,var,std))

#%% ( 마지막 문제 )문제121. (통계를 코드로 구현)

import numpy as np
avg = 18
std = 3
N = 100000
mo = np.random.randn(N)*std + avg
cnts = 0
cnt = 0
for i in range(10000):
    result = np.random.choice(mo,36).mean()
    cnts += 1
    if result >= 17 :
        cnt += 1
            
print(cnt/cnts)



































