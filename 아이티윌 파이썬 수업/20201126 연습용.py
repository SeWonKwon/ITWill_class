# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:48:34 2020

@author: neva
"""

import random as r

box = [ '정상', '정상', '정상', '정상', '불량', '불량' ]
#복원
cnt = 0
cnts = 0
for i in range(100000):
    cnts += 1
    a1 = r.choice(box)        
    a2 = r.choice(box)
    a3 = r.choice(box)
    if a1==a2==a3=='정상': 
        cnt += 1
print(1-cnt/cnts)
#비복원
cnt = 0
cnts = 0
for i in range(100000):
    cnts += 1
    a = r.sample(box,3)
    if a == ['정상', '정상', '정상']: 
        cnt += 1
print(1-(cnt/cnts))

#%%
# for for for

x = int(input('a')) 
y = int(input('b'))
z = int(input('b'))


n_list = []
for a in range(x):
    for b in range(y):
        for c in range(z):
            n_list.append((a,b,c))
            
print ( n_list )

#%%
# for for for 
x = int(input('a')) 
y = int(input('b'))
z = int(input('b'))

n_list = [(a,b,c) for a in range(x) for b in range(y) for c in range(z)]
print ( n_list )