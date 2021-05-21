# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:50:30 2020

@author: stu02
"""

#%%특정 문자 얻기

print('scott'[0])
print('scott'[0])

a = 'scott' 
# a라는 문자형 변수를 생성하면서 scott을 a라는 빈컵에 담았다.

print(a[0]) 
print(a[2])

#%%문제253. 아래의 txt 변수에서 w를 출력하시오!

txt = 'A tale that was not right'
n=0
for i in txt:
    print(i,n)
    n += 1

print(txt[12])

#%%문제254. 위의 txt 변수에서 맨끝의 철지인 t를 출력하시오!

print(txt[-1])

#%%문제255. emp3.csv 에서 이름만 출력하시오!
# 판다스를 이용하지 말고 emp2.csv 파일에서 직접 읽어들여서 출력하시오!

import csv

file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1])

#%%문제256. 위의 출력된 이름의 데이터 유형이 무엇인지 확인하시오!

import csv

file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(type(emp_list[1]))

#%%문제257. 문제 255번을 다시 수행해서 emp2.csv에서 이름을 출력하는데 이름의 첫번째 철자만 출력하시오!

import csv

file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0])

#%%문제258. 위의 결과를 다시 출력하는 첫번쨰 철자가 소문자로 출력되게 하시오.
#  (힌트: 'scoTT'.lower()) : (문자열.lower())

import csv

file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0].lower()) #a[0].lower()

#%% 슬라이싱

print( 'scott'[0:2]) # sc 0부터 2미만까지

a  = 'scott'
print(a[0:2]) # sc
print(a[3:]) # 3부터 문자끝까지 출력됨.
print(a[:3]) # 처음부터 3-1(2) 까지.3미만까지

#%%문제259. 아래의 SQL을 파이썬으로 구현하시오!
#  (판다스 이용하지 말과)

# SQL> select ename, substr(ename,1,3)
#       from emp;
      
# 파이썬>

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    print(i[1],i[1][:3])
    
#%%특정열

txt = 'aAbBcCdDeEfFgGhHiIjJkK'

result = txt[0:] # 0번째 부터 문자끝까지 출력
result2 = txt[0::2] # 문자열에서 2칸씩 건너 뛰면서 출력


print(result)
print(result2)

#%%문제260. 위의 txt 문자열에서 짝수번째 철자들만 출력하시오!

txt = 'aAbBcCdDeEfFgGhHiIjJkK'

print(txt[1::2])

#%%거꾸로 만들기

txt = 'aAbBcCdDeEfFgGhHiIjJkK'

print(txt[:]) # 문자열 전체 다 출력
print(txt[::]) # 문자열 전체 다 출력
print(txt[::1]) # 처음부터 끝까지 1스텝으로 읽는다.
print(txt[::-1]) # 문자열 전체를 뒤에 철자부터 앞으로 읽어라~
print(txt[-1::-1]) # 뒤에서부터 거꾸로 ~  -1 스텝씩(방향이 거꾸로~)

#%%문제261. 이름을 출력하는데 이름의 철자를 거꾸로 출력하시오!
#           (emp2.csv를 읽어서)

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    print(i[1][::-1])
    
#%% 문자열 합치기( + )

a = 'scott'
b = 'king'

print(a+b) #scottking

#%%문제262. 아래의 SQL을 파이썬으로 구현하시오! ( emp2.csv를 이용하세요)

# SQL> select enmae||job
#       from emp;

#  파이썬>

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    print(i[1]+i[2])
    
#%%문제263. 아래와 같이 결과가 출력되게 하시오!

# KING 의 직업 PRESIDENT 입니다.
# BLAKE 의 직업은 MANAGER 입니다.

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    print('%s 의 직업은 %s 입니다.' %(i[1],i[2]))

#%%문자열 반복하기 *

print('$'*10)
print('여러분~'*10)

#%%문제264. for loop문을 이용해서 숫자1부터 5까지 출력하시오!

for i in range(5):
    print(i+1)

#%%문제265. 숫자를 물어보게하고 숫자를 입력하면 해당 숫자까지 숫자가 출력되게하시오!

# 숫자를 입력하세요~ 5
n =  int(input('숫자를 입력하세요~  '))

for i in range(n):
    print(i+1)

#%%문제266. 위의 코드를 수정해서 숫자를 물어보게 하고 아래와 같이 $가 출력되게하시오


n =  int(input('숫자를 입력하세요~  '))

for i in range(n):
    print('$'*(i+1))

#%%문제267. (알고리즘 문제22 )  아래와 같이 사각형이 출력되게 하시오 !
# 가로의 숫자를 입력하세요~ 3
# 세로의 숫자를 입력하세요~ 5

a =  int(input('숫자를 입력하세요~  '))
b =  int(input('숫자를 입력하세요~  '))

for i in range(b):
    print('$'*(a))

#%% in 활용하기 특정 문자 확인하기.

txt = 'abcdefghijklmnopqr'

if 'b' in txt:
    print('존재합니다.')
else:
    print('존재하지 않습니다.')
    
#%%문제268. emp2.csv에서 이름을 출력하는데 이름에 S를 포함하고 있는 사원들의 이름을 출력하시오!
# SQL> select ename
#       from emp
#       where ename like '%S%';
      
# 파이썬>

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

for i in emp:
    if 'S' in i[1]: # if 'b' in txt:
        print(i[1])

# 설명: 위의 코드는 금융감독원에서 금융사에 요청하는 것중에 하나가
# 보험회사의 경우 보험 상담원들이 상담할때 적절한 보험용어를 써서
# 고객을 응대를 해야해서 고객과의 통화를 다 녹음을 하고
# 그 녹음된 내용을 text로 변환해서 그 text 안에 단어들을 일일히
# 확인하는 작업을 한다. (예: '30일'이라고 해야하는데 '한달' 이라고 했다던가)
# 이럴때 응용될 수 있는 코드입니다.

#%%문제269. 문제 268번 코드를 수정해서 출력하는데 이름에 S 자가 포함된 
# 사원의 이름이 몇명인지 출력하시오.

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)

cnt = 0
for i in emp:
    if 'S' in i[1]: # 이름에 S 자가 포함되어져 있으면
        cnt += 1

print(cnt)

#%% 문자열 확인하기 
# 겨울왕국 스크립트에서 elsa 라는 단어(문자열)가 몇번 나오는지 카운트 해봅니다.
# 예제1. 겨울왕국(winter.txt) 스크립트를 파이썬으로 불러와서 출력하시오.

winter = open("c:\\data\\winter.txt")
print(winter)

# <_io.TextIOWrapper name='c:\\data\\winter.txt' mode='r' encoding='cp949'>

for i in winter:
    print(i)

# 전체 스크립트 가 한줄 한줄 출력된다.
#%%
# 예제2. 출력되는 스크립트를 전부 소문자로 출력하시오.

winter = open("c:\\data\\winter.txt")
print(winter)
cnt = 0
for i in winter:
    print(i.lower())
    cnt += 1
print(cnt)
#%% 예제3. 위에서 소문자로 출력된 스크립트 한행을 하나 가져와서 아래와 같이 실행하면 뭐가 나올까?

if 'elsa' in 'olaf skates and help elsa coach anna':
    print('존재합니다.')
else:
    print('존재하지 않습니다.')

#%%예제4. 겨울왕국 스크립트에 elsa 가 몇번 나오는지 카운트 하시오!

winter = open("c:\\data\\winter.txt")
print(winter)
cnt = 0
for i in winter:
    if 'elsa' in i.lower():
        cnt += 1
        
print(cnt)

#  한열에 elsa가 2번이상이 나오게 되어도 1개만 cnt 값은 하나만 증가하게 된다.
#  정확하게 하려면 위의 문자열에 elsa 가 2개가 나오게 됩니다.
#%%예제5. winter.txt를 한행씩 읽어서 어절 단위로 출력되게 하시오!

winter = open("c:\\data\\winter.txt")
winter2 = winter.read().split(' ') # 스크립트를 공백단위로 분리해라~ 공백 한칸

for i in winter2:
    print(i)
    
#%%예제6. 위의 어절들이 소문자로 출력되게 하시오.

winter = open("c:\\data\\winter.txt")
winter2 = winter.read().split(' ') # 스크립트를 공백단위로 분리해라~ 공백 한칸

for i in winter2:
    print(i.lower())
#%%문제270. (점심시간 문제) 겨울왕국 스크립트에서 elsa라는 문자열(단어)이 몇번 나오는가?

winter = open("c:\\data\\winter.txt")
winter2 = winter.read().split(' ') # 스크립트를 공백단위로 분리해라~ 공백 한칸

cnt = 0
for i in winter2:
    if 'elsa' in i.lower():
        cnt +=1
        print(i,cnt)
print(cnt)

# Elsa 318
# 설명: 어절별로 분리했지만 \n 때문에 중복이 된경우가 생긴다.
# 위와 같은 실수를 하지 않으려면 먼저 스크립트를 행단위로 먼저 분리를 하고나서
#어절별로 분리를 해야 합니다.

#%%270번 정답

winter = open("c:\\data\\winter.txt")
winter2 = winter.read().split("\n") # 행단위로 분리한다.

cnt = 0
for i in winter2:
    for j in i.split(' '):
        if 'elsa' in j.lower():
            cnt +=1
            print(j,cnt)

# Elsa 329
        
#%%

winter = open("c:\\data\\winter.txt") # winter를 불러온다.
winter2 = winter.read().split("\n") # \n(엔터) 으로 구분을 먼저한다.
#줄 단위로 구분된다.

cnt = 0
for i in winter2:
    for j in i.split(' '):
        if 'elsa' in j.lower():
            cnt +=1
            print(j,cnt)
            
#%%
winter = open("c:\\data\\winter.txt")
winter2 = winter.read().split("\n")

cnt = 0
for i in winter2:
    for j in i.split(' '):
        if 'anna' in j.lower():
            if 'wanna' in j.lower():
                continue
            elif 'vanna' in j.lower():
                continue
            elif 'moreanna' in j.lower():
                continue
            else:
                cnt+=1
                print(j,cnt)

#%%건준's 코드

winter=open('c:\\data\\winter.txt')
winter2=winter.read().split() # 디폴트 값은 어절별로 나눠진다.
                            
cnt=0
for i in winter2:
    if 'elsa' in i.lower():
        cnt+=1
print(cnt)

#%%len

a='scott'
print( len(a) )

#%%문제271. 파이썬으로 emp2.csv를 읽어 이름,이름의 길이를 출력하시오!

# SQL> select ename, length(ename)
#        from emp;
       
# 파이썬>

import csv

file = open("c:\\data\\emp2.csv")
emp = csv.reader(file)
for i in emp:
    print(i[1],len(i[1]))

#%% isalpha

txt1 = 'Warcraft three'
txt2 = '안녕'
txt3 = '3PO'
txt1_1 = 'Warcraftthree'

print(txt1.isalpha()) # False 공백때문에 False가 됨
print(txt1_1.isalpha()) # True 공백을 제거하면 
print(txt2.isalpha()) # True 알파벳이 아니어도 True
print(txt3.isalpha()) # False 숫자또한 알파벳이 아니다!

#%%문제272. 스티븐 잡스 연설문인 jobs.txt 를 한행 한행씩 출력하시오!

stev = open("c:\\data\\jobs.txt", encoding='cp949')
stev2 = stev.read().split('\n') # 한행씩 분리하는 작업

for i in stev2: #한행씩 분리된 스크립트를 읽어서
    print(i) # 출력

#설명: 위의 코드를 실행했는데 cp949 에러가 나면, encoding 에 UTF*도 써보고
# ANSI 도 써보고 CP949도 써보세요~

#%%문제273. 위에서 한행씩 출력하고 있는 스크립트를 철자 하나씩 출력하시오.

stev = open("c:\\data\\jobs.txt", encoding='cp949')
stev2 = stev.read().split('\n') # 한행씩 분리하는 작업

for i in stev2: 
    for k in i: # 철자 하나씩 나오게~
        print(k)

#%%문제274. 위에서 출력된 철자가 알파벳이면 cnt를 증가시켜서
 # 스티븐 잡스 연설문에 알파벳이 몇개가 있는지 출력하시오!

stev = open("c:\\data\\jobs.txt", encoding='cp949')
stev2 = stev.read().split('\n') # 한행씩 분리하는 작업
cnt = 0
for i in stev2: 
    for k in i: 
        if k.isalpha() == True:
            cnt+=1
            print(cnt,k)
            
print(cnt)

# 설명: 스티븐 잡스 연설문에서 숫자나 공백문자나 마침표와
# 같은 구두점을 뺀 알파벳 철자만 카운트 했습니다.
#데이터 분석 사례중에 유명한 사례중 하나가 아프리카 캐냐의 은행에서
# 고객들에게 대출을 해줄때 그 사람의 신용을 확인해서 대출을 해주는데
# 신용을 확인할때 sns의 그사람에 대한 글을 분석해서 긍정적인 평가가
# 많은지 부정적인 평가가 많은지를 파악해서 대출심사에 반영을 하니까
# 훨씬 은행의 대출금 환수가 원활해졌던 사례에서 사용되고 있습니다.

#%%

import pandas as pd

emp122 = pd.read_csv("c:\\data\\emp122.csv")

print(emp122['ENAME','AGE'])

#%%문제275. 숫자가 몇개인지 확인하시오!


stev = open("c:\\data\\jobs.txt", encoding='cp949')
stev2 = stev.read().split('\n') # 한행씩 분리하는 작업
cnt = 0
for i in stev2: 
    for k in i: 
        if k.isdigit() == True:
            cnt+=1
            print(cnt,k,i)
            
print(cnt)

#%%isalnum

a = 'A story is 2003!'
for i in a:
    if i.isalnum()==True:
        print(i)

#%%캐냐 은행의 데이터 분석 사례를 파이썬 코드로 구현해 봅니다.
# ( 긍정단어집, 부정단어집을 다운로드 받으세요.)
# 예제1. 긍정단어(positive-word.txt)를 파이썬으로 읽어서 한행씩 출력하시오.

positive = open("c:\\data\\positive-words.txt")
pos = positive.read().split('\n')

for i in pos:
    print(i)
#%%    
# 예제2. 긍정단어들을 a 라는 비어있는 리스트에 다 추가시키시오!

positive = open("c:\\data\\positive-words.txt")
pos = positive.read().split('\n') # positive 스크립트행을 엔터로 구분한
print(pos)           # 단어들을 pos를 list 형태로 담습니다.

#%%예제3. 아래의 단어가 긍정단어 리스트들 중에 있는지 확인하시오!

if 'wonderful' in [ 'wonderful', 'wonderfully', 'wonderous', 'wonderously', 'wonders', 'wondrous', 'woo', 'work', 'workable', 'worked', 'works', 'world-famous', 'worth', 'worth-while', 'worthiness']:
    print('존재합니다')
else:
    print('존재하지 않습니다.')
    
if 'wonderful' in pos:
    print('존재합니다')
else:
    print('존재하지 않습니다.')
    
# 예제4. 스티븐 잠스 연설문(jobs.txt)를 읽어서 한 단어씩 출력하시오!

stev = open("c:\\data\\jobs.txt", encoding='cp949')
stev2 = stev.read().split() # default 어절별로 분리하는 작업

for i in stev2:
    print(i)
    
#%% 문제276. 스티븐 잡스 연설문에는 긍정단어가 몇개가 있는지 확인하세요~

stev = open("c:\\data\\jobs.txt", encoding='cp949')
stev2 = stev.read().split() 
positive = open("c:\\data\\positive-words.txt")
pos = positive.read().split()

cnt=0
for i in stev2:
    if i.lower() in pos:
        cnt += 1
        
print(cnt)    

#%% 중복된 단어 제거

stev = open("c:\\data\\jobs.txt", encoding='cp949')
stev2 = list(set(stev.read().split())) 
positive = open("c:\\data\\positive-words.txt")
pos = positive.read().split()

cnt=0
for i in stev2:
    if i.lower() in pos:
        cnt += 1
        
print(cnt)    

#%% upper, lower


txt = 'A lot of things occur each day'
result1 = txt.upper()
result2 = txt.lower()
print(result1)
print(result2)

#%%문제277. emp2.csv에서 이름과 월급을 출력하시오!

import csv

file = open("c:\\data\\emp2.csv")

emp_csv = csv.reader(file)

for i in emp_csv:
    print(i[1],i[5])
    
#%%문제278. 이름을 물어보게하고 이름을 입력하면 해당사원의 이름과 월급이 출력되게 하는데 소문자로 입력하던 대문자로 입력하던 잘 출력되게 하시오!

import csv

a = input('이름을 입력하세요~').upper()

file = open("c:\\data\\emp2.csv")
emp_csv = csv.reader(file)

for i in emp_csv:
    if a == i[1]:
        print(i[1],i[5])
        
#%% lstrip, rstrip, strip

txt7 = '    양쪽에 공백이 있는 문자열입니다.     '

print(txt7.lstrip())
print(txt7.rstrip())
print(txt7.strip())

#%%문제279. 스티븐 잡스 연설문에서는 정관사 the 가 몇번 나오는가?

file = open("c:\\data\\jobs.txt", encoding = 'cp949')
jobs = file.read().split()

cnt = 0

for i in jobs:
    if i.lower().strip() == 'the':
        cnt = cnt + 1
        print(i.lower(),cnt)

#%% count

#  문자열 객체의 count() 메소드는 문자열에서 특정 문자의 갯수를 리턴합니다.

txt = 'A lot of things occur each day. Today is beautiful day'

print(txt.count('day'))

#%% 문제280. 안철수 연설문에서는 국민이라는 단어가 몇번 나오는지 카운트 하시오!

file = open("c:\\data\\ahn.txt", encoding = 'UTF8')
ahn = file.read() # split 안했으니까 그냥 안철수 연설문을 읽어서 ahn2에 통채로 입력한다.

print(ahn) # 안철수 연설문 전체가 출력됨
print(ahn.count('국민'))
# 안철수 연설문에서 국민이라는 단어가 몇개 있는지 출력합니다.

#%% count 를 이용해서 elsa 찾아 보기!

winter = open("c:\\data\\winter.txt") 
winter2 = winter.read().lower() 

print(winter2.count('elsa'))

#%% 파이썬에서 막대 그래프 그리는 방법 : 시각화!

import matplotlib.pyplot as plt

y_value=[21.6, 23.6, 45.8, 77.0]
x_index = [0,1,2,3]
plt.bar(x_index, y_value, color='orange')
plt.show()

#%% 문제281. 동전을 10번 던져서 앞면이 2개가 나오는 지난번 마지막 문제의 확률 10개를 가지고 막대 그래프를 그리시오!

import matplotlib.pyplot as plt

y_value=[0.00191, 0.01, 0.07, 0.16]
x_index = [0,1,2,3]
plt.bar(x_index, y_value, color='orange')
plt.show()

#%%문제282. 위의 그래프의 결과에 제목, x축 라벨과 y축 라벨을 같이 출력하시오.

import matplotlib.pyplot as plt

y_value=[0.00191, 0.01, 0.07, 0.16]
x_index = [0,1,2,3]
plt.bar(x_index, y_value, color='orange')
plt.title('coint Probability') # 그래프 제목
plt.xlabel('cnt')               # 그래프 x축 라벨
plt.ylabel('probability')       # 그래프 y축 라벨
plt.show()


#%%%문제283. 동전을 10번 던져서 앞면이 n개 나오는 아래의 확률 결과를 가지고 막대그래프로 시각화 하시오!
import random as r
import matplotlib.pyplot as plt

coin = ['앞','뒤']
y_value=[]
x_index=[]
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
        
    y_value.append(cnt2/cnts)
    x_index.append(n)
print(y_value)
print(x_index)    
# print(y_value, x_value)
plt.bar(x_index, y_value, color='orange')
plt.title('coint Probability') # 그래프 제목
plt.xlabel('cnt')               # 그래프 x축 라벨
plt.ylabel('probability')       # 그래프 y축 라벨
plt.show()

    # print('동전을 10번 던져서',n,'개 앞면이 나올 확률', cnt2/cnts)

#%%문제283. 정답

import random as r
import matplotlib.pyplot as plt

coin = ['앞','뒤']
y_value=[]
x_index=[]
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
        
    y_value.append(cnt2/cnts)
    x_index.append(n)

plt.bar(x_index, y_value, width=0.7, color='orange')
plt.title('coint Probability') 
plt.xlabel('cnt')               
plt.ylabel('probability')       
plt.show()



































