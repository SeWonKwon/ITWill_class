# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:32:20 2020

@author: bigne
"""

#%% insert

list_a = ['a','b','c','d','e']
list_a.append('f')
print(list_a)

list_a.insert(3,'k')
print(list_a)

# 설명: list_a.insert(3,'k') 는 인덱스 번호 3 에 k를 구성해라~

#%%문제319. 아래의 a 리스트의 요소 화성 다음에 소행성을 요소로 입력하시오!

a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']

a.insert(a.index('화성')+1,'소행성')
print(a)

#%%  del & remove

a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']

del(a[4])
print(a)

#%%문제320.아래의 a 리스트에서 목성을 지우시오!

a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']

del(a[a.index('목성')])
print(a)

#%% remove

a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']

a.remove('목성')
print(a)

#%%321. 아래의 빨간공 2개와 파란공 3개가 들어 있는 주머니에서 공을 하나 랜덤으로 빼면
# 그 공이 주머니에서 지워지게 하시오!

box = ['red','blue','red','blue','blue']

import random as r

a1 = r.choice(box)
box.remove(a1)
print(a1,box)
print(box.count('red'))
#%%
box = ['red','blue','red','blue','blue']

import random as r

for i in range(len(box)):
    box.remove(r.choice(box))

    print(box)
    print(box.count('red'))

#%%문제322. 아래의 주머니에서 임의로 하나의 공을 뽑았을 때 그 공이 파란색일 확률은 
어떻게 되는가? (복원추출)

box = ['red','blue','red','blue','blue']

import random as r

cnt= 0
cnts = 0
for i in range(1000000):
    cnts += 1
    a1 = r.choice(box)
    if a1 == 'blue':
        cnt+=1
print(cnt/cnts)
#%%문제323. 파란공 70개와 빨간공 30개가 들어 있는 주머니를 만드시오.
box = []
a = ['blue']*70
b = ['red']*30
box = a+b
print(box)

# 문제324. 위의 box 에 들어있는 요소가 몇개인지 확인하시오!

box = []
a = ['blue']*70
b = ['red']*30
box = a+b
print(len(box))
print(box.count('red'))

#%%문제325. 위의 box 에 있는 요소들을 무작위로 섞으시오!

from random import shuffle

box = []
a = ['blue']*70
b = ['red']*30
box = a+b

shuffle(box)
print(box)

#%%문제 326. 위의 box에서 공 3개를 추출했을때 그 공3개가 다 파란색일 확률은 어떻게
#되는가? ( 공을 뽑는 작업을 10000번 수행하시오.) (복원)

from random import shuffle

box = []
a = ['blue']*70
b = ['red']*30
box = a+b

shuffle(box)

cnt = 0
cnts = 0

for i in range(1000000):
    a1 = r.choice(box)
    a2 = r.choice(box)
    a3 = r.choice(box)
    cnts += 1
    if a1 == 'blue' and a2 =='blue' and a3 =='blue':
        cnt += 1

print(cnt/cnts)

#%% choice 를 여러번 쓰지 않는 방법
from random import shuffle

box = []
a = ['blue']*70
b = ['red']*30
box = a+b

shuffle(box)

cnt = 0
cnts = 0

for i in range(1000000):
    result = r.sample(box,99)
    cnts += 1
    if result.count('blue')==3:
        cnt += 1

print(cnt/cnts)
#%%
from random import shuffle

box = []
a = ['blue']*70
b = ['red']*30
box = a+b

shuffle(box)

cnt = 0
cnts = 0

for i in range(1000):
    result = r.sample(box,101)
    cnts += 1
    if result.count('blue')==3:
        cnt += 1

print(cnt/cnts)

#ValueError: Sample larger than population or is negative 코드로 sample 함수가 비복원임을 알수 있따.
#%% 문제327. 이번에는 위의 box에서 공을 3개를 뽑았을때 그중 2개가 blue 일 확률을 출력하시오!
# (복원 추출, 공을 뽑는 작업을 10000번 수행하세요~) 비복원
from random import shuffle

box = []
a = ['blue']*70
b = ['red']*30
box = a+b

shuffle(box)

cnt = 0
cnts = 0

for i in range(1000):
    result = r.sample(box,3)
    cnts += 1
    if result.count('blue')==2:
        cnt += 1

print('비복원', cnt/cnts)


#%%문제328. 위의 문제를 복원추출로 수행하시오!


import numpy as np

box = []
a = ['blue']*70
b = ['red']*30
box = a+b

cnt = 0
cnts = 0

for i in range(1000000):
    result = list(np.random.choice(box,3))
    cnts += 1
    if result.count('blue')==2:
        cnt += 1

print('복원',cnt/cnts)


#%%

import numpy as np

box = []
a = ['blue']*70
b = ['red']*30
box = a+b

cnt = 0
cnts = 0

for i in range(1000000):
    result = list(np.random.choice(box,3,replace= False))
    cnts += 1
    if result.count('blue')==2:
        cnt += 1

print('비복원',cnt/cnts)


#[김주원] [오후 12:01] https://yganalyst.github.io/data_handling/memo_4/
#%%문제329. 내가 올린 코드를 참조해서 아래의 문제를 해결하시오!
#6개의 제품이 들어 있는 상자가 있는데 그중에 2개가 불량품이라고 했을때 제품 검사를 위해 3개를 추출했을때 
#1개가 불량품일 확률을 출력하시오!

import numpy as np

box = ['불량']*2+['정상']*4

cnt = 0
cnts = 0

for i in range(10000):
    result = list(np.random.choice(box,3,replace=True)) # 복원, replace=False 비복원
    cnts += 1
    if result.count('불량') == 1:
        cnt += 1

print(cnt/cnts)


#%%

import numpy as np

box = ['불량']*2+['정상']*4

cnt = 0
cnts = 0

for i in range(10000):
    result = list(np.random.choice(box,3,replace=False)) # 복원, replace=False 비복원
    cnts += 1
    if result.count('불량') == 1:
        cnt += 1

print(cnt/cnts)

#%% 추출 및 선택 에 관하여
import ranomd as r
import numpy as np

a= [1,2,'dd']
a1 = np.random.choice(a,3,replace=False) # 비복원
a2 = np.random.choice(a,3,replace=True)  # 복원
a3 = r.sample(a,3) # 비복원 
a4 = r.choice(a) # 한개만 석택

print (a1,a2,a3,a4)

#%%난수 생성1.

np.random.rand : 0부터 1사이의 균일분포
np.random.randn : 가우시안 표준 정규 분포
np.random.randint : 균일 분포의 정수 난수

#%%
a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del(a[2:6])
print(a)

#%%문제330. 위의 리스트 a의 요소를 다 지우시오!

a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del(a[:])
print(a)

#%%문제331. (점심 시간 문제) 초등학생 10만명의 체중 데이터를 가지고 히스토그램 그래프를 그리시오~

# (초등학생 10만명의 평균 체중은 45kg 이고 표준 편차는 5입니다.)

# 30 ~~ 60kg 2간격으로


import csv
import numpy as np
import matplotlib.pyplot as plt

emp12 = open("c:\\data\\emp1222.csv")
emp12 = csv.reader(emp12)
next(emp12)               # 컬럼명 날리기
a=[]
for i in emp12:
    a.append(int(i[2]))
x_val = list(range(int(min(a)),int(max(a))+1,2))
a = np.array(a)

plt.xticks(x_val)         # x축 눈금 조절. 검색해서 찾았습니다.
plt.yticks(range(0,12))   # y축 눈금 조절.
plt.hist(a,x_val,rwidth = 0.8)

#%%


import matplotlib.pyplot as plt
import numpy as np
import csv

file = open("c:\\data\\emp1222.csv")
emp = csv.reader(file)

age = [ int(i[2]) for i in emp ]
bins = [ i for i in range(24,45,2)]
plt.grid()
plt.hist(age, bins, rwidth= 0.8, alpha = 0.8, color='orange')

plt.title('12') 
plt.xlabel('cnt')               
plt.ylabel('age') 

#%%

import numpy as np
import matplotlib.pyplot as plt

weight = np.random.randn(100000)*5 + 45

x_val = [i for i in range(30,61,2)]
weight = np.array(weight)

plt.xticks(x_val)                 #눈금표시
plt.yticks(range(0,20000,2000))  #눈금 표시
plt.ylim(0, 18000)                # y 범위 지정 
plt.hist(weight,x_val,rwidth = 0.8,alpha = 0.8, color='orange')
# plt.axis([30, 61, 0])

plt.title('weight') 
plt.xlabel('kg')               
plt.ylabel('cnt') 


#%%len
a=['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
print( len(a) )

#%%문제332. 점심시간에 만들었던 초등학생 10만명의 체중 데이터를 모수로 보고 10만명의
# 체중 데이터에서 100명을 샘플링하여 평균을 구하시오.

import numpy as np

weight = np.random.randn(10000)*5 + 45

sample= np.random.choice(weight,100, replace=True).mean()

print(sample)

#%%

import matplotlib.pyplot as plt

import numpy as np

 

N = 1000000

std = 5

avg = 45

 

a = []

population_weight = np.random.randn(N) * std + avg

#print(population_weight)

 

for i in population_weight:

    a.append(int(i))

 

bins = list(range(30,61,2))

plt.xticks(bins) #x축 tick

 

plt.grid()

plt.hist(population_weight, bins, rwidth = 0.9, color = 'black')

plt.xlabel('kg') #x축 label

plt.ylabel('cnt') #y축 label




#%%문제333. 위의 모집단에서 표본 100명을 추출하여 표본평균을 구하는 작업을 1000번 수행해서 1000개의
# 표본평균을 a 라는 비어있는 리스트에 넣으시오!

import numpy as np

weight = np.random.randn(10000)*5 + 45

a = []
for i in range(1000):
    sample_mean= np.random.choice(weight,100, replace=True).mean()
    a.append(sample_mean)

print(a)

#%%문제334. 위의 a 리스트의 요소의 갯수를 출력하시오.

import numpy as np

weight = np.random.randn(10000)*5 + 45

a = []
for i in range(1000):
    sample_mean= np.random.choice(weight,100, replace=True).mean()
    a.append(sample_mean)

print(len(a))

#%%문제335. 위의 표본평균 1000개를 가지고 히스토그램 그래프를 그리시오.

# x 축 계급의 범위 : 30 ~ 60 (간격2)

import numpy as np
import matplotlib.pyplot as plt

weight = np.random.randn(1000)*5 + 45

x_val = [i for i in range(30,61,2)]
weight = np.array(weight)

a = []
for i in range(1000):
    sample_mean= np.random.choice(weight,100, replace=True).mean()
    a.append(sample_mean)



plt.xticks(x_val)         
plt.yticks(range(0,50,5))
# bins = list(range(42,47,1))   
plt.hist(a,30,rwidth = 0.8,alpha = 0.8, color='orange') # (갯수를 셀 대상, x축에 관하여서 몇개로 나누는가?, 넓이,투명도,색깔)
# plt.axis([43.5, 46.5, 0, 10])# x 축의 범위

plt.title('weight') 
plt.xlabel('kg')               
plt.ylabel('cnt') 
plt.ylim(0, 100, 10) # y축의 칸

#%%문제335. 위의 표본평균 1000개를 가지고 히스토그램 그래프를 그리시오

 # x 축 계급의 범위 : 30 ~ 60 (간격 2)  
import matplotlib.pyplot as plt
import numpy as np
N = 1000000
std = 5
avg = 45
population_weight = np.random.randn(N) * std + avg
a = []
for  i  in  range(1, 1001):
    result  = np.random.choice(population_weight, 100, replace=True).mean()
    a.append(result)
bins = list(range(40,51,1))
plt.xticks(bins) #x축 tick
plt.grid()
plt.hist( a, bins, rwidth = 0.9, color = 'black')
plt.xlabel('kg') #x축 label
plt.ylabel('cnt') #y축 label


#%%리스트.count()

box= ['yellow','yellow','red','red','red']
print(box.count('red'))

#%%문제336. 우리반 데이터의 나이를 비어있는 리스트에 a 에 입력하고 나서 
# 우리반 나이 데이터중에서 27살이 몇명있는지 출력하시오!

import csv

file = open("c:\\data\\emp1222.csv")
emp12 = csv.reader(file)

a = []
for i in emp12:
    a.append(i[2])
print(a.count('27'))

#%% del

a = [ 1, 2, 3, 3, 3, 4 ]

del a
print(a) # NameError: name 'a' is not defined 메모리에서 완전히 지우는 명령어

#설명: 스파이더 오른쪽 에 지우개 기능은 현재까지 스파이더를 사용하면서 정의된 모든 변수를 
#  다 지우는 기능입니다.

#%%문제337. 파이썬에서 정의된 모든 변수들을 확인하시오!

a = [1,2,3,4,5]
b = 'scott'
c777 = 30

print(dir())
print(globals())

#%% sort

a= [2,4,1,3,5]
a.sort()
print(a) # [1,2,3,4,5]

#만약에 역순으로 정렬하고 싶다면 ?

a.sort(reverse=True)
print(a) # [5, 4, 3, 2, 1]

#%% 문제338. emp2.csv에서 월급을  비어있는 리스트인 a 에 담고 월급을 역순으로 정렬해서 
# 리스트의 요소로 구성하시오!

import csv

file = open('c:\\data\\emp2.csv')
emp = csv.reader(file)

a=[]
for i in emp:
    a.append(int(i[-3]))

a.sort(reverse=True)
print(a)

#%%  sorted

a = [2,1,3,5,4]
a.sort()
print(a)

a = [2,1,3,5,4]
b = sorted(a)

print(b)
print(a)

#%% shuffle

from random import shuffle
a=[1,2,3,4,5,6,7,8,9,10]
shuffle(a)
print(a)
#%%문제339. 아래의 artist 라는 리스트에 가수이름들을 추가하고 music 리스트에 음악 리스트를 추가하시오!

artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

#%%문제340. 아래에 artist를 키로 하고 music을 값으로 해서 아래와 같은 딕셔너리를 구성하시오.

artist = ['비틀즈','아이유','마이클 잭슨']
music = ['yesterday','너랑나','beat it']

# gini = {'비틀즈': 'yesterday', '아이유': '너랑나', '마이클 잭슨': 'beat it'}

# 답:
gini = {} # 비어있는 딕셔너리를 gini라는 이름으로 생성한다.
gini['비틀즈'] = 'yesterday' # 변수['키값']='밸류값'
gini['아이유'] = '너랑나'
gini['마이클 잭슨'] = 'beat it'
print(gini)

#%%문제341. 위와 같이 일일이 손으로 노가다 하지말고 아래의 2개의 리스트를 이용해서 
# for 문과 zip을 이용해서 한번에 gini 딕셔너리를 구성하시오
artist = ['비틀즈','아이유','마이클 잭슨']
music = ['yesterday','너랑나','beat it']

gini = {}

for i,k in zip(artist,music):
    gini[i]=k
print(gini)

#%% enumerate

# 예:
emp12 = ['김주원','김미승','김홍비','권세원']
result = list( enumerate(emp12))
print(result)

# 예2:
emp12 = ['김주원','김미승','김홍비','권세원']
for i, k in enumerate(emp12):
    print(i,k)
    
#%%문제342. 아래의 music 리스트에서 요소를 하나씩 빼내는데 앞에 인덱스 번호도
# 같이 출력되게 하시오
# 0 yesterday
# 1 imagine
# 2 너랑나
# 3 마슈멜로우
# 4 beat it
# 5 smooth criminal
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

for i,k in enumerate(music):
    print(i,k)

#%%문제343. artist 리스트를 가지고 아래와 같이 출력하시오.

artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
# 비틀즈 0
# 비틀즈 1
# 아이유 2
# 아이유 3
# 마이클 잭슨 4
# 마이클 잭슨 5
for i,k in enumerate(artist):
    print(k,i)
    
#%%문제344. 아래의 두개의 리스트를 가지고 아래와 같이 출력하시오!

# 비틀즈 yesterday
# 비틀즈 imagine
# 아이유 너랑나
# 아이유 마슈멜로우
# 마이클 잭슨 beat it
# 마이클 잭슨 smooth criminal


artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

for i,k in enumerate(artist):
    print(k, music[i])

#%%
def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value
        
artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
gini={}
for i,k in zip(artist,music):
    append_value(gini, i, k)
    
print(gini)

#%% 최종: 위에 artist 를 키로 하고 music 을 값으로 해서 딕셔너리를 구성하시오!
# {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}
# 설명: 위와 같이 딕셔너리를 구성하려면 그냥 딕셔너리인 중괄호 하나로 {} 비어있는
# 딕셔너리를 만들면 안되고 defaultdict 를 이용해야합니다. defaultdict는
# collections 패키지에 있어서 아래와 같이 임폴트 해야합니다.

artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

from collections import defaultdict
gini = defaultdict(list)
gini['비틀즈'].append('yesterday')
print(gini)
gini['비틀즈'].append('imagine')
print(gini)

#%%345. 그럼 위에서 만든 default 딕셔너리에 아이유를 키로 하고 너랑나, 마슈멜로우를
# 값으로 해서 추가하시오!
artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

from collections import defaultdict
gini = defaultdict(list)
gini['비틀즈'].append('yesterday')
gini['비틀즈'].append('imagine')

print(gini)

#%%346. 위와 같이 일일이 손으로 노가다 하지 말고 enumerate를 이용해서 gini 딕셔너리를 구성하시오!
artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

from collections import defaultdict
gini = defaultdict(list)
for i,k in enumerate(artist):
    gini[k].append(music[i])

print(gini)

#%%문제347. 위의 gini 딕셔너리에서 음악만 추출하시오(딕셔너리 값만 추출)
# 딕셔너리에서 키값만 추출: 딕셔너리이름.key()
# 딕셔너리에서 밸류만 추출: 딕셔너리이름.values()
artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

from collections import defaultdict
gini = defaultdict(list)
for i,k in enumerate(artist):
    gini[k].append(music[i])

for i in gini.values():
    for k in i:
        print(k)
#%%문제348. 위의 코드 음악들을 비어있는 리스트인 a 에 담으시오!

# ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

from collections import defaultdict
gini = defaultdict(list)
for i,k in enumerate(artist):
    gini[k].append(music[i])
a=[]
for i in gini.values():
    for k in i:
        a.append(k)
print(a)
#%%문제349. 아래의 코드를 수행해서 gini.values() 의 요소들을 프린트 해보시오!

artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']

from collections import defaultdict
gini = defaultdict(list)
for i,k in enumerate(artist):
    gini[k].append(music[i])

for i in gini.values():
    print(i[0])

for i in gini.values():
    print(i[1])

#%%350. 아래와 같이 결과를 출력하시오!
artist = ['비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
from random import shuffle

from collections import defaultdict
gini = defaultdict(list)
for i,k in enumerate(artist):
    gini[k].append(music[i])
a=[]
for j in range(2):
    for i in gini.values():
        shuffle(i)
        a.append(i[j])

print(a)

#%%ㅇㅇ
import numpy as np
from random import shuffle

gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}
list_gini = (list(gini.items())) # 딕셔너리는 순서가 없기때문에 list로 변환
shuffle(list_gini) # 임의대로 섞어준후 가수가 임의로 순서를 정하려고.
r_gini=dict(list_gini) # 다시 딕셔너리형으로 바꿔줌.

a= []
for j in np.random.choice([0,1],2,replace=False): # 임의로 노래 순서를 선택하되 중복되지 않게 하기위해서.
    for i in r_gini.values():
        a.append(i[j])

bond = ', '
play_list = bond.join(a)
print(play_list)

#%%코드 다듬기 노래의 갯수가 달라지는 경우. 최소값 기준으로 돌리기  더 나은 방법 생각해바~

import numpy as np
import random 

gini = {'비틀즈': ['111', '333','3','32','43'], '아이유': ['너랑나', '마슈멜로우','하나더'], '마이클 잭슨': ['beat it', 'smooth criminal','another','the others']}
list_gini = (list(gini.items())) # 딕셔너리는 순서가 없기때문에 list로 변환

print(gini.values())
num=[]
for i in gini.values():
    num.append(len(i))
n = min(num)
shuffle(list_gini) # 임의대로 섞어준후 가수가 임의로 순서를 정하려고.
r_gini=dict(list_gini) # 다시 딕셔너리형으로 바꿔줌.
  
a= []
for j in np.random.choice([a for a in range(n)], n, replace=False): # 임의로 노래 순서를 선택하되 중복되지 않게 하기위해서.
    try:
        for i in r_gini.values():
            a.append(i[j])
    except:   
        print('d')
            
bond = ', '
play_list = bond.join(a)
print(play_list)
#%%


from collections import defaultdict
import numpy as np
import random 

gini = {'비틀즈': ['111', '333','3','32','43'], '아이유': ['너랑나', '마슈멜로우','하나더'], '마이클 잭슨': ['beat it', 'smooth criminal','another','the others']}
list_gini = (list(gini.items())) # 딕셔너리는 순서가 없기때문에 list로 변환



print(gini.values())
num=[]
for i in gini.values():
    num.append(len(i))
n = min(num)
random.shuffle(list_gini) # 임의대로 섞어준후 가수가 임의로 순서를 정하려고.
r_gini=dict(list_gini) # 다시 딕셔너리형으로 바꿔줌.
for i,j in enumerate(artist):
    gini[j].append(music[i])
a=[]
b=[]
for i in artist:
    b.append(artist.count(i))

for n in range(max(b)):    
    for k in gini.values():
        if len(k)>n:
            a.append(k[n])
        else:
            continue
bond = ','
result = bond.join(a)
print(result)

#%%
artist = ['비틀즈','비틀즈','비틀즈','비틀즈','아이유','아이유','마이클 잭슨','마이클 잭슨']
music = ['yesterday','imagine','1','2','너랑나','마슈멜로우','beat it','smooth criminal']

from collections import defaultdict
gini = defaultdict(list)
for i,k in enumerate(artist):
    print(i,k)
    gini[k].append(music[i])
# print(gini)

# a=[]
# for i,k in gini.items():
#     for 