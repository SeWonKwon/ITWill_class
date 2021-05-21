# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:45:40 2020

@author: neva
"""
#%%클래스 생성자 이해하기

class Card():
    def __init__(self):
        self.cash = 0
        print('카드가 발급되었습니다.', self.cash, '원이 충전되어 있습니다.')

ksw_card = Card() # 객체(제품)를 생성하는 명령어

#%%문제167. 총 클래스를 생성하는데 총 클래스로 아래와 같이 총(제품)을 생성하면 
# "총이 만들어졌습니다. 총알은 0발 장전되었습니다.'라는 메세지가 출력되게 총 클래스를 만드시오!

class Gun():
    def __init__(self):
        self.bullet = 0
        print('총이 만들어졌습니다.','총알은', self.bullet,'발 장전되었습니다')
        
ksw_gun = Gun()

#%%문제168.문자열 포멧을 이용해서 위의 메세지를 더 자연스럽게 출력되게 하시오!

class Gun():
    def __init__(self):
        self.bullet = 0
        print('총이 만들어졌습니다.총알은 %d발 장전되었습니다' %self.bullet)
        # print('총이 만들어졌습니다.','총알은', str(self.bullet)+'발 장전되었습니다')
        
ksw_gun = Gun()

#%% 소멸자 이해하기
    
class Gun():
    def __init__(self):
        self.bullet = 0
        print('총 한정이 생성되었습니다.')
    def __del__(self):
        print('총이 폐기 되었습니다.')

yys_gun1 = Gun()

del yys_gun1


#%% 상속 이해하기

# 팀장님이 만든 카드 class ( 카드 설계도 )   
# 1. 카드가 발급되었을때 0원이 충전되게 하는 기능 : __init__(self)
# 2. 카드를 충전하는 기능 : charge(self,num) :
# 3. 카드를 쓰는 기능 : consume(self,num) :

class Card(): #부모 클래스
    def __init__(self):
        self.cash = 0
        print ('카드가 발급되엇습니다.')
    
    def charge(self,num):
        self.cash += num
        print(num,'원이 충전되었습니다.')
    
    def consume(self, num):
        if self.cash >= num:
            self.cash -= num
            print (num,'원이 사용되었습니다.')
        else:
            print('잔액이 부족합니다.')

ksw_card = Card()
ksw_card.charge(10000)
ksw_card.consume(8000)

#%%문제169. 충전한 금액보다 더 많은 금액을 소비하면 어떻게 되는지 테스트하시오!

ksw_card.consume(8000)   
        
#%%문제170. 팀장님이 만든 Card() 클래스를 상속받아 영화할인 카드를 생성하시오 !
# (영화할인 카드 클래스: Movie_Card()) 

class Movie_Card(Card): # 부모클래스인 Card 클래스를 상속받아서
    pass                # Movie_Card 클래스를 만든다.

m_card1 = Movie_Card() 
m_card1.charge(100000)
m_card1.consume(5000)

#%%문제171. 이번에는 제대로 영화관에서 사용하면 할인이 될수 있도록 영화 클래스를 생성하시오 !

class Movie_Card(Card): # 부모에게 __init__, charge, consume 를 상속받았다.
    def consume(self,num,place): # 부모에게 받은 consume는 내가 만든 consume로
        if place == '영화관':     # 덮어쓰기(overriding)가 됩니다.
            num = 0.8*num
            if self.cash >= num: 
                self.cash -= num
                print(place,'에서', int(num),'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.')
        else:
            if self.cash >= num:
                self.cash -= num
                print( place,'에서', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.')

m_card1 = Movie_Card()
m_card1.charge(100000)
m_card1.consume(10000,'영화관')
m_card1.consume(5000,'편의점')
      
#%%문제172.위의 영화할인 카드에 할인 장소를 추가해서 
#   주유소에서도 20%할인 될수 있도록 코드를 수정하시오!
        
class Movie_Card(Card): 
    def consume(self,num,place): 
        if place in ('영화관','주유소'):     # 할인율이 같다면 in을 사용한다.
            num = 0.8*num
            if self.cash >= num: 
                self.cash -= num
                print(place,'에서', int(num),'원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.')
        else:
            if self.cash >= num:
                self.cash -= num
                print( place,'에서', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다.')

m_card1 = Movie_Card()
m_card1.charge(100000)
m_card1.consume(10000,'영화관')
m_card1.consume(80000,'주유소')
m_card1.consume(5000,'편의점')      

#%%문제173. (점심시간 문제) 영화관과 주유소에서는 20% 할인되게 하고 
#                         스타벅스에서는 10% 할인되게 코드를 수정하시오

class Movie_Card(Card): 
    def consume(self,num,place): 
        if place in ('영화관','주유소'):     
            num = 0.8*num
        elif place =='스타벅스':            
            num = 0.9*num
        else:
            pass
        if self.cash >= num: 
                self.cash -= num
                print(place,'에서', int(num),'원이 사용되었습니다.')
        else:
                print('잔액이 부족합니다.')

m_card1 = Movie_Card()
m_card1.charge(100000)
m_card1.consume(10000,'영화관')
m_card1.consume(80000,'주유소')
m_card1.consume(6000,'스타벅스')
m_card1.consume(5000,'편의점')             

#%% 클래스 맴버 이해하기
""" 사원이 입사하면 입사한 사원에 대한 이메일을 자동으로생성하고 
이름을 출력하는 함수와 월급을 인상하는 함수를 담는 클래스를 생성"""


class  Employees: # ()괄호를 따로 안쓴 이유는 __init__ 함수에 입력 매개변수가 여러개 있을때는 ()을 쓰지 않는다.
    raise_amount = 1.1  # 클래스 변수( 메쏘드 밖에 생성됨 ), 클래스 변수에는 self가 없습니다.
    def __init__(self, first, last, pay): # 클래스(설계도)를 사용해서 처음 만들때 사용하는 함수
        self.first = first                # emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)
        self.last  = last                 # 위와 같이 객체(제품)를 생성할 때 입력값이 3개가 입력되면서 
        self.pay   = pay                  # 객체(제품)이 만들어 집니다.
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        print ('{} {}'.format(self.first, self.last) ) ## 앞에 중괄호 2개에 각각 self.first 와 self.last 
# print 와 return 의 차이점: return 값만 도출 print는 출력 # 에 있는 값이 입력이 됩니다.
    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * self.raise_amount)


emp_chulsu = Employees('chulsu', 'kim', 5000000)
print(emp_chulsu.pay)   # 5000000
#  객체이름.인스턴스변수이름 
emp_chulsu.apply_raise()
print(emp_chulsu.pay)  # 5500000

emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)
emp_chulsu2.raise_amount = 1.2
print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 6000000


class  Employees:
    raise_amount = 1.1  # 클래스 변수
    def __init__(self, first, last, pay): # 객체가 만들어질때
        self.first = first               # 바로 작동되는 함수
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        return  '{} {}'.format(self.first, self.last)

    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * Employees.raise_amount)  # 클래스 변수를 사용 
                        # 위의 코드는 여기에 self 였는데 지금은 클래스 이름인 Employees가 있다.
                        # 이자리에 인스턴스 변수가 아니라 클래스 변수를 썼습니다.

emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)

emp_chulsu2.raise_amount = 1.2   # 인스턴스 변수만 변경할 수 있고 클래스 변수는
                                              # 변경할 수 없다. 

print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 6000000이 아니라 55000000이 나온다!!


#%%문제174. 위에서 생성한 객체 emp_chulsu 의 email 변수에 있는 내용을 출력해보시오!

print( emp_chulsu.email ) #chulsu.kim@gmail.com

#%%문제175. 철수의 월급을 회사규정에 따라 인상시키시오!

emp_chulsu.apply_raise() # emp_chulsu 객체의 apply_raise() 메소드를 실행한다.
print (emp_chulsu.pay)        

#%%문제176. 이번에는 새로운 사원 철수2로 emp_chulsu2 객체를 생성하시오 !

emp_chulsu2 = Employees('chulsu2','kim',50000000)

#%%문제177. 철수2 사원이 월급을 인상시키기 위한 인스턴스 변수를 알아냈습니다.
#           자기는 월급이 10%인상이 아니라 20% 인상 시키고 싶어서 아래와 같이 
#           emp_chulsu2 객체의 멤버인 raise_amount 라는 변수에 1.2 를 할당하고
#           월급을 인상시키는 apply_raise() 메소드를 실행을 했다.

emp_chulsu2.raise_amount = 1.2

print( emp_chulsu2.pay )
emp_chulsu2.apply_raise()
print ( emp_chulsu2.pay)        
        
# 177 번 같이 악용이 가능하기 때문에 아래 코드와 같이 클래스 변수를 이용한다!
# 위와 같이 민감한 변수(멤버)들은 인스턴스 변수가 아니라 클래스 변수(멤버)를 
# 사용해서 계산되게 코딩해야합니다.

#  클래스내의 변수는 2개가 있는데
# 1. 클래스 변수 : 메소드 바깥의 변수
#                  객체 생성이후에 안의 값을 변경할 수 없다.
# 2. 인스턴스 변수 : 메소드 안의 변수
#                   객체 생성이후에 안의 값을 변경 할수없다.

#%% 예외 처리하기

#예제1: try ~ except 를 사용해서 예외처리를 하지 않았을때의 코드

def my_divide():
    x = input('분자의 숫자를 입력하세요 ~')       
    y = input('분모의 숫자를 입력하세요 ~')
    return int(x) / int(y) 

print(my_divide())
        
# 분자의 숫자를 입력하세요 ~10

# 분모의 숫자를 입력하세요 ~2
# 5.0

# 에러가 남
# 분자의 숫자를 입력하세요 ~10

# 분모의 숫자를 입력하세요 ~0
        
# ZeroDivisionError: division by zero 

#%% 예제2: try~ except 를 사용했을 때의 예제

def my_divide():
    try:
        x = input('분자의 숫자를 입력하세요 ~')       
        y = input('분모의 숫자를 입력하세요 ~')
        return int(x) / int(y) 
    except:
        return '고갱님~ 당황하셨죵~ 잘못된 값을 입력하셔서 나누기를 할수 없습니다.'
print(my_divide())

# 분자의 숫자를 입력하세요 ~231

# 분모의 숫자를 입력하세요 ~0
# 고갱님~ 당황하셨죵~ 잘못된 값을 입력하셔서 나누기를 할수 없습니다.

# try 와 except 사이에 코드가 잘 실행이 된다면 except 이후의 문장은 실행하지 않고
# try 와 except 사이에 코드가 실행이 안된다면 excep 이후의 문장을 실행한다.

#%%문제179. 판다스를 이용해서 emp3.csv 에서 이름과 월급을 출력하시오!

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")   
print( emp[['ename','sal']])

#%%문제180. 이름이 SCOTT 인 사원의 이름과 월급을 출력하시오!

import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")   
print( emp[['ename','sal']] [emp['ename']=='SCOTT'])

#%%문제181. input 함수를 이용해서 이름을 물어보게 하고 이름을 입력하면
# 해당 사원의 이름과 월급을 출력되게 하시오!

import pandas as pd

a = (input('이름을 대시오~'))

emp = pd.read_csv("c:\\data\\emp3.csv")   
print( emp[['ename','sal']] [emp['ename']==a])

#%% 문제182. 이번에는 소문자로 이름을 입력해도 출력되게 하시오!

import pandas as pd

a = (input('이름을 대시오~').upper())

emp = pd.read_csv("c:\\data\\emp3.csv")   
print( emp[['ename','sal']] [emp['ename']==a])

#%% 문제 183. 이번에는 위의 코드를 실행하는데 없는 사원이름을 입력하시오 !
import pandas as pd

a = (input('이름을 대시오~').upper())

emp = pd.read_csv("c:\\data\\emp3.csv")   
print( emp[['ename','sal']] [emp['ename']==a])

#%%문제184. 위의 코드에 예외처리를 해서 없는 사원이름을 입력하면 입력하신 
# 이름의 사원은 존재하지 않습니다. 라는 메세지가 출력되게 하시오! 


import pandas as pd

a = (input('이름을 대시오~').upper())

emp = pd.read_csv("c:\\data\\emp3.csv")
if a in emp['ename']:
    print( emp[['ename','sal']] [emp['ename']==a])
else:
    print('입력하신 이름의 사원은 존재하지 않습니다.')
    
# 설명: try~ except 로는 할수 없다. 오직 에러났을때만을 통해서 해야한다.

#%%문제185. 숫자를 입력하면 해당 숫자의 제곱값이 출력되는 코드를 구현하시오~
# 숫자를 입력하세요~ 2

def jegob(num):
    return print(num**2)

jegob(int(input('숫자를 입력하세요~')))

#%%문제186. try~ except 예외처리를 이용해서 아래와 같이 문자를 입력하면 
#  '잘못된 값을 입력하셨습니다' 라는 메세지가 출력되게 하시오!

def jegob():
    try: 
        num  = int(input('숫자를 입력하세요~'))
        print(num**2)
    except:
        print('잘못된 값을 입력하셨습니다.')
        
jegob()

# 설명: try 와 except 사이의 있는 코드에서 에러가 나야지만 except 이후의 문장을 실행합니다.

#%% try~ except~ else

try: 
    num  = int(input('숫자를 입력하세요~'))
    print(num**2)
except:
    print('잘못된 값을 입력하셨습니다.')
else:
    print('결과 출력에 성공했습니다.')
    
# 설명: try~ except 사이의 코드에 에러가 안났다면 else: 이후의 문장을 실행합니다.
    
#%%문제187. 아까 했던 나누기 프로그램을 수정해서 나누기가 성공하면 
# 성공적으로 나누기를 하였습니다. 라는 메세지가 출력되게하시오.

def my_divide():
    try:
        x = input('분자의 숫자를 입력하세요 ~')       
        y = input('분모의 숫자를 입력하세요 ~')
        print( int(x) / int(y) ) 
    except:
        print( '고갱님~ 당황하셨죵~ 잘못된 값을 입력하셔서 나누기를 할수 없습니다.' )
    else:
        print( '성공적으로 나누기를 하셨네요~' )

my_divide()
#%% 문제187 번 비교
#비교
def my_divide():
    try:
        x = input('분자의 숫자를 입력하세요 ~')       
        y = input('분모의 숫자를 입력하세요 ~')
        return int(x) / int(y) 
    except:
        return '고갱님~ 당황하셨죵~ 잘못된 값을 입력하셔서 나누기를 할수 없습니다.'
    else:
        print( '성공적으로 나누기를 하셨네요~' )
print(my_divide())
#설명: return 이 들어간 함수로는 함수 하나당 return 값은 한개만 출력되기 때문에 정상 작동 하지 않는다.

#%% try~ except~ finally~
try:
    print('안녕하세요~')
except:
    print('예외가 발생했습니다.')
finally:
    print('저는 무조건 실행됩니다')


#%%문제188. 나누기하는 프로그램을 실행할 때 오류가 나던 오류가 나지 얺던 무조건 아래의 메세지가 출력되게 하시오!

def my_divide():
    try:
        x = input('분자의 숫자를 입력하세요 ~')       
        y = input('분모의 숫자를 입력하세요 ~')
        print( int(x) / int(y) ) 
    except:
        print( '고갱님~ 당황하셨죵~ 잘못된 값을 입력하셔서 나누기를 할수 없습니다.' )
    else:
        print( '성공적으로 나누기를 하셨네요~' )
    finally:
        print('권세원이 만든 나눗셈이에용~')
my_divide()

#%%문제189. 동전을 10번 던져서 앞면이 2번 나올 확률을 출력하세요 !
#           (동전을 10번 던지는 작업을 10000 번 수행되게 하시오)

import random as r

coin = ['앞','뒤']

cnt2= 0
cnts= 0

for j in range(10000): 
    cnt = 0   
    for i in range(10):
        result = r.choice(coin)
        if result == '앞':
            cnt += 1
    if cnt == 2:
        cnt2 += 1
    cnts += 1

print(cnt2/cnts)

#%% append를 이용한 방법~

import random as r

coin = ['앞','뒤']

cnt2= 0
cnts= 0

for j in range(10000): 
    a = []  
    for i in range(10):
        result = r.choice(coin)
        a.append(result)
    if a.count('앞') == 2:
        cnt2 += 1
    cnts += 1

print(cnt2/cnts)

#%%문제190. (오늘의 마지막 문제) 위의 코드를 함수로 생성하여 확률이 출력되게 하시오!

# coin_prob(2) # 0.04314
# coin_prob(4) # 0.2065

# 앞면의 갯수
import random as r

coin = ['앞','뒤']


def coin_prob(num):
    try:
        coin = ['앞','뒤']
        cnt2= 0
        cnts= 0    
        for j in range(10000): 
            a = []  
            for i in range(10):
                result = r.choice(coin)
                a.append(result)
            if a.count('앞') == num:
                cnt2 += 1
            cnts += 1
        print(cnt2/cnts)
    except:
        print('0과 10000 사이의 정수를 넣어주세요')
        
coin_prob(2)
coin_prob(4)    
