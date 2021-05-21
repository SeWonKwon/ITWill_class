# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:34:31 2020

@author: neva
"""
import math as m
# n= int(input('숫자'))
n=18

num = 0
for i in range(1,n+1):
    b = int(m.log10(i)) + 1
    num = num*(10**b) + i
    
print(num)
    
# 2 1 3 1 4 1 ... 10 2 999 3 1000 4
# 1        1*10**0
# 12       1*10**1 + 2*10**0
# 123      1*10**2 + 2*10**1 + 3*10**0
# 1234     1*19**3 + 2*10**2 + 3*10**1 + 4*10**0

#%%

a = int(input('숫자를 입력하세요~'))+1

s = 0
for i in range(1,a):
    for j in range(5):
        if 10**(j-1)<= i <10**(j):
            s = s*10**j + i
        else:
            s = s
print ( s )
        
#%%
n = int(input())

s = 0
for nt in range(1,14):
    for nk in range(0,3):
        if nt < 10**nk and nt >= 10**(nk-1):
            s = s*10**nk +nt      
        else:
            s = s        
print(s)