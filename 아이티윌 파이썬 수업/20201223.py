# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:48:02 2020

@author: bigne
"""

# 154. 필수 알고리즘3 (버블정렬)

# EBS 영상

# 버블 정렬이란? 서로 인접한 두 요소의 크기를 서로 비교하여 순서에 맞지 않는 요소를 인접한
# 요소와 서로 교환하여 정렬하는 정렬 방법을 버블 정렬이라고 한다.

# 문제502. 아래의 리스트를 만들고 첫번째 요소와 두번째 요소의 순서를  변경하시오 !

a = [10,5,20,9,8]

# 결과 a = [5,10,20,9,8]

temp = a[1]
a[1] = a[0]
a[0] = temp
print(a)

#%%문제503. 아래의 a 리스트의 첫번째 요소와 두번째 요소의 크기를 비교해서 첫번째 
#  요소의 숫자가 두번째 요소의 숫자보다 크다면 두개를 바꿔치기해라~~
 
a = [10,5,20,9,8]

# 결과: [5, 10, 20, 9, 8]

temp = a[1]
if a[0] >= a[1]:
    temp = a[1]
    a[1] = a[0]
    a[0] = temp

print(a)

#%%문제504. 문제 503번 코드에 for loop 문을 넣어서 버블 정렬하시오 !

a = [5,4,3,2,1,8,7,10]

# 결과 : [1,2,3,4,5,7,8,10]

for i in range(len(a)-1):
    if a[i] >= a[i+1]:
        temp = a[i+1]
        a[i+1] = a[i]
        a[i] = temp
    print(a)

#%%
a = [5,4,3,2,1,8,7,10]

# 결과 : [1,2,3,4,5,7,8,10]
n=0
for i in range(len(a)-1):
    if a[i] >= a[i+1]:
        temp = a[i+1]
        a[i+1] = a[i]
        a[i] = temp
        n+=1
    print(a,n)
    #%%
a = [5,4,3,2,1,8,7,10]
n=1
while n>0:
    n=0
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            temp = a[i+1]
            a[i+1] = a[i]
            a[i] = temp
            n+=1
        print(a,n)
#%%문제 505. (필수알고리즘3) 위의 코드를 이용해서 버블 정렬을 하는 함수를 아래와 같이 생성하시오.

# print(bubble_sort(a))
# 결과 : [1,2,3,4,5,7,8,10]

a=[10,7,5,4,2,8,1,3]

def bubble_sort(a):
    n=1 
    while n>0:
        n=0
        for i in range(len(a)-1):
            if a[i] >= a[i+1]:
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
                n+=1
            print(a,n)
    return a

print(bubble_sort(a))

#%%


a = [ 10,8, 7, 5, 4, 3, 2, 1  ]

def bubble_sort(a):
    n=0
    for k in range(1, len(a)):
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
            n += 1
    print(n)
    return a
        
print( bubble_sort(a) )

#%%


def bubble_sort(a):

    for j in range(len(a)-1):

        for i in range(len(a)-j-1): # 과도한 계산을 막기 위해서 하나씩 빼줌 정렬된 수는 안봐도 되니까

            if a[i] > a[i+1]:

                a[i],a[i+1] = a[i+1],a[i]
                print(a)
    return a

a=[10,7,5,4,2,8,1,3]

print(bubble_sort(a))

#%% 결이 코드 응용

a=[10,7,5,4,2,8,1,3]

def bubble_sort(a):
    n=1
    b=0 
    while n>0: # n = 0 이 되면 정렬이 완료된것임
        n=0
        b+=1
        for i in range(len(a)-b-1):
            if a[i] >= a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                n+=1
        print(a,n,b)
    return a

print(bubble_sort(a))
#%%소라 코드
a = [5, 4, 3, 2, 1, 8, 7, 10]
def bubble_sort(num):
    n = len(num)

    for k in range(n):
        cnt = 0
        for i in range(n-1):      
            if num[i] > num[i+1]: 
                temp = num[i+1]
                num[i+1] = num[i]
                num[i] = temp
                cnt = 1
        if cnt == 0:  # 더이상 바꿀게 없으면 break
            break
    return num

print(bubble_sort(a))

#%%155 필수 알고리즘4(탐욕알고리즘)

# 머신러닝 배울때 의사결정트리를 구현할 때 사용하는 알고리즘입니다.

#탐욕알고리즘 이란?
# 탐욕 알고리즘은 매 순간마다 최선의 선택을 하는 것입니다. 선택할 때마다 가장 좋다고 생각되는것을
# 선택해 나가며 최종적인 해답을 구하는 알고리즘 입니다.
# 이 알고리즘을 설계할 때 주의할 점은 전체를 고려하는게 아니라 문제를 부분적으로 나누어,
# 나누어진 문제에 대한 최적의 해답을 구하겠금 해야한다는 점입니다.

# 예: 14원의 잔돈을 줘야 하는데 잔돈의 종류가 10원, 7원, 1원이 있으면 잔돈을 가장 빨리 줄수 있는 방법은?
# 답: 7원짜리 2개를 주면 된다.
# 탐욕알고리즘은 10원 1개, 7원 0개, 1원 4개로 주는게 탐욕 알고리즘 입니다.

#%%문제506. 14를 10으로 나눈 몫을 출력하시오.
print(14/10) # 실수
print(int(14/10)) # 정수
print(14//10) # 몫

#%%문제507. 14를 10으로 나눈 나머지값을 출력하시오!

print(14%10)

#%%문제508. 숫자를 물어보게하고 숫자를 10으로 나눈 몫과 숫자를 10으로 
# 나눈 나머지값을 출력하게 하시오!

num = int(input('숫자를 입력하세요~'))

print('몫은 :'+str(num//10))
print("나머지값은 :"+str(num%10))

#%%문제509. 아래의 잔돈 리스트를 만들고 잔돈 리스트의 첫번째 요소로 나눈 몫과 나머지 값이 
#  출력되게 하시오!

coin = [10,7,1]
sorted(coin,reverse=True)
num = int(input('숫자를 입력하세요~'))

print('몫은 :',num//coin[0])
print("나머지값은 :",num%coin[0])

#%%문제510. 위의 코드를 함수로 만들어서 실행되게 하시오!

coin = [10,1,7]

def greedy():
    coin = [10,1,7]
    coin = sorted(coin,reverse=True)
    
    num = int(input('숫자를 입력하세요~'))
    
    print('몫은 :',num//coin[0])
    print("나머지값은 :",num%coin[0])

greedy()

#%%문제511.(필수 알고리즘 4번째) 탐욕 알고리즘을 파이썬으로 구현하시오.

# 잔돈을 입력하세요~ 14

# 10원 동전 1개, 7원 동전 0개, 1원 동전 4개로 줍니다.

# 잔돈을 입력하세요~ 107

# 10원 동전 10개, 7원 동전 1개, 1원 동전 0개로 줍니다.

def greedy():
    coin = [10,1,7]
    coin = sorted(coin,reverse=True)
    
    num = int(input('잔돈을 입력하세요~'))
    
    a = num//coin[0]
    a2 = num%coin[0]
    b= a2//coin[1]
    b2 = a2//coin[1]
    c= b2//coin[2]
    c2= b2//coin[2]

greedy()

#%%
def greedy():
    coin = [10,1,7]
    coin = sorted(coin,reverse=True)
    
    num = int(input('잔돈을 입력하세요~'))
    a=[]
    for k,i in enumerate(coin):
        a.append ( num//i )
        num = num%i
        if k != len(coin)-1:
            print(f"{i}원 동전 {a[k]}개, ",end= '' )
        else:
            print(f"{i}원 동전 {a[k]}개",end= '' )
    print(f"로 줍니다.")

greedy()
#%%

def greedy():

    a = int(input('잔돈을 입력하세요 ~ '))

    coin = [10,7,1]

    for i in coin[:-1]:

        print(f'{i}원 동전 {a//i}개, ',end = '')

        a = a%i

    print(f'{coin[-1]}원 동전 {a//coin[-1]}개로 줍니다.')

greedy()













