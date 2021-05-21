# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:59:32 2020

@author: bigne
"""

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') # 오라클 주소를 기입한다.

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn) # 오라클 접속 유져 정보
cursor = db.cursor() # 결과 데이터를 담을 메모리 이름을 cursor 로 선언함.
cursor.execute("""select * from emp """) # 작성한 쿼리문의 결과가 
                                            # cursor 메모리에 담긴다.
row = cursor.fetchall() # cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
emp = pd.DataFrame(row)
print(emp)

#%%문제440. 위의 emp 테이블 전체를 select 했는데 전체를 다 select 하지 말고 아래의 쿼리의
# 결과만 select 하시오 ! 
#  select empno, ename, sla,deptno
# from emp;

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select empno, ename, sal, deptno from emp """)  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)

#%%문제441. dept 테이블의 모든 데이터를 조회하시오 ! 

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select * from dept""")  
                                            
row = cursor.fetchall() 
dept = pd.DataFrame(row)
print(dept)
#%%문제442. 우리반 학생들의 정보를 조회 하시오!
import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select * from emp12""")  
                                            
row = cursor.fetchall() 
emp12 = pd.DataFrame(row)
print(emp12)


#%%문제443. 월급이 1200 이상인 사원들의 이름과 월급을 출력하시오!


import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select * from emp where sal>1200""")  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)

#%% ??
import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select ename,sal from emp""")  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
emp.index = emp[0]
emp.plot(kind='bar')
# emp.cloumns = ['ename','sal']
print(emp[0])

#%%문제445. (점심시간 문제) 위의 그래프의 색깔을 변경하고 그래프를 올리세요.

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select ename,sal from emp""")  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
emp.columns = ['ename','sal']
emp.index = emp['ename']
emp.plot(kind='bar',color='orange')
# print(emp[0])
#%%문제446

#%%문제447. 직업,직업별 토탈월급을 출력하는데 직업별 토탈월급이 높은것부터 출력하시오.

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select job, sum(sal)
                    from emp
                    group by job
                    order by sum(sal) desc""")  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
emp.columns=['job','sum(sal)']

print(emp)

#%%문제448. 이름, 월급, 순위를 출력하는데 순위가 월급이 높은 사원 순으로 순위를 부여하시오!

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select job, sal, rank() over (order by sal desc)
                    from emp
                    order by sal desc""")  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
emp.columns=['job','sal','rank']

print(emp)

#%%문제449. 부서번호, 부서번호별 토탈월급을 출력하시오!

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select deptno, sum(sal)
                    from emp
                    group by deptno""")  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
emp.columns=['deptno','sum(sal)']

print(emp)
#%%문제450. 위의 결과를 막대 그래프로 시각화 하시오!

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

# print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select deptno, sum(sal)
                    from emp
                    group by deptno""")  
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row)
emp.columns=['deptno','sum(sal)']


row = cursor.fetchall() 
emp.index = emp['deptno']
emp.plot(kind='bar',color='orange')

#%%문제451. emp 테이블 전체를 출력하는데 컬럼명이 출력되게 하시오.

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

# print(dsn)

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
# cursor.execute("""select * from emp""")
cursor.execute("""select * from emp""")
row = cursor.fetchall()
colname=cursor.description
emp = pd.DataFrame(row)
col = []
for i in colname:
    col.append(i[0].lower())
# print(colname)
# print(col)

print(emp)
#%%문제452. 위의 col 리스트에 담긴 컬럼명을 위의 데이터에 매핑 시키시오.
#컬럼명을 출력해보자~

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select * from emp""")
row = cursor.fetchall()

colname=cursor.description
# col = []
# for i in colname:
#     col.append(i[0].lower())
# emp.columns=col # 컬럼명을 지정
emp = pd.DataFrame(list(row),columns =[i[0].lower() for i in cursor.description ] )
print(emp)

#%%문제453. 위의 컬럼명을 이용해서 판다스 문법으로 이름과 월급을 출력하시오.

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select * from emp""")
row = cursor.fetchall()

colname=cursor.description
emp = pd.DataFrame(list(row),columns =[i[0].lower() for i in cursor.description ] )

result=emp[['ename','sal']]
print(result)

#%%문제454. 월급이 3000 이상인 사원들의 이름과 월급을 출력하시오 !

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select * from emp""")
row = cursor.fetchall()

colname=cursor.description
emp = pd.DataFrame(list(row),columns =[i[0].lower() for i in cursor.description ] )

result=emp[['ename','sal']][emp['sal']>=3000] 
print(result)

#%%문제455. 이름과 부서위치를 출력하시오 ! ( SQL )

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select e.ename, d.loc 
                   from emp e, dept d
                   where e.deptno = d.deptno""")
row = cursor.fetchall()

colname=cursor.description
emp = pd.DataFrame(row)
emp = pd.DataFrame(list(row),columns =[i[0].lower() for i in cursor.description ] )

result=emp[['ename','loc']]
print(result)

#%%문제456. 부서위치, 부서위치별 토탈월급을 출력하시오 !

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select d.loc ,sum(e.sal)
                   from emp e, dept d
                   where e.deptno = d.deptno
                   group by d.loc""")
row = cursor.fetchall()

colname=cursor.description
emp = pd.DataFrame(row)
emp = pd.DataFrame(list(row),columns =[i[0].lower() for i in cursor.description ] )

result=emp[['loc','sum(e.sal)']]
print(result)
#%%문제457. 위의 표를 막대 그래프로 보이시오.

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select d.loc ,sum(e.sal)
                   from emp e, dept d
                   where e.deptno = d.deptno
                   group by d.loc""")
row = cursor.fetchall()

colname=cursor.description
emp = pd.DataFrame(row)
# emp = pd.DataFrame(list(row),columns =[i[0].lower() for i in cursor.description ] )

# result=emp[['loc','sum(e.sal)']]
emp.index = list(emp[0])
emp.plot(kind='bar',color='red')
print(emp)

#%%문제 458~~ onenote

#%%문제472.

import pymysql,pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select * from emp"
curs.execute(sql)
rows = curs.fetchall()
colname = curs.description
col = []
for i in colname:
    col.append(i[0].upper())
emp = pd.DataFrame(list(rows),columns=col)
print(emp[['ENAME', 'SAL']] )
#%%

import pymysql,pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select job, sum( sal ) from emp group by job"
curs.execute(sql)
rows = curs.fetchall()
colname = curs.description
col = []
for i in colname:
    col.append(i[0].upper())
emp = pd.DataFrame(list(rows),columns=col)
print(emp[['ENAME', 'SAL']] )


#%%문제 문제473. 직업, 직업별 토탈월급을 출력하시오.

import pymysql,pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select job, sum(sal) from emp group by job"
curs.execute(sql)
rows = curs.fetchall()
colname = curs.description
col = []
for i in colname:
    col.append(i[0].upper())
emp = pd.DataFrame(list(rows),columns=col)
# print(emp)
print(emp[['JOB','SUM(SAL)']])

#%%문제474. 위의 결과를 막대그래프로 시각화 하시오!

import pymysql,pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select job, sum( sal ) from emp group by job"
curs.execute(sql)
rows = curs.fetchall()
colname = curs.description
col = []
for i in colname:
    col.append(i[0].upper())
# emp = pd.DataFrame(list(rows),columns=col)
emp = pd.DataFrame(rows)
# print(emp[0][1])
#
emp.index = list(str(emp[0]))
# emp=emp.astype(float)
emp.plot(kind='bar',color='orange')

#%%

import pymysql
import pandas as pd

conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select job, sum(sal) from emp group by job"
curs.execute(sql)
rows = curs.fetchall()

# colname = curs.description
# col = []
# for i in colname:
#     col.append(i[0].upper())
emp = pd.DataFrame(list(rows),columns=[i[0] for i in curs.description])

# result = emp[['job','sum(sal)']]
# for i in result:
#     print(i)
#%%

row = cursor.fetchall() 
emp.index = emp['job']

#%%
emp.plot(kind='bar',color='Blue')


#%%문제474번을 오라클로 한 경우

import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select job, sum(sal) from emp group by job""")
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row,columns = [i[0] for i in cursor.description ])
print(type(emp))

row = cursor.fetchall() 
emp.index = emp['JOB']
emp.plot(kind='bar',color='orange')

#%%문제 475(마지막 문제). 오라클과 파이썬을 연동하여 아래의 사원들 검색하시오!
# 이름과 월급과 부서번호와 자기가 속한 부서번호의 평균 월급을 출력하는데 자신의 월급이 자기가 속한 
# 부서번호의 평균월급보다 더 큰 사원들만 출력하시오 !


import cx_Oracle 
import pandas as pd

dsn = cx_Oracle.makedsn("localhost",1521,'orcl') 

db = cx_Oracle.connect('scott','tiger',dsn)
cursor = db.cursor() 
cursor.execute("""select e.ename, e.sal, e.deptno, d.avgs
                    from emp e, (select deptno, round(avg(sal),2) avgs
                                     from emp
                                     group by deptno) d
                    where e.deptno = d.deptno""") 
                     
                                            
row = cursor.fetchall() 
emp = pd.DataFrame(row,columns = [i[0] for i in cursor.description ])

print(emp[['ENAME','SAL','DEPTNO','AVGS']][emp['SAL']>emp['AVGS']])



















