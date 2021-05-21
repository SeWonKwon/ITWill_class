# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:36:25 2020

@author: STU-14
"""

#%% 예제

try: 
    x = int ( input('분자의 숫자를 입력하시오'))
    y = int ( input('분모의 숫자를 입력하시오'))
    print(x/y)
except:
    print('잘못된 값으로 나누기를 시도하셨습니다.')

 # 설명: 위의 경우에는 분모값을 입력할 때 숫자 0을 입력했을때와
# 문자 a 를 입력했을때 똑같이 '잘못된 값을 입력하셔서 나누기를 시도하셨습니다'가
# 출력되게 했는데 좀더 구체화 해서 분모값으로 0을 입력하면 0으로 나눌 수 없습니다. 나오게하고
# 분모값으로 a 를 입력하면 잘못된 값을 입력하셨습니다 가 나오게 하고 싶다면?


#%%

try: 
    x = int ( input('분자의 숫자를 입력하시오'))
    y = int ( input('분모의 숫자를 입력하시오'))
    print(x/y)
except ZeroDivisionError: # 파이썬 싸이트에서 예외처리에서 알아 볼수 있다.
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자를 입력하라고!')
    
#%% 문제191. 숫자를 물어보게하고 숫자를 입력하면 해당 숫자만큼 
#1번부터 출력되게 하는 코드를 작성하시오!  

n = int(input('숫자를 입력하세요'))

for i in range(1,n+1):
    print(i)   

#%% 문제192. 위의 코드에 예외처리를 해서 숫자를 물어볼때 문자를 입력하면 잘못된 값을 입력하셨습니다.
#    라고 메세지가 출력되게하시오.

try:
    n = int(input('숫자를 입력하세요'))
    for i in range(1,n+1):
        print(i)       
except:
    print('잘못된 값을 입력하셨습니다.')    
#%%    
# 잘못된 값을 입력하셨습니다. 말고도 정확한 에러에 대한 원인을 
# 파악을 하고 싶다면 아래와 같이 작성하면 됩니다.

try:
    n = int(input('숫자를 입력하세요'))
    for i in range(1,n+1):
        print(i)       
except Exception as e:          
    print('잘못된 값을 입력하셨습니다.')   
    print(e)
    
    
#%%문제193. 판다스를 이용해서 emp3.csv의 데이터를 로드하는데 이름을
    # 물어보게 하고 이름을 입력하면 해당 사원의 이름과 월급이 출력되게하시오!

import pandas as pd

name = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['ename']==name.upper()])

#%%
import pandas as pd

name = input('이름을 입력하세요~').upper()
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['ename']==name])

#%%문제194. 위의 결과에서 월급만 출력하시오

import pandas as pd

name = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp['sal'][emp['ename']==name.upper()]
print(result)
print(type(result)) #<class 'pandas.core.series.Series'>

# 3000 <-- 필드값 딱 필드값만 보고싶다!  
result = emp['sal'][emp['ename']==name.upper()].values[0]
print(result)
print(type(result))
#%%문제195. 위의 코드에 사용자 저의 예외처리를 해서 월급이 고소득자는 해당사원의 월급을 볼수 없습니다.
# 라는 메세지가 출력되게 하시오.   (3000 이상인 사원들을 고소득자로 보고 작성하시오.)

import pandas as pd

name = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp['sal'][emp['ename']==name.upper()].values[0]
if result >= 3000:
    raise Exception('해당 사원의 월급은 볼 수 없습니다.')
print(emp[['ename','sal']][emp['ename']==name.upper()])
#%% continue 나 break 나 다른것과 비교해봐~

import pandas as pd

name = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp['sal'][emp['ename']==name.upper()].values[0]
if result >= 3000:
    continue
    print('해당 사원의 월급은 볼 수 없습니다.')
print(emp[['ename','sal']][emp['ename']==name.upper()])

#%%   
# 문제196. 위의 코드를 수정해서 이름을 물어보게 하고 이름과 직업을 출력하는
# 코드로 작성하는데  직업이 SALESMAN 이면 해당 사원의 정보는
# 볼 수 없습니다. 라는 메세지가 출력되면서 
# 프로그램이 종료되게 하시오!    

import pandas as pd

name = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp['job'][emp['ename']==name.upper()].values[0]
if result == 'SALESMAN':
    raise Exception('해당 사원의 월급은 볼 수 없습니다.')
print(emp[['ename','job']][emp['ename']==name.upper()])
    
    
    
#%% 문제197. 아래처럼 사원 이름을 물어보게하고 사원이름을 입력하면
# 해당 사원의 이름과 월급이 출력되게하시오!

import pandas as pd
try:
    name = input('사원 이름을 입력하세요~')    
    emp = pd.read_csv('c:\\data\\emp3.csv')
    print(emp[['ename','job']][emp['ename']==name.upper()])    
except LookupError:
    print( ' 해당 사원은 없습니다.' )    
    
    
#%%문제198.

import pandas as pd
try:
    name = input('사원 이름을 입력하세요~')    
    emp = pd.read_csv('c:\\data\\emp3.csv')
    result = emp['ename'][emp['ename']==name.upper()].values[0]
    print(emp[['ename','job']][emp['ename']==result])    
except LookupError:
    print( ' 해당 사원은 없습니다.' )    

# 설명: result = emp['ename'][emp['ename']==name.upper()].values[0]    
#       이 코드에서 values[0]을 사용하면 Series(컬럼) 가 아니라 값으로 출력이 되어서 result 에 담기게 됩니다.
#       없는 사원이름을 입력하면 result 에 값이 입력되지 않게 되므로 LookupError 예외처리가 되어서 해당사원은 없습니다.
    
#%%문제199. (점심시간 문제) 직업을 물어보게하고 직업을 입력하면 해당사원의 이름과 직업과 월급이 출력되게 하는 코드를 작성하는데
# 없는 직업을 입력하면 해당 직업은 사원 테이블에 없습니다. 라는 메세지가 출력되게 하시오.

# 직업을 입력하세요~

# 해당 직업은 사원 테이블에 없습니다.

import pandas as pd

try:
    name = input('직업을 입력하세요~')
    emp = pd.read_csv('c:\\data\\emp3.csv')
    job = emp['job'][emp['job']==name.upper()].values[0]
    print(emp[['ename','job','sal']][emp['job']==job])
except LookupError :  
    print('해당 직업은 사원 테이블에 없습니다.')
   
#%%자료형 확인하기

numdata = 57
print( type(numdata) ) # <class 'int'>

numdata2 = 27.2
print( type(numdata2) ) # <class 'float'>

strdata = '파이썬'
print ( type(strdata) ) # <class 'str'>

a = [1,2,3,4]
print ( type(a) ) # <class 'list'>

a = (1,2,3,4)
print ( type(a) ) # <class 'tuple'>

#%%문제200. 딕셔너리 자료형을 만들고 위와같이 type을 확인하시오!

a = {'a':'ㅏ','o':'ㅗ'}  
print(type(a)) # <class 'dict'>
    
#설명: 리스트[],튜플(),딕셔너리{}

#%%나머지만 구하기(%)

print(12%3) # 0
print(12%5) # 2

#%%문제201. 아래와 같이 두개의 숫자를 각각 물어보게하고 아래의 메세지가 출력되게 하시오!

# 첫번째 숫자를 입력하세요~ 1113
# 두번쨰 숫자를 입력하세요~ 23

# 1113을 23으로 나누면 9가 나머지로 남습니다.

a = int(input('첫번째 숫자를 입력하세요'))
b = int(input('두번째 숫자를 입력하세요'))
c = a%b

print('%d을 %d로 나누면 %d가 남습니다.' %(a,b,c))    
#설명: string formatting : %s문자,%c기호,%f실수,%d정수

#%%몫과 나머지 구하기

result1, result2 = divmod(1113,23)
 # 몫     나머지
print(result1,result2)
# divmod 함수가 출력하는 값이 2개여서 변수가 2개 필요하다.    
print(divmod(1113,23))    
print(type(divmod(1113,23)))
result = divmod(1113,23)   
print(result)

c,d=(2,3)
print(d)

#%%
# 문제202. 아래와 같이 실행되게 코드를 수행하시오 !

# 첫번째 숫자를 입력하세요~ 1113
# 두번쨰 숫자를 입력하세요~ 23

# 1113을 23으로 나눈 몫은 48이고 나머지는 9입니다.
# 0으로는 나눌수 없습니다.



try:
    a = int(input('첫번째 숫자를 입력하세요'))
    b = int(input('두번째 숫자를 입력하세요'))
    c = divmod(a,b)   
    print('%d을 %d로 나눈 몫운 %d이고 나머지는 %d입니다.' %(a,b,c[0],c[1]))    
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다.')
except ValueError:
    print('숫자를 입력해주세요~')
except:
    print('다시....')

#%%Pandas Drillllllllllll

#문제203. dept3.csv를 판다스로 로드해서 dept 데이터 프레임 전체를 출력하시오!

import pandas as pd

dept = pd.read_csv('c:\\data\\dept3.csv')
print(dept)
#%%
#문제204. 부서위치가 DALLAS의 부서번호와 부서명(dname)을 출력하시오!

import pandas as pd

dept = pd.read_csv('c:\\data\\dept3.csv')
print(dept[['deptno','dname']][dept['loc']=='DALLAS'])

#%%조인하기 예제

# SQL

# Pandas

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
dept = pd.read_csv('c:\\data\\dept3.csv')
result = pd.merge( emp,dept, on='deptno')

print(result)
print(result[['ename','loc']])

# 설명: emp 데이터 프레임과 dept 데이터 프레임을 조인시키는데
# on = 'deptno'를 이용하여 지정해주면 됩니다.
#%%문제205. DALLAS 에서 근무하는 사원들의 이름과 부서위치를 출력하시오
# SQL>
# select e.ename,d.loc
#  from emp e, dept d
#  where e.deptno = d.deptno
#     and d.loc = 'DALLAS';
    
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
dept = pd.read_csv('c:\\data\\dept3.csv')
result = pd.merge( emp,dept, on='deptno')

print(result[['ename','loc']][result['loc']=='DALLAS'])

#%%문제206.월급이 3000이상인 사원들의 이름과 월급과 부서위치를 출력하시오.
# SQL>
# select e.ename, e.sal, d.loc
#  from emp e, dept d
#  where e.deptno = d.deptno
#     and e.sal >= 3000;
    
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
dept = pd.read_csv('c:\\data\\dept3.csv')
result = pd.merge( emp,dept, on='deptno')

print(result[['ename','sal','loc']][result['sal']>=3000])
#%%문제207. 부서번호가 10번, 20번인 사원들의 이름과 부서위치와 부서번호를 출력하시오.

# SQL>
# select e.ename, d.loc, e.deptno
#  from emp e , dept d
#  where e.deptno = d.deptno
#    and e.deptno in (10,20);
   
# Pandas>

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
dept = pd.read_csv('c:\\data\\dept3.csv')
result = pd.merge(emp,dept, on='deptno')
print(result[['ename','loc','deptno']][result['deptno'].isin([10,20])])

#%%문제208. 월급이 1000에서 3000사이인 사원들의 이름과 월급과 부서위치를 출력하시오!

# SQL>
# select e.ename, e.sal, d.loc
#  from emp e, dept d
#  where e.deptno = d.deptno
#   and e.sal between 1000 and 3000;

# Pandas>

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
dept = pd.read_csv('c:\\data\\dept3.csv')
result = pd.merge(emp,dept, on='deptno')
print(result[['ename','sal','loc']][result['sal'].between(1000,3000)])

#%%문제209. 아래의 SQL을 Pandas 로 구현하시오.
# SQL>
# select e.ename, d.loc
#  from emp e, dept d
#  where e.deptno(+) = d.deptno ;
 
# Pandas> 

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
dept = pd.read_csv('c:\\data\\dept3.csv')
result = pd.merge(emp,dept, on='deptno',how ='right')
print(result[['ename','loc']])

#%%문제210. 아래의 SQL을 Pandas로 구현하시오!
# SQL>
# select e.ename, d.loc
#  from emp e full outher join dept d
#  on (e.deptno = d.deptno);

# Pandas>

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
dept = pd.read_csv('c:\\data\\dept3.csv')
result = pd.merge(emp,dept, on='deptno',how ='outer')
print(result[['ename','loc']])

#%% Pandas를 이용한 서브쿼리
# 예제: JONES 보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하시오.

# SQL> 
# select ename,sal 
#  from emp
#  where sal > ( select sal
#                  from emp
#                  where ename ='JONES');      

# Pandas> 
 
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')

jsal = emp['sal'][emp['ename']=='JONES'].values[0]
#서브쿼리 부분을 변수에 담고 필드값으로(.values[0]변경한다.)
print(emp[['ename','sal']][emp['sal']>jsal]) 
 
#%%문제211. 아래의 서브쿼리를 Pandas로 구현하시오.
# SQL>
# select ename, sal
#   from emp
#   where job = ( select job
#                   from emp
#                   where ename='SCOTT');

# Pandas>
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')

sjob = emp['job'][emp['ename']=='SCOTT'].values[0]
print(emp[['ename','sal']][emp['job']==sjob]) 

#%%문제212. 아래의 서브쿼리의 결과를 Pandas 로 수행하시오!
# SQL> 
# select ename,sal
#  from emp
#  where job = (select job
#                from emp
#                where ename='SCOTT')
#    and ename != 'SCOTT';
   
# Pandas>

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')

sjob = emp['job'][emp['ename']=='SCOTT'].values[0]
print(emp[['ename','sal']][(emp['job']==sjob) & (emp['ename']!= 'SCOTT')]) 

# 설명: 판다스에서 and sms & 이고 or 는 | dlqslek. & 와 | 를 쓸때는 괄호로 묶어줘야 합니다.

#%% drill
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')

sjob = emp['job'][emp['ename']=='SCOTT'].values[0]
for i in emp[['ename','sal']][(emp['job']==sjob) ]:
    # if emp['ename']=='SCOTT':
    #     continue
    print(i[i]) 
    
#%% 오라클과 SQL 구룹함수 비교 6
# SQL>
# select max(sal)
#  from emp;

# Pandas>
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
print( emp['sal'].max())

# 설명: 
#     emp['sal'].max() --> 최대월급
#     emp['sal'].min() --> 최소월급
#     emp['sal'].sum() --> 토탈월급
#     emp['sal'].var() --> 분산
#     emp['sal'].std() --> 표준편차값
#     emp['sal'].mean() --> 평균   
#%%문제213. 아래의 SQL을 판다스로 구현하시오!
# SQL>
# select max(sal)
#  from emp
#  where deptno=20;
 
# Pandas>

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')

print(emp['sal'][emp['deptno']==20].max())

#%%문제214. 아래의 SQL을 판다스로 구현하시오!
# SQL>
# select min(sal)   
#  from emp
#  where job = 'SALESMAN';
 
# Pandas>

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')

print(emp['sal'][emp['job']=='SALESMAN'].min())

#%% 문제215. emp12.csv 를 판다스 데이터 프레임으로 만들어서 출력하시오.

import pandas as pd

emp12 = pd.read_csv("c:\\data\\emp122.csv")
print(emp12)

#%% 문제216. 우리반에서 최소 나이를 출력하시오!

import pandas as pd

emp12 = pd.read_csv("c:\\data\\emp122.csv")
print(emp12['AGE'].min())

#%%문제217. 아래의 SQL을 판다스로 구현하시오!
# SQL>
# select job, max(sal)
#  from emp
#  group by job;

# Pandas>
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv')
result = emp.groupby('job')['sal'].max().reset_index() # reset_index() 키워드 때문에 컬럼이 2개이기때문에 DataFrame으로 출력된다.
# result = emp.groupby('job')['sal'].max() 과 비교해보면 시리즈 형식이고 컬럼명이 나오지 않는다.
print(result)
print(type(result))


#설명: reset_index() 키워드는 Series(컬럼) 로 출력하는게 아니라 DataFrame(테이블) 으로 출력하는 키워드 입니다.

#%%218. 아래의 SQL을 판다스로 구현하시오!

# SQL> 
# select deptno, sum(sal)
#  from emp
#  group by deptno;

# Pandas>
import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv') 
result = emp.groupby('deptno')['sal'].sum().reset_index()
print(result)

#%%문제219. 아래의 SQL을 판다스로 구현하시오!

# SQL> 
# select deptno, sum(sal)
#  from emp
#  where deptno != 20
#  group by deptno;
 
# Pandas>

import pandas as pd
emp = pd.read_csv('c:\\data\\emp3.csv') 
result = emp.groupby('deptno')['sal'].sum().reset_index()
print(result[['deptno','sal']][result['deptno']!=20])

#%%오늘의 마지막 문제) 어제 마지막 문제로 만든 함수를 이용해서 아래와 같이 출력되게 하시오!

import random as r

coin = ['앞','뒤']


def coin_prob(num):
    try:
        coin = ['앞','뒤']
        cnt2= 0
        cnts= 0    
        for j in range(10000): 
            a = []  
            for i in range(10):
                result = r.choice(coin)
                a.append(result)
            if a.count('앞') == num:
                cnt2 += 1
            cnts += 1
        print(cnt2/cnts)
    except:
        print('0과 10000 사이의 정수를 넣어주세요')
        

#%%
coin = ['앞','뒤']

for n in range(11):
    cnt2= 0
    cnts= 0    
    for j in range(10000): 
        a = []  
        for i in range(10):
            result = r.choice(coin)
            a.append(result)
        if a.count('앞') == n:
            cnt2 += 1
        cnts += 1
    print('동전을 10번 던져서',n,'개 앞면이 나올 확률', cnt2/cnts)




















