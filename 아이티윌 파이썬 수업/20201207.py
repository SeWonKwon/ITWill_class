# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:09:04 2020

@author: bigne
"""

#%%판다스 조인 복습

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge( emp,dept, on = 'deptno',how = 'right')
print( result[['ename','loc']])

# 14     NaN    BOSTON

#%%문제221. 부서번호, 부서번호별 평균월급을 출력하시오!

# SQL>> select deptno, avg(sal)
#         from emp
#         group by deptno;
        
# pandas>> 
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['sal'].mean().reset_index()
print(result)

# 설명: groupby 부터 시작해서 reset_index() 까지가 한 세트이므로 항상
# 같이 사용하면 됩니다.

#%%문제 222. 위의 결과에서 평균월급을 출력할 때 정수부분만 출력하고 싶다면
    #(소수점 이전만 출력)

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['sal'].mean().reset_index().astype(int                                                                  )
print(result)

# astype(int)는 출력되는 데이터에서 정수부분만 취해라라는 뜻입니다.
# 정수형으로 변환해라 ~ 라는 뜻입니다. float, str

#%%문제223. 직업과 직업별 토탈월급을 출력하시오!

# SQL> select job, sum(sal)
#         from emp
#         group by job;
        
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('job')['sal'].sum().reset_index()
print(result)

#%%문제224. 부서위치, 부서위치별 토탈월급을 출력하시오!
# SQL> select d.loc, sum(e.sal)
#        from emp e, dept d
#        where e.deptno = d.deptno
#        group by d.loc;
       
# Pandas>

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result1 = pd.merge(emp,dept,on ='deptno') # 조인하고 그룹나누고~
result2 = result1.groupby('loc')['sal'].sum().reset_index()
print(result2)

#%%문제223. 아래의 SQL을 판다스로 구현하시오!
# SQL > select d.loc, nvl(sum(e.sal),0)
#        from emp e, dept d
#        where e.deptno (+) = d.deptno
#        group by d.loc;

# pandas>

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result1 = pd.merge(emp,dept,on ='deptno',how='right') # 조인하고 그룹나누고~
result2 = result1.groupby('loc')['sal'].sum().reset_index()
print(result2)

#%%문제226. 아래의 SQL을 판다스로 구현하시오!
# SQL> select deptno, count(*)
#         from emp
#         group by deptno;

# Pandas>

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['empno'].count().reset_index()
# result = pd.groupby('deptno')['empno'].count().reset_index()
print(result)

#%%문제227. emp122.csv를 다운 받고 판다스 데이터 프레임으로 만들고 출력하시오!

import pandas as pd

emp12 = pd.read_csv("c:\\data\\emp122.csv")
print(emp12)

#%%문제228. 통신사, 통신사별 인원수를 출력하시오!

import pandas as pd

emp12 = pd.read_csv("c:\\data\\emp122.csv")
result = emp12.groupby('TELECOM')['INDEX'].count().reset_index()
print(result)

#%%문제229. 우리반 테이블에서 통신사가 kt 이고 나이가 
# 30살 이상인 한생들의 이름과 나이와 통신사를 출력하시오!

import pandas as pd

emp12 = pd.read_csv("c:\\data\\emp122.csv")
result = emp12[['ENAME','AGE','TELECOM']][emp12['AGE']>=30]
result2 = result[['ENAME','AGE','TELECOM']][result['TELECOM']=='kt']
print(result2)


#%%문제229번 정답
import pandas as pd

emp12 = pd.read_csv("c:\\data\\emp122.csv")
result = emp12[['ENAME','AGE','TELECOM']][(emp12['AGE']>=30)&(emp12['TELECOM']=='kt')]
print(result)   

# 설명: & : and , | : or

#%%

print( round(16.554))  #소수점 첫번째 자리에서 반올림
print( round(16.554,0)) #소수점 첫번쨰 자리에서 반올림
print( round(16.554,1)) #소수점 두번째 자리에서 반올림
print( round(16.554,2)) #소수점 세번째 자리에서 반올림

# * 파이썬에서 반올림 할때 중요하게 알아야 할 내용

print( round(142.5) ) # 143으로 예상했느데 142가 나온다.
# " R과 파이썬은 짝수를 좋아합니다." 
print( round(187.5))  # 188

# 가까운 짝수로 변한다. 2    2.5   3 --> 2 // 7  7.5  8 --> 8 짝수!!

#%%예제. 판다스를 이용하지 않고 파이썬으로만 emp3.csv에서 이름과 우러급을
# 출력하시오!

import csv

file = open("c:\\data\\emp2.csv") # os에 있는 emp2.csv를 읽어서
                                  # file 이라는 변수에 넣는다.

emp_csv = csv.reader(file) # file 변수에 있는 csv 파일을 읽어서 emp_csv
                           # 변수에 넣는다.

print(emp_csv)  # 이 상태에서 그냥 프린트 하면 메모리가 주소만 나옵니다.

# for emp_list in emp_csv:
#     print(emp_list)

for i in emp_csv:
    print(i[1], i[5])

# 판다스용 csv와 판다스를 이용하지 않는 csv의 차이점은 컬럼과 인덱스의 유무이다.
#%%문제230. 판다스를 이용하지 말고 이름과 월급*12.3를 출력하시오
import csv

file = open("c:\\data\\emp2.csv") 
emp_csv = csv.reader(file)

for i in emp_csv:
    print(i[1], int(i[5])*12.3)

#%%문제231. 위의 결과를 다시 출력하는데 첫번째 자리에서 반올림되게 하시오!

import csv

file = open("c:\\data\\emp2.csv") 
emp_csv = csv.reader(file)

for i in emp_csv:
    print(i[1], round(int(i[5])*12.3))
    
#%%문제232. 직업이 SALESMAN 인 사원들의 이름과 직업을 출력하는데
#           판다스 이용하지 말고 emp2.csv 을 읽어서 출력하시오!

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    if i[2] == 'SALESMAN':
        print(i[1],i[2])
        
#%%(점심시간 문제) 부서번호가 20번인 사원들의 이름과 월급과 부서번호를 출력하시오~

# 판다스를 이용하는 법:
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp[['ename','sal','deptno']][emp['deptno']==20]
print(result)
#%%
# 판다스를 이용하지 않는 방법:
import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    if i[7]=='20':
        print(i[1],i[5],i[7])

#%%

print(int(-5.4)) # -5

# 문제234. 판다스를 이용해서 emp3.csv 를 읽어다가 이름과 월급을 출력하는데
# 월급을 출력할때 소수점 이하는 버리고 정수부분만 출력되게 하시오!

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp[['ename','sal']])

# 설명: int() 함수를 따로 안써도 정수형으로 출력되고 있습니다.
#      판다스를 이용하지 않았을때와는 다르게 숫자는 바로 숫자형으로 출력해주고 있습니다.

#%%float

print(float(10)) # 10.0

#문제235. 판다스를 이용해서 이름과 월급을 출력하는데 월급을 출력할때
#실수형으로 출력하시오.

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

emp['sal'] = emp['sal'].apply(float) # emp 데이터 프레임의 sal 컬럼의 
                                     # 데이터를 float(실수형) 로 변환해서 
#바꿔치기 가능!!                      # emp 데이터 프레임에 sal 컬럼의 데이터로 변경해라~
print(emp['sal'])
print(emp[['ename','sal']])

#설명: emp['sal'].apply 는 emp 데이터 프레임에 sal 시리즈에 apply 함수를
#      적용해서 데이터 유형을 변경할 수 있습니다.
#      emp['sal'].apply(float) 이렇게 하면 데이터 유형을 실수형으로 변경하는 것입니다.

#%%filter

#예제: 숫자가 나열되어있는 리스트에서 짝수만 추출해내는 코드를 작성

a = [ 1,2,3,4,5,6,7,8,9,10]

# 1. 숫자를 입력하면 짝수이면 결과를 출력하고 홀수면 출력하지 않는 함수를 생성

def get_even(num):
    if num%2 == 0:
        return num
    else:
        return # 리턴 다음에 default 값은 아무것도 리턴 되지 않습니다.

print(get_even(7))
print(get_even(2))

result = filter(get_even,a) # filter( 함수이름, 리스트 이름)

print(result) # <filter object at 0x0000020ACE16D820>

print( list(result) )

#%%문제236. 아래의 리스트에서 숫자가 300이상이면 출력하고
#  300미만이면 출력되지 않게 하시오!

b = [ 100,352,254,456,123,234,567,903]

def over_300(num):
    if num>=300:
         return num
    else:
        return
    
print(list(filter(over_300,b)))

#%% 문제237. 우리반 데이터에서 나이가 30살 이상인 나이만 따로 결과로 리스트로 출력하시오!

import pandas as pd

emp122 = pd.read_csv("c:\\data\\emp122.csv")

a = []
for i in emp122['AGE']:
    if i >= 30:
        a.append(i)

print(a)


#%%

a = [ 8,7,12,55,21,34,15,9,22]
print(max(a))

#%%문제238. 사원 테이블에서 최대월급을 출력하시오! emp3.csv

# 1. 판다스를 이용했을때
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp['sal'].max()
print(result)

# max(),min(),mean(),sum()

# 2. 판다스를 이용하지 않았을때

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

a = []
for i in emp:
    a.append(int(i[5])) # str 형으로 불러 오기때문에 int를 써준다.

print(a)
print(max(a))

#%%
#문제239. 우리반 데이터(emp122.csv)에서 최소나이를 출력하시오!

# 1. 판다스 이용했을때
import pandas as pd

emp122 = pd.read_csv("c:\\data\\emp122.csv")
result = emp122['AGE'].min()
print(result)
#%%
# 2. 판다스 이용하지 않았을때

#emp122.csv 를 복사해서 emp1222.csv로 붙여 넣는다. 컬럼명을 날린다.
#UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 3: illegal multibyte sequence
#인코딩을 ANSI와 UTF-8 등으로 바꿔준다.
import csv

file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)

a = []
for i in emp:
    a.append(int(i[2]))
print(a)

#%% NaN 예: 판다스를 이용해서 이름과 커미션을 출력하시오!

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp[['ename','comm']])

#문제240. 커미션이 결측치(NaN)인 사원들의 이름과 커미션을 출력하시오.
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp[['ename','comm']][emp['comm'].isnull()])

#%%문제241. 커미션이 결측치(NaN)이 아닌 사원들의 이름과 커미션을 출력하시오!
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
print( emp[['ename','comm']][~emp['comm'].isnull()])

# * 데이터 받았으면 데이터 분석을 하기 전에 데이터 전처리를 해야하는데
#   전처리중에서 결측치 확인하는 단계가 있습니다.

#%%문제242. emp3.csv 에 결측치가 있는지 확인하는 방법?

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")

print(emp.isnull())

#%%문제243. 결측치를 한눈에 보는 방법을 확인하시오.

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")

print(emp.isnull().sum())

# 설명: 결측치가 있으면 제대로 된 대이터 분석하기가 어렵고
# 머신러닝을 이용한 데이터 분석인 경우 좋은(정확도가 높은)
# 머신러닝 모델이 나오기 어렵습니다. 결측치를 처리를 해줘야 합니다.

#%%문제244. 타이타닉 데이터에 결측치가 어느 컬럼에 많은지 확인하시오!

import pandas as pd

ta = pd.read_csv("c:\\data\\train.csv")

print(ta.isnull().sum())

#%%emp 데이터 프레임에 sal의 데이터와 똑같은 데이터로 sal2 라는 컬럼을 추가하려면?

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")

emp['sal2'] =emp['sal']
# emp 데이터 프레임에 sal2 컬럼을 추가하는데 
# 데이터는 emp 데이터 프레임에 sal로 하시오.
print(emp)

#%%문제245. 판다스를 이용해서 이름과 부서위치를 출력하시오!
    # (emp3.csv와 dept3.csvf를 이용해서 조인하세요)

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")

result = pd.merge(emp,dept,on='deptno',how='inner')
print( result[['ename','loc']])

#%%문제246. emp데이터 프레임에 loc컬럼을 추가하고 해당 사원의 부서위치로 값을 갱신하시오!

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")

result = pd.merge(emp,dept,on='deptno',how='inner')
emp['loc'] = result['loc'] # emp 데이터프레임에 loc컬럼 추가하면서
                            # result 의 loc 로 값을 갱신합니다.
print(emp)
print( emp[['ename','loc']])

#설명 : 파생변수를 왜 추가를 하냐면?
     # emp 테이블에서 퇴사할것 같은 사원이 누구인지 예측하시오!
     # 머신러닝을 이용해서 예측을 하면 됩니다.
     # 머신러닝이 예측을 잘하려면 좋은 데이터를 주고 학습시켜야 합니다.
     # 자기의 월급이 자기가 속한 직업의 평균월급보다 
     # 더 작은 월급을 받는 사원이면 퇴사할 가능성이 높다.
     # 직업별 평균월급이 emp 데이터 프레임에 추가 되어 있으면
     # 머신러닝이 예측하기 좋은 데이터가 추가가 된것입니다.
     
#%%문제247. 직업, 직업별 평균 월급을 판다스로 출력하시오!

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('job')['sal'].mean().reset_index()
print(result)
result['sal'] = result['sal'].astype(int)
# result 데이터 프레임에 sal을 정수형으로 변환해서 result 데이터 프레임에 sal에 반영하겠다.
print(result)

#%%문제248. emp 와 result를 서로 조인해서 조인된 전체 데이터 프레임을 출력하시오.

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('job')['sal'].mean().reset_index()
result['sal'] = result['sal'].astype(int)

result2 = pd.merge(emp, result, how='inner',on='job')
print(result2)

# 설명: emp에도 sal이 있고 result 에도 sal 이 있어서 
# emp의 sal은 컬렴명이 sal_x로 변경되었고 
# result 의 sal으s sal_y(해당 직업의 평균월급)로 변경되었습니다.

#%%문제249. emp 데이터 프레임에 컬럼을 하나 추가하는데 
# job_avgsal로 추가하고 문제248번에서 구한 직업별 
# 평균월급인 result2['sal_y'] 의 값으로 값을 갱신하시오!

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('job')['sal'].mean().reset_index()
result['sal'] = result['sal'].astype(int)

result2 = pd.merge(emp, result, how='inner',on='job')
emp['job_avgsal'] = result2['sal_y']
print(emp)

#설명: 현업에서 머신러닝 데이터 분석가들이 하는 일중
# 상당수가 바로 이런 파생변수를 추가하는 작업니다.
# 좋은 파생변수를 추가해야 머신러닝이 예측을 잘 할수 있습니다.
# 예를 들어 : 게임회사에서 어떻게 응용하냐면 그 게임을 이탈될것 
# 같은 유져를 머신러닝으로 찾아서 형평성에 어긋나지 않도록하면서
# 그 유져가 인식하지 못하도록 조용히 혜택을 준다.

#%%문제250. emp 데이터 프레임에 해당 사원이 근무하는
# 부서번호의 평균월급을 sal_avg 라는 이름으로 파생변수를 생성하시오!
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['sal'].mean().reset_index()
result['sal'] = result['sal'].astype(int)
print(result)
result2 = pd.merge(emp, result, how='inner',on='deptno')
emp['sal_avg'] = result2['sal_y']
print(emp)

#%%문제251. 이름과 월급을 출력하는데 (판다스로) 월급이 높은 사원부터 출력하시오!

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.sort_values('sal',ascending =False)
print(result)
#설명: 판다스를 사용할 때 데이터를 정렬하려면 위와 같이
# sort_values 함수를 이용하면 됩니다.

# ascending = True : 낮은값에서 높은값으로
# ascending = False : 높은값에서 낮은값 순으로

#%%문제252. (오늘의 마지막 문제) 아래의 SQL을 판다스로 구현하시오!

# SQL> select job,sum(sal)
#       from emp
#       group by job
#       having sum(sal) >= 6000
#       order by sum(sal) desc;
      
# Pandas>

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")

emp_j = emp.groupby('job')['sal'].sum().reset_index()
emp_j2s = emp_j[['job','sal']][emp_j['sal']>=6000].sort_values('sal',ascending=False)
print(emp_j2s)

#%%
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
emp_j = emp.groupby('job')['sal'].sum().reset_index().sort_values('sal',ascending=False)
print(emp_j[['job','sal']][emp_j['sal']>=6000])

#%%

import pandas as pd

 

emp = pd.read_csv("c:\\data\\emp3.csv")

result = emp.groupby('job')['sal'].sum().reset_index()

result2 = result [result['sal'] >= 6000]

result3 = result2.sort_values('sal', ascending = False)

 

print(result3)
















