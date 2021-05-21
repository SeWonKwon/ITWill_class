# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 09:39:34 2020

@author: bigne
"""



#%% 코딩 예제 : 아래의 리스트를 받아서 아래의 결과를 출력하시오 !
cities = ['Jeju','Pangyo','New York','new york']
cities_lower = []
for i in cities:
    cities_lower.append(i.lower())
    
print(cities_lower)

#%% 위의 코드를 comprehesion 을 사용해서 간단하게 수행하시오 !

cities = ['Jeju','Pangyo','New York','new york']
city = [i.lower() for i in cities]
print(city)

# 설명: 위의 코드는 comprehension 코드로 위의 5줄 코드를 3줄로 간소한 코드입니다.

#%% 문법:[출력 표현식 for 요소 in 입력시퀀스 if 조건식]
# 예:
a = [i for i in range(1,21) if i%2 ==1]
print(a)
#%% 예제: 아래의 리스트를 생성하시오 !

# 코딩예제: 아래의 리스트를 생성하시오 ! (None 은 아무것도 없다는 뜻입니다.)

a = [None for i in range(4)]

print(a)

#%%
a = [input('d') for i in range(3) for j in range(3)]
print(a)

#%% 메모리에 데이터를 올린다.(cache miss 니까 5초가 걸려야 한다.) 메모리에 데이터를
cache = [None for i in range(4)]
del[cache[0]]
cache.append('jeju')
print(cache)

#%% pangyuo를 올려보시오.

cache = [None for i in range(4)]
del[cache[0]]
cache.append('jeju')
del[cache[0]]
cache.append('pangyo')
print(cache)

#%% 코딩 예제3. 위에서 만든 코드를 가지고 아래의 함수를 생성하시오.

cities = ['Jeju','Pangyo','New York','new york']

def cacheProcess( cities, cachesize):
    city = [i.lower() for i in cities]
    cache = [None for i in range(1,cachesize+1)]
    for i in city:
        cache.append(i)
        del cache[0]
    return cache

print( cacheProcess(cities,4))

#%%코딩예제4. 위의 함수의 결과가 cache 의 결과가 아니라 수행시간이 되게 하시오!

cities = ['Jeju','Pangyo','New York','new york']

def cacheProcess( cities, cachesize):
    city = [i.lower() for i in cities]
    cache = [None for i in range(1,cachesize+1)]
    cnt= 0
    for i in city:
        if i in cache:
            cnt+=1
            cache.append(i)
            del cache[0]
        else:
            cnt+=5
            cache.append(i)
            del cache[0]
    return cnt
    

print( cacheProcess(cities,0)

      #%% 점심시간 문제: LRU 를 구현하시오. 카카오 문제
def cacheProcess(search,cacheSize):
    cache = [] # 요소의 갯수는 cacheSize 의 갯수와 같다.
    search = [i.lower() for i in search] # 대소문자 구분 제거
    cnt=0
    
    for i in search:
        if i in cache: # cache hit
            cnt+=1
            del(cache[cache.index(i)]) # 검색된 코드를 맨뒤로 넣는 코드
            cache.append(i)
        else: #cache miss
            cnt+=5
            if cacheSize==0:
                continue
            elif len(cache) != cacheSize:
                cache.append(i)
            else:
                del(cache[0])
                cache.append(i)
    return cnt





check = []

a = cacheProcess(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],3)

check.append(a)

a = cacheProcess(["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],3)

check.append(a)

a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA","SanFrancisco","Seoul","Rome","Paris","Jeju","NewYork","Rome"],2)

check.append(a)

a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA","SanFrancisco","Seoul","Rome","Paris","Jeju","NewYork","Rome"],5)

check.append(a)

a = cacheProcess(["Jeju","Pangyo",'NewYork','newyork'],2)

check.append(a)

a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA"],0)

check.append(a)

a = cacheProcess(['Jeju', 'Jeju','Jeju'],3)

check.append(a)



print(check)



correct = [50,21,60,52,16,25,7]



for i in range(len(check)) :

    if check[i] != correct[i] :

        print("%i번째 경우가 틀립니다."%i)
    
    else:
        print("%i번이 일치합니다.."%i)

#%%자료형 
# 1. 튜플형
# 2. 리스트형
# 3. 딕셔너리형
# 4. 집합형 set
a = {1,2,3,4}
b = {2,4,5}
#1. a와 b 의 합집합 구하기

result1 = a.union(b)
print(result1)
# 2. a 와 b의 교집합 구하기
result2 = a.intersection(b)
print(result2)

# 3. a 와 b 의 자카드 유사도를 구하시오.

result3 = len(result2)/len(result1)
print(result3)


#%% 리스트로 합집합과 교집합 구하기.

a = [1,2,3,4]
b = [2,4,5]

# 1. a와 bdml 합집합 구하기
result1 = list(set(a+b))
print(result1)

# 2. a와 b의 교집합 구하기
result2=[]
for i in a:
    if i in b:
        result2.append(i)
        
result3 = [i for i in a if i in b]
# result2 = list(set(a+b))
# del(result(a)) 
print(result3)

#%% 자카드 유사도 알고리즘 문제를 파이썬으로 구현하는 방법 순서
# 1. 문제를 2번 읽으면서 문제를 정확하게 파악한다.
    # (특히 질문을 명확하게 제시해줘야 합니다.)

# 질문: FRANCE, FRENCH 의 두 단어의 자카드 유사도는?
    # 관련 알고리즘(자카드 유사도) 의 정확한 이해가 있어야 합니다.

# 2. 문제를 해결하기 위해서 순서별로 해결방법을 기술한다.

# 3. 순서별로 정한 해결방법을 파이썬 코드로 구현한다.


#%%

str1 = input('문자열을 입력하세요~').lower()
str2 = input('문자열을 입력하세요~').lower()
#%% 2개씩 나누기, isapha를 이용해서 문자열만 뽑아내기
str1 ='FRANCE'
str2 ='french'
str1 = str1.lower()
str2 = str2.lower()
res1 = []
res2 = []
for i in range( len(str1) - 1):
    if str1[i].isalpha() & str1[i+1].isalpha():
        res1.append(str1[i:i+2])
print(res1)

#%% 함수로 만들기

def str_split(string):
    string = string.lower()

    res1 = []
    for i in range( len(string) - 1):
        if string[i].isalpha() & string[i+1].isalpha():
            res1.append(string[i:i+2])
    return res1

print(str_split('asdfAS+df""dfdfas'))

# 확인해보기

str1 ='FRANCE'
str2 ='french'

print(str_split(str1))
print(str_split(str2))
#%% 교집합과 합집합을 구해보자.
a= str_split(str1)
b= str_split(str2)
a_b_inter = [i for i in a if i in b]
a_b_union= list(set(a+b))

print(a_b_inter)
print(a_b_union)
#%% 다중 집합으로 확장하기 위해서 바꾼다.
a =[1,1,1,2,2,3,4,4,4]
b =[1,1,2,2,2,4,4,4,4,5]

a_b_inter = []
for i in a:
    if i in b:
        a_b_inter.append(i)
print(a_b_inter)
a_b_inter= list(set(a_b_inter))

a_b_inter2 = []
for i in a_b_inter: 
    if a.count(i) or b.count(i) >=2:
        for j in range(min(a.count(i),b.count(i))-1):       # 다중 함수 교집합
            a_b_inter2.append(i)
    else:
        a_b_inter2.append(i)
print(a_b_inter2)

a_b_union = [i for i in a if i not in (a_b_inter2)] + [i for i in b if i not in (a_b_inter2)]
for i in list(set(a_b_inter)):
    for j in range(max(a.count(i),b.count(i))):
        a_b_union.append(i)
print(a_b_union)
#%%

a_b_inter = [i for i in a if i in b]
a_b_union= [ ]
for i in a+b:
    if i in 

print(a_b_inter) # 1,1,2,2,4,4,4,4
print(a_b_union) # 1,1,2,2,2,3,4,5

#%% 자카드 유사도 구하기

result = int(len(a_b_inter)/len(a_b_union)* 65536)
print(result)

#%% 문제521. 지금까지의 코드를 함수로 만들어서 아래와 같이 실행되게 하시오.
def str_split(string):
    
    res1 = []
    for i in range( len(string) - 1):
        if string[i].isalpha() & string[i+1].isalpha():
            res1.append(string[i:i+2].lower())
        
    return res1


def Jaccard():

    str1 = 'handshake'
    str2 = 'shake hands'
    # str1 = 'aa1+aa2'
    # str2 = 'AAAA12'
    str1 = 'E=M*C^2'
    str2 = 'e=m*c^2'
    # str1 = input('문자열을 입력해주세요').lower()
    # str2 = input('문자열을 입력해주세요').lower()
    
    
    a= str_split(str1)
    b= str_split(str2)
    
    
    a_b_inter = []
    for i in a:
        if i in b:
            a_b_inter.append(i)
    print(a_b_inter)
    a_b_inter= list(set(a_b_inter))
    print(a_b_inter)
    a_b_inter2 = []
    for i in a_b_inter: 
        for j in range(min(a.count(i),b.count(i))):
            a_b_inter2.append(i)
        
    print(a_b_inter2)
    a_b_union = [k for k in a if k not in b] +[t for t in b if t not in a]
    
    print(a_b_union)
    
    for i in a_b_inter:
        for j in range(max(a.count(i),b.count(i))):          # 다중함수 합집합
            a_b_union.append(i)
    print(a_b_union)
    
    if len(a_b_inter2) == 0: 
        return 65536
    else:
        return int((len(a_b_inter2)/len(a_b_union))* 65536)


print(Jaccard())



#%%
def str_split(string): # 문자열 나누기
    
    res1 = []
    for i in range( len(string) - 1):
        if string[i].isalpha() & string[i+1].isalpha():
            res1.append(string[i:i+2].lower())
        
    return res1

def inter(a,b): # 다중 함수 교집합
    a_b_inter = [i for i in a if i in b]
    a_b_inter= list(set(a_b_inter))
    
    a_b_inter2 = []
    for i in a_b_inter: 
        for j in range(min(a.count(i),b.count(i))):
            a_b_inter2.append(i)
    return a_b_inter2

def union(a,b):    # 다중함수 합집합
    
    a_b_union = [k for k in a if k not in b] +[t for t in b if t not in a]
    
    a_b_inter_set = list(set(inter(a,b)))
    for i in a_b_inter_set:
        for j in range(max(a.count(i),b.count(i))):          
            a_b_union.append(i)
    
    return a_b_union

def Jaccard(): # 자카드 유사도 구하는 함수

    str1 = input('문자열을 입력해주세요').lower()
    str2 = input('문자열을 입력해주세요').lower()
        
    a= str_split(str1)
    b= str_split(str2)
    
    if len(inter(a,b)) == 0: 
        return 65536
    else:
        return int((len(inter(a,b))/len(union(a,b)))* 65536)


print(Jaccard())

#%%


def  str_split(string):           
    res =[]
    for  i  in  range( len(string) -1 ):
        if  string[i].isalpha()  and  string[i+1].isalpha():   
            res.append( string[ i : i+2] )
    return res

def Jaccard():
    str1 = input('문자열을 입력해주세요. :').upper()
    str2 = input('문자열을 입력해주세요. :').upper() 
    
    a = str_split(str1)
    b = str_split(str2)

    import math
    import collections
    intersection = []
    result = collections.Counter(a) & collections.Counter(b) # 교집합
    intersection = list(result.elements()) # 요소만 리스트로 빼내오기
    
    result2 = collections.Counter(a) | collections.Counter(b) # 합집합
    union = list(result2.elements())       # 요소만 리스트로 빼내오기

    len_i = len(intersection)
    len_u = len(union) 
    
    try:
        return math.trunc(len_i / len_u * 65536)
    
    except:
        return 65536

print( Jaccard() )



























