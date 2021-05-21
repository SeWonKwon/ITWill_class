



#%%
def fun_row():  # 수열의 방식
    num = int(input('input number'))
    n = 1
    for i in range(2,num+1):
        if i <= 9:
            n  = n*10**1+ i
        elif i <= 99:
            n = n*10**2 + i
        else:
            n = n*10**3 + i
    return n

print(fun_row())

#%%
import math
def fun_log():  # 로그의 지표를 이용한 방법.
    num = int(input('input number'))
    n = 1
    for i in range(2,num+1):
        n  = n*10**int(math.log10(i) +1 )+ i
    return n

print(fun_log())

#%%
import math
def fun_jae(num,n=1,a=0): #재귀
    if n == num+1:
        return a
    else:
        a = a*10**int(math.log10(n) +1)+ n
        return fun_jae(num,n+1, a)
    
print(fun_jae(151))

#%%

import math
def add_number(number,stack=0,start=0): # 입력받을 숫자, stack = 누적, start = 한자리씩 올리기 위함
    squ = 0
    squ = start + stack # 제곱에 들어갈 숫자 = 기본적으로 n-1승 + stack
    stack += math.trunc(math.log10(number)) # stack은 log10해서 버림한 숫자의 sum
    if number == 1: # 1이면
        return number*(10**squ) # 1곱하기 10의 squ 제곱
    else:
        return add_number(number-1,stack,start+1) + number * (10**squ)  # 재귀함수 
        # 2를 넣으면 2*10^squ + add_num(1) = 1*10^1 + 2*10^0

print(add_number(101))






