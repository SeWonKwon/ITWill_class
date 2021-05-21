# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:52:47 2020

@author: bigne
"""

listdata = [2,2,1,3,8,4,3,9,2,20]

result = sum(listdata)
print(result)
#%%
# 문제351. 아래의 리스트의 짝수 번째 요소의 합을 출력하시오!

listdata = [ 2,2,1,3,8,4,3,9,2,20]

listdata2 = listdata[1::2]
print(sum(listdata2))

#%%문제352. (알고리즘 문제) 아래의 리스트에 1부터 10까지의 숫자중에 없는 숫자가 하나있따.
# 없는 숫자가 하나있다. 그 없는 숫자는 무엇인가?

a = [ 2,1,5,4,6,7,9,10,3]

print(sum(range(1,11))-sum(a))

#%% all(), any()

listdata1 = [True,True,True]
listdata2 = [True,False,True]
print( all(listdata1))
print( all(listdata2))
print( any(listdata1))
print( any(listdata2))

#%%예제

listdata1 = [1,1,1]
listdata2 = [1,0,1]  # True 는 숫자로는 1이고 False는 숫자로는 0입니다.
print( all(listdata1))
print( all(listdata2))
print( any(listdata1))
print( any(listdata2))

#%%문제353. while loop 문을 이용해서 무한루푸문을 수행하시오!
while True:
    print('계속 출력중입니다')
    
#%%문제354. 이번에는 위의 True 대신에 숫자1을 넣고 무한 로프문을 수행하시오!

while 1:
    print('1은 True입니다.')
    
#%%

sol = {} # 중괄호를 써서 비어있는 딕셔너리를 생성합니다.
sol['태양'] = 'Sun'
sol['수성'] = 'Mercury'
sol['금성'] = 'Venus'
print(sol)

#%%문제355. 아래의 2개의 리스트를 가지고 sol 딕셔너리를 생성하시오!

sol_eng = ['sun','mercury','venus','earth','mars']
sol_kor = ['태양','수성','금성','지구','화성']
sol={}

for i,k in enumerate(sol_kor):
    sol[k]=sol_eng[i]

print(sol)


#%% 사전형이름['키값'] = '값'
sol['태양'] = 'aaa'
print(sol)

#%% 문제356. 아래의 딕셔너리의 값중에 Fire 를 피땀눈물로 변경하시오!
dict = {'방탄소년단':'Fire','소녀시대':'Gee'}

dict['방탄소년단']='피땀눈물'
print(dict)

#%%문제357. 아래의 딕셔너리의 값중에서 Fire를 피땀눈물로 변경하시오!
dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}

dict['방탄소년단'] = ['DNA','피땀눈물']

print(dict)

#%%
dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}

dict['방탄소년단'][1] = '피땀눈물'
print(dict)

#%%

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}

del sol['태양']

print(sol)

#%%문제358. 아래의 딕셔너리에서 다시만난세계의 값만 지우시오!

dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}

del dict['소녀시대'][0]
print(dict)

#%% clear

dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}
dict.clear()
print(dict) #{}

#%%문제359. 위와 같이 딕셔너리의 요소를 지우는게 아니라 딕셔너리 자체를
# 메모리에서 지우려면 어떻게 해야하는가?

dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}
del dict
print(dict)

#%% keys

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}

print(list(sol.keys()))

#%%문제360. 위의 sol 사전에 있는 키를 추출해서 아래와 같이 결과를 출력하시오.

# 결과: 태양, 수성, 금성, 지구, 화성

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}
for i in sol.keys():
    print ( i , end = ', ')

# a = list(sol.keys())
# print(' ,'.join(a))

#%%문제361. 위의 결과에서 맨끝에 있는 콤마(,)는 출력되지 않게 하시오!

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}

for i,k in enumerate(sol.keys()):
    if i+1 != len(sol):
        print ( k , end = ', ')
    else:
        print(k)

#%%

#%%문제362. 아래의 sol 딕셔너리에서 값들만 아래와 같이 출력하시오!

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}
for i in sol.values():
    print ( i , end = ', ')

#%%문제363. 아래의 gini 딕셔너리에서 값만 추출하시오 !

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}

for i in gini.values():
    print(i)

#%%문제364. 위의 결과를 다시 출력하는데 리스트 3개중에 0번째 요소만 출력하시오!

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}

for i in gini.values():
    print(i[0])
    
#%%문제365. 지난주 목요일 마지막 문제의 자신의 답을 가져와서 gini딕셔너러니에서
# 음악만 출력하는데 아티스트별로 노래가 겹치지 않게 출력하시오!


import numpy as np
from random import shuffle

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}


list_gini = (list(gini.items()))                            # 딕셔너리는 순서가 없기때문에 list로 변환
shuffle(list_gini)                                           # 임의대로 섞어준후 가수가 임의로 순서를 정하려고.
r_gini=dict(list_gini)                                      # 다시 딕셔너리형으로 바꿔줌.

a= []
for j in np.random.choice([0,1],2,replace=False):  # 임의로 노래 순서를 선택하되 중복되지 않게 하기위해서.
    for i in r_gini.values():
        a.append(i[j])

bond = ', '
play_list = bond.join(a)
print(play_list)
#%%문제366. 아래의 gini 딕셔너리의 값들을 리스트로 만드시오!
from random import shuffle
gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}
gini2 = []
for i in gini.values():
    gini2.append(i)
print(gini2)
#문제367. 위에서 출력된 gini2 리스트의 요소들을 shuffle 로 섞어 보시오!
shuffle(gini2)
print(gini2)
#%%문제367.(점심시간문제) 지난시간 만들었던 마지막 문제의 자신의 답과 리스트의 요소를 무작위로 섞는 
# shuffle 함수를 이용해서 코드를 수행할때마다 곡이 무작위로 섞여서 출력되게 하시오.
# ( 단 조건은 아트스트별로 노래가 겹치면 안된다. 바로 음악 바로 옆에 다른 아티스트의 노래가 나오게 합니다.)

from random import shuffle

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}
a = []

for i in gini.values():
    shuffle(i) # 노래의 순서를 뒤바꾸기
    a.append(i)
shuffle(a) # 가수의 순서를 뒤바꾸기

for j in range(2):
    for i,k in enumerate(a):
        if i+j < len(a):
            print (k[j], end=', ')
        else: 
            print ( k[j])

#%% items()



#문제369. 위의 gini딕셔너리 요소들의 items 를 뽑아서 리스트에 담으시오!

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}

result = list(gini.items())

print(result)

#문제370. 위의 result 에서 음악 첫번째 곡들만 아래와 같이 출력하시오!

# yesterday
# 너랑나
# beat it

for i in result:
    # list(i)      # 튜플도 순서가 있어서 굳이 리스트화 해주지 않아도 된다.
    print(i[1][0])

#%%

dict2 = {'소녀시대': '소원을 말해봐', '방탄 소년단' : 'DNA', '오마이걸' : ' 살짝 설랬어'}

#  1. 위의 dict2 에서 키만 추출

print(dict2.keys()) # dict_keys(['소녀시대', '방탄 소년단', '오마이걸'])

# 2. 위의 dict의 키값을 아래와 같이 정렬 해서 출력하시오!

result = dict2.keys()
print(sorted(result))  # ['방탄 소년단', '소녀시대', '오마이걸']

#문제371. 위의 결과를 reverse 되게 해서 출력하시오!

print(sorted(result,reverse=True))

#%%문제372. 우리반 데이터 (emp1222.csv)에서 이름과 통신사를 출력하시오!

import csv

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    print ( emp_list[1], emp_list[5])
    
#%% defaultdictionary 를 이용해서 딕셔너리의 값을 리스트로 구성하는 코드

from collections import defaultdict
gini = defaultdict(list)  # 같은 키에 여러 밸류값을 넣고 싶을때 설정
# gini={'kt':'3','sk':'33'} 에러나게 됨
gini['kt'].append('허혁')
gini['kt'].append('정다희')
gini['sk'].append('박혜진')
gini['sk'].append('김승순')
print(gini)

#%%문제373. 우리반 데이터에서 통신사를 key로 하고 학생이름을 값을로해서
# deafultdictionary 를 생성하시오! default dictionary 이름은 telecom 으로 하세요.

import csv
from collections import defaultdict

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
telecom = defaultdict(list)

for emp_list in emp_csv:
    telecom[emp_list[5]].append(emp_list[1])

print(telecom)

#%%374. 위에서 구성한 telecom 딕셔너리에서 통신사가 kt 인 학생들을 출력하는데
# 이름을 ㄱ ㄴ ㄷ ㄹ 순으로 정렬해서 출력하시오!

import csv
from collections import defaultdict

file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
telecom = defaultdict(list)

for emp_list in emp_csv:
    telecom[emp_list[5]].append(emp_list[1])

telecom_kt = sorted(telecom['kt'])

print(telecom_kt)

#%%ord

print( ord('A'))

#%%문제375. 알파벳 대문자를 출력하시오 !

import string
print(string.ascii_uppercase)

#%%문제376. 위의 코드와 ord() 함수를 이용해서 아래의 결과를 출력하시오!
# 결과:
# A ---------> 65
# B ---------> 66
# C ---------> 67

import string
for i in string.ascii_uppercase:
    print(i+' ---------> '+str(ord(i)))
    

#%% chr()
print( chr(65))

#%%문제377. 아래와 같이 결과를 출력하시오!

# 결과:
# 65 ---------> A
# 66 ---------> B
# 67 ---------> C
# 68 ---------> D

import string
for i in range(65,91):
    print(str(i)+' ---------> '+chr(i))
    
    
#%% eval
a  = '2 + 3'
print(a)
print( eval(a))

#%%문제378. 아래의 결과를 출력하시오 !

# 34 + 256 - 71*34 = ? 

a  =  '34 + 256 - 71*34'
print(a,'=',eval(a))

#%%문제379. 아래의 리스트의 숫자를 뽑아내서 아래의 문자열을 생성하시오!

a = [34,22,45,27,31,33,55]
a = str(a)

bond = '+'
b = bond.join(a)
print(b) # TypeError: sequence item 0: expected str instance, int found
# [+3+4+,+ +2+2+,+ +4+5+,+ +2+7+,+ +3+1+,+ +3+3+,+ +5+5+]

#%%답:
    
a = [34,22,45,27,31,33,55]
b = []
for i in a:
    b.append(str(i))
print(b)

result = ' + '.join(b)
print(result)
#%%

#%%문제380. 아래의 리스트를 가지고 아래의 결과를 출력하시오 !
#결과 : 34 + 22 + 45 + 27 + 31 + 33 + 55 = 247
a = [34,22,45,27,31,33,55]
b = []
for i in a:
    b.append(str(i))
print(b)

result = ' + '.join(b)
print(result, ' = ',eval(result))

#%%문제381. 우리반 데이터(emp1222.csv) 에서 나이를 읽어들여 아래와 같이
#       결과가 출력되게 하시오.

import csv
file = open("c:\\data\\emp1222.csv")
emp_csv = csv.reader(file)
b = []
for i in emp_csv:
    b.append(i[2])
result = ' + '.join(b)
print(result,' = ', eval(result))
# print(emp_age)

#%% lambda

def add_func(a,b):
    return a+b
    
print(add_func(2,3)) # 5

#  설명: 함수를 만들때 위와 같이 함수 이름을 주고 생성했습니다.


k = lambda a,b : a + b
print( k(2,3)) # 5

# 문법: 변수이름 = lambda 입력매개변수 : 실행문

#%%문제382. 아래의 함수를 그냥 이름 없는 한줄짜리 함수로 만들어 보시오!

def gob_func(a,b):
    return a*b

k = lambda a,b : a*b
print(k(2,3))

#%%문제383. 아래의 함수를 그냥 이름 없는 한줄짜리 함수로 생성하시오!

def odd_func(a):
    if a % 2 == 0:
        return '짝수입니다.'
    else:
        return '홀수 입니다.'

print ( odd_func(2))
print ( odd_func(3))
#%%
k = lambda a : '짝수입니다.' if a%2==0 else '홀수입니다.'  
print(k(3))

#%%문제384. 아래의 함수를 lambda 로 구현하시오!
def high_income(a):
    if a >= 3000:
        return '고소득자입니다.'
    else:
        return '일반 소득자입니다.'
    
k = lambda a : '고소득자입니다.' if a>=3000 else '일반 소득자입니다.'
print(k(3333))

#%%문제385. 아래의 함수를 lambda 로 구현하시오 !

def child_tall(num):
    if 140 - 1.96*5<= num <= 140 + 1.96*5:
        return '신뢰구간 95% 안에 있습니다.'
    else: 
        return '신뢰구간 95% 안에 없습니다.'

k = lambda a : '신뢰구간 95% 안에 있습니다.' if 140 - 1.96*5<= a <= 140 + 1.96*5 else '신뢰구간 95% 안에 없습니다.'
print(k(144)) # 이렇게 길때는 그냥 def 써라~

# 신뢰구간 68%  z = 1
# 신뢰구간 95%  z = 1.96
# 신뢰구간 99%  z = 2.58

#%%문제 386. 초등학생 키 데이터를 120 ~ 160 사이로 해서 0.001 간격으로 생성하시오!

import numpy as np
x= np.arange(120,160,0.001)
print(len(x))
print(x)

#%%387.  위에서 만든 40000건의 데이터에 대한 확률 밀도 함수값을 출력하시오.

from scipy.stats import norm
import numpy as np 
x = np.arange(120,160,0.001)
y = norm.pdf(x,140,5)
print(y)

#%%388. 
from scipy.stats import norm
import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(120,160,0.001)
y = norm.pdf(x,140,5)
print(y)
plt.plot(x,y,color='red')
plt.show()
#%%389. 위의 그래프에서 신뢰구간 95% 에 해당하는 부분만 색깔로 칠하시오.
from scipy.stats import norm
import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(120,160,0.001)
y = norm.pdf(x,140,5)
print(y)
plt.plot(x,y,color='red')
plt.fill_between(x,y, where = (x >= 140 - 1.96*5)&(x<=140+1.96*5),color='red',alpha=0.5)
plt.show()


#%% 문제390. (오늘의 마지막 문제) 위의 코드를 이용해서 confidence_interval 함수를 생성
#            하고 아래와 같이 신뢰구간을 넣으면 해당 신뢰구간에 해당하는 그래프가
#            출력되게하시오 !

# 신뢰구간 68% ---> 평균 ± 1 * 표준편차
# 신뢰구간 95% ---> 평균 ± 1.96 * 표준편차
# 신뢰구간 99% ---> 평균 ± 2.58 * 표준편차 

from scipy.stats import norm
import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(120,160,0.001)
y = norm.pdf(x,140,5)
print(y)
plt.plot(x,y,color='red')
plt.fill_between(x,y, where = (x >= 140 - 1.96*5)&(x<=140+1.96*5),color='orange',alpha=0.5)
plt.show()


#%%

from scipy.stats import norm
import numpy as np 
import matplotlib.pyplot as plt
def multiple():
    try:
        question = [('신뢰구간을 선택해 주세요~/1번)68%/2번)95%/3번)99%')]
        for i in question:
            ii = i.split('/')
            for j in range(4):
                print(ii[j])
        a = int(input('몇번?'))
        if a == 1:
           return  1
        elif a == 2:
           return  1.96
        elif a == 3:
           return  2.56           
    except:
        return None

inter = multiple()
  
try:  
    x = np.arange(120,160,0.001)
    y = norm.pdf(x,140,5)
    plt.plot(x,y,color='black')
    plt.fill_between(x,y, where = (x >= 140 - inter*5)&(x<=140+inter*5),color='orange',alpha=0.5)
    plt.show()
except:
    print('1,2,3번 중에서 선택해 주세요')
#%%


    print(sl[0])

    print(sl[1])

    print(sl[2])

    print(sl[3])li=[]

li.append('1. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/4')

li.append('2. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/3')

li.append('3. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/2')

li.append('4. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/1')

li.append('5. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/3')

tot=0

for i in li:

    sl=i.split('/')

    print(sl[4])

    a=input('\n 답?')

    if a==sl[5]:

        print('정답입니다.')

        tot=tot+20

    else :

        print('오답입니다.')

    print()



print('당신의 점수는',tot,'입니다.')













