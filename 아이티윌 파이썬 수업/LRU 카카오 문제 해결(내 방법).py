# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:17:46 2020

@author: bigne
"""

# LRU 알고리즘 문제 풀기

# 2가지 캐이스로 구분 해주는데

# cacheSize(1~30)
# cache hit 1초

# cache miss 5초


cache = [] # 요소의 갯수는 cacheSize 의 갯수와 같다.

cacheSize = int(input('캐쉬 사이즈 캣쉬 갯수'))

search = []

cnt=0
for i in search:
    if i in cache:
        cnt+=1
        if len(cache) != cacheSize: # cache에 꽉차지 않은 경우
            i.append(cache)
        else: # cache에 꽉찬 경우
            for j in range(cachSize-1):
                chache[j]=chache[j+1]#한칸씩 땡겨서 앞으로 가는 코드 마지막 코드는 지운다.
                i.append(cache)
            del(cache[cachSize])
    else:
        i.append(cache)
        cnt+=5
        
print(cnt)

#%%

cache = [] # 요소의 갯수는 cacheSize 의 갯수와 같다.

cacheSize = 3

search = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

cnt=0
for i in search:
    if i in cache:
        cnt+=1
        del(cache[cache.index(i)])
        if len(cache) != cacheSize: # cache에 꽉차지 않은 경우
            cache.append(i)
            print('있는데 안찬경우',cache)
        else: # cache에 꽉찬 경우
            for j in range(cacheSize-2): # 0,1 
                cache[j]=cache[j+1]#한칸씩 땡겨서 앞으로 가는 코드 마지막 코드는 지운다.
                cache.append(i)
            
            print('꽉차서 지운경우',cache)
    else:
        cnt+=5
        if len(cache) != cacheSize:
            cache.append(i)
            print('없어서 넣은경우 안참', cache)
        else:
            del(cache[0])
            # for j in range(cacheSize-2): # 0,1 
            #     cache[j]=cache[j+1]#한칸씩 땡겨서 앞으로 가는 코드 마지막 코드는 지운다.
            cache.append(i)
            
            print('없어서 꽉차서 지운경우',cache)
print(cnt)

print(cache)

#%%

search = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

del(search[3])

print(search)

#%%오류 해결함. 함수 생성 완료. 정답 까지 체크 됨.

def cacheProcess(search,cacheSize):
    cache = [] # 요소의 갯수는 cacheSize 의 갯수와 같다.
    # cacheSize = 3
    search = [i.lower() for i in search]
    cnt=0
    if cacheSize == 0:
        cnt = len(search)*5
    else:
        for i in search:
            if i in cache:
                cnt+=1
                del(cache[cache.index(i)])
                if len(cache) != cacheSize: # cache에 꽉차지 않은 경우
                    cache.append(i)
                    # print('있는데 안찬경우',cache)
                else: # cache에 꽉찬 경우
                    for j in range(cacheSize-2): # 0,1 
                        cache[j]=cache[j+1]#한칸씩 땡겨서 앞으로 가는 코드 마지막 코드는 지운다.
                        cache.append(i)
                    
                    # print('꽉차서 지운경우',cache)
            else:
                cnt+=5
                if len(cache) != cacheSize:
                    cache.append(i)
                    # print('없어서 넣은경우 안참', cache)
                else:
                    del(cache[0])
                    # for j in range(cacheSize-2): # 0,1 
                    #     cache[j]=cache[j+1]#한칸씩 땡겨서 앞으로 가는 코드 마지막 코드는 지운다.
                    cache.append(i)
                    
                    # print('없어서 꽉차서 지운경우',cache)
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
        print("%i번가 일치합니다.."%i)
#%%다듬기

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
