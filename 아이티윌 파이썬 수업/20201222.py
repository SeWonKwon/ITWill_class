# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:32:50 2020

@author: bigne
"""
#%%이미지 
# 예제1. 이미지 파일 리스트를 가져오시오.
import os

test_image='c:\\images\\lungs'

def image_load(path):
    file_list = os.listdir(path) # 해당 디렉토리의 파일명을 추출한다.
    return file_list

print(image_load(test_image))

# 예제2. 위의 결과에서 숫자만 나오게 함수의 코드를 수정하시오!
a = []
for i in image_load(test_image):
    a.append(int(i.replace('.png','')))
a=sorted(a)


#%%선생님 방법.
import re
import os
def image_load(path):
    file_list = os.listdir(path) # 해당 디렉토리의 파일명을 추출한다.
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) # i 의 값중에서 숫자가 아닌것들은 싱글 두개 붙인것으로 인 null로 변경해라~
        file_name.append(a)
    file_name
    return file_name
print(image_load(test_image))

#%%문제475. 위에서 출력되고 리스트 안의 요소들은 문자입니다. 그런데 문자가 아니라 리스트의 요소들이 숫자가 되게 하세요~
import os
import re

def image_load(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    return file_name
print(image_load(test_image))

#%%문제476. 위의 리스트의 요소가 asceding 하게 정렬되게 하시오~
import os
import re

def image_load(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    file_name.sort()
    return file_name

print(image_load(test_image))

#%%문제477. 원래 이름대로 넣어 주어야 한다. 위의 함수의 코드를 추가해서
# 아래와 같이 출력되게 하시오!
# ['1.png','2.png',....,'20.png']
import os
import re

def image_load(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append(str(k)+'.png')
    return file_res

print(image_load(test_image))

#%%문제478 위의 함수의 코드를 수정해서 아래와 같이 이름 앞에 절대경로가 붙게 하시오!
# ['c:\\images\\lungs\\1.png', 'c:\\images\\lungs\\2.png',...,'c:\\images\\lungs\\20.png']
import os
import re

test_image='c:\\images\\lungs\\' 

def image_load(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append(test_image+str(k)+'.png')
    return file_res

print(image_load(test_image))

#%%예제3. 폐사진 이미지를 숫자로 변환하기 위하여 필요한 파이썬 모듈을 install 하시오.
# conda install opencv
# 위의 명령어로 했을 때 에러가 나면 아래와 같이 하세요!
# pip install opencv-python

# 설명: opencv 모듈은 이미지를 파이썬에서 숫자로 변환하고 다양한 이미지 처리를 할 수 있게 해주는 기술을 제공해주는 함수

# 예: 구글지도나 카카오 지도, 네이버 지도에 보면 street view 가 있는데 거기에 사람얼굴이나 자동차 번호판을 모자이크 처리를 해줘야합니다.

#%%예제4. 위에서 설치한 opencv 모듈을 이용해서 폐사진을 숫자로 변환한다.

import cv2 # opencv 모듈을 임폴트 하겠다.
import os
import re # 데이타 정제를 전문으로 하는 모듈

test_image='c:\\images\\lungs\\' 

def image_load(path):
    file_list = os.listdir(path) 
    
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    file_name.sort()
    
    file_res=[]
    for k in file_name:
        file_res.append(test_image+str(k)+'.png')
        
    image = []
    for h in file_res:
        img = cv2.imread(h) # 이미지를 숫자로 변환하는 코드 
        image.append(img)
    return image
    
    # return file_res

print(image_load(test_image))

#%%예제5. 위의 숫자로 변환한 리스트를 신경망에 넣기 위해서는 numpy 모듈의 array 형태로 제공을 해줘야 합니다.
# 위의 리스트를 numpy array 로 변환합니다.

import numpy as np # 행렬 연산을 쉽고 빠르게 할 수 있게 해주는 모듈
import cv2 # opencv 모듈을 임폴트 하겠다.
import os
import re # 데이타 정제를 전문으로 하는 모듈

test_image='c:\\images\\lungs\\' 

def image_load(path):
    file_list = os.listdir(path) 
    
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    file_name.sort()
    
    file_res=[]
    for k in file_name:
        file_res.append(test_image+str(k)+'.png')
        
    image = []
    for h in file_res:
        img = cv2.imread(h) # 이미지를 숫자로 변환하는 코드 
        image.append(img)
    return np.array(image, dtype=object)
    
print(image_load(test_image))
#%%예제1
# 예제2 강아지 사진 30장만 c 드라이브 밑에 images2 라는 폴더에 넣으세요.

# 예제3. c 드라이브 밑에 images2 라는 폴더에 있는 이미지 이름을 가져오는 함수를
# image_load2 라는 함수로 생성하시오!

import os
path = "c:\\images2\\"

def image_load2(loc):
    file_list = os.listdir(loc)
    return file_list

print(image_load2(path))






#%%예제6. 아래와 같이 절대경로와 확장자가 붙어서 출력되게 하시오!
# ['c:\\images2\\dog.1.jpg', 'c:\\images2\\dog.2.jpg',...,'c:\\images2\\dog.30.jpg']
import os
import re

test_image='c:\\images2\\' 

def image_load2(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append(test_image+'dog.'+str(k)+'.jpg')
    return file_res

print(image_load2(test_image))

#%%예제7. 위의 개사진 이미지들을 opencv와 numpy 를 이용해서 숫자로 변환하고 numpy array 로 반환되게 하시오 !
import os
import re

test_image='c:\\images2\\' 

def image_load2(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a = re.sub('[^0-9]','',i) 
        file_name.append(int(a))# int!
    file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append(test_image+'dog.'+str(k)+'.jpg')
    
    images = []
    for h in file_res:
        img = cv2.imread(h)
        images.append(np.array(img))
    return images
    

print(image_load2(test_image))

#%%문제480.(점심시간 문제) 지난번에 여러분들이 직접 스크롤링한 사진 20장을 c 드라이브 밑에 images3 에 넣고 숫자로 변환하는 함수를
# image_load3 로 생성하시오!

#전기수의 예: 스킨스쿠버를 취미인 학생(보라)
# 바닷속에 자연보호를 위해서 비닐사진과 해파리 사진을 다운 받아 비닐사진과 해파리 사진을 분류하는 인공신경망을 생성하는 포트폴리오를 생성


#%%알고리즘

# 합성곱 문제481. 아래의 두 행렬을 만들고 덧셈 연산을 하시오 !

# 123             201
# 012      +      012
# 301             102

a = [[1,2,3],[0,1,2],[3,0,1]]
b = [[2,0,1],[0,1,2],[1,0,2]]

import numpy as np
a2 = np.array(a)
b2 = np.array(b)
# print(a2,b2)
print(a2+b2)
#%%문제482. 아래의 두 행렬을 만들고 두행렬의 원소들의 곱을 구하시오 !

# 123             201
# 012      *      012
# 301             102

import numpy as np

a = [[1,2,3],[0,1,2],[3,0,1]]
b = [[2,0,1],[0,1,2],[1,0,2]]

a2 = np.array(a)
b2 = np.array(b)
# print(np.dot(a2,b2)) 행렬의 곱
print( a2 * b2)

#%%문제483. 위에서 원소들의 곱으로 출력된 결과인 3x3 행렬의 요소들을 모두 다 더하시오 !


import numpy as np

a = [[1,2,3],[0,1,2],[3,0,1]]
b = [[2,0,1],[0,1,2],[1,0,2]]

a2 = np.array(a)
b2 = np.array(b)

c = a2*b2
print(np.sum(c))

# 설명: numpy란 ? python 언어에서 기본적으로 지원하지 않는 배열(array) 혹은
#               행렬(matrix) 의 계산을 쉽게 해주는 라이브러리 입니다. 머신러닝에서 많이 사용하는 
#               선형대수학에 관련되 수식들을 python 에서 쉽게 프로그래밍 할 수 있게 해줍니다.

#%%문제484. 아래의 4x4 행렬을 만드시오!

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]

a = np.array(a)

#%%문제485. 아래의 4x4 행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오.
# 설명: 행이 1부터 3까지 열도 1부터 3까지

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]

a = np.array(a)

print(a[0:3,0:3]) # [행,렬]

#%%문제486. 아래의 4x4행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오.

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]

a = np.array(a)

print(a[0:3,1:4]) # [행,렬]

#%%문제486. 아래의 4x4행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오.

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]

a = np.array(a)

print(a[1:4,0:3]) # [행,렬]

#%%문제486. 아래의 4x4행렬에서 빨간색으로 지정한 영역의 숫자들만 출력하시오.

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]

a = np.array(a)

print(a[1:4,1:4]) # [행,렬]

#%%문제489. 아래의 4x4 행렬에서 위에서 빨간색으로 지정된 4개의 영역의 숫자들을 for loop 문을 이용해서 모두 출력하시오.

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]

aa = np.array(a)

for a,b,c,d in zip([0,0,1,1],[0,0,1,1],[0,1,0,1],[0,1,0,1]):
    # print(aa[(0+a):(3+b),(0+c):(3+d)])
    print(a,b,c,d)
    print(a,a,c,c)
    
#%% 4차 정사각 행렬이 3차 필터를 만났을때 는 4가지의 경우의 수 2*2
#5차가 4차를 만나면 똑같이 4가지 2*2
#5차가 3차를 만나면 9가지 3*3
                  (a,b)
print(a[0:3,0:3]) (0,0)
print(a[0:3,1:4]) (0,1) 
print(a[1:4,0:3]) (1,0)
print(a[1:4,1:4]) (1,1)
#%%



#%%문제490. 위에서 선택한 4개의 행렬(3x3) 과 아래의 filter 행렬(3x3)과의 원소의 곱을 출력하시오!
import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
filter = [[2,3,4],[1,2,3],[2,0,1]]

aa = np.array(a)
filter = np.array(filter)

for i, k in zip(range(0,2), range(3,5)):
    for j, h in zip(range(0,2), range(3,5)):
        print(aa[i:k,j:h]*filter)

#%%문제491. 위에서 출력된 3x3 행렬 4개에 대한 원소들의 합이 각각 출력되게 하시오.

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
filter = [[2,3,4],[1,2,3],[2,0,1]]

aa = np.array(a)
filter = np.array(filter)

for i, k in zip(range(0,2), range(3,5)):
    for j, h in zip(range(0,2), range(3,5)):
        print(np.sum(aa[i:k,j:h]*filter))
        
#%%492.

import numpy as np

a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
filter = [[2,3,4],[1,2,3],[2,0,1]]

aa = np.array(a)
filter = np.array(filter)

result=[]
for i, k in zip(range(0,2), range(3,5)):
    for j, h in zip(range(0,2), range(3,5)):
        result.append(np.sum(aa[i:k,j:h]*filter))
result2 = np.array(result).reshape(2,2)
print(result2)
# 설명: aa 라는 원본 이미지(개사진)에 filter (랜덤으로 생성한 이미지)를 가지고 원본이미지를
#  스트라이드(양옆위애라로 스캔) 하면서 특징을 잡아내어 특징 이미지를 추출(result2) 하는것을
# 합성곱이라고 합니다.

#%%문제493. 아래의 원본 이미지 행렬(5x5) 행렬에서 필터행렬(4x4)로 스트라이딩 해서 
# 합성곱해서 특징을 추출하시오 ~

import numpy as np

a = [[2,3,1,4,7],[3,1,6,4,3],[2,1,5,3,1],[6,2,4,1,2],[7,3,1,2,3]]
filter = [[3,1,4,1],[2,3,3,4],[5,1,2,1],[6,1,3,4]]

aa = np.array(a)
filter = np.array(filter)

result=[]
for i, k in zip(range(0,2), range(4,6)):
    for j, h in zip(range(0,2), range(4,6)):
        result.append(np.sum(aa[i:k,j:h]*filter))
result2 = np.array(result).reshape(2,2)
print(result2)

#%%문제494. 아래의 리스트에서 숫자 3이 있는지 순차 탐색으로 구현하시오 !
# 있으면 숫자 3이 있습니다. 라는 메세지가 출력되게 하시오!
a = [15,11,1,3,8]

for i in a: 
    if i == 3:
        print ('숫자 3 이 있습니다.')
        break
else:
    print('숫자 3이 없습니다.')
        
# 설명: 순차 탐색이란 ? 주어진 데이터를 처음부터 차례대로 비교하면서 찾는 방법.
    
#%%문제495. 위의 코드를 수정해서 숫자를 물어보게 하고 숫자를 입력하면
# 해당 숫자가 존재하는지 존재하지 않는지가 출력되게 하시오!

# 검색할 숫자를 입력하세요~ 3

a = [15,11,1,3,8]
n=int(input('검색할 숫자를 입력하세요~'))
for i in a: 
    if i == n:
        print ('숫자'+str(n)+' 이 있습니다.')
        break
else:
    print('숫자' +str(n)+' 이 없습니다.')
# =============================================================================
#  이진탐색? 정렬된 데이터를 좌우 둘로 나눠서 원하는 값의 탐색범위를 좁혀가며 찾는 방법.
# =============================================================================
#%%문제496. 아래의 a 리스트에서 중앙값을 찾으시오!
# a = [1,7,11,12,14,23,33,47,51,64,77,149,672, 871]
a = [1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871]
import numpy as np
a_n = np.array(a)
print(np.median(a_n))
#%%문제497. a 리스트에서 첫번째 숫자 부터 중앙값에 해당하는 숫자 까지만 검색하시오~
a = [1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871]
import numpy as np
a_n = np.array(a)
a_m = np.median(a_n)

print(a[:a.index(a_m)+1])

#%%문제498. 위의 a 리스트에서 문제 497번에서 선택된 숫자들을 중앙값까지 포함해서 다 지우고
#아래의 결과만 출력되게 하시오 !
# a= [51, 64, 67, 77, 139, 672, 871]
a = [1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871]
import numpy as np
a_n = np.array(a)
a_m = np.median(a_n)

del(a[:a.index(a_m)+1])
print(a)

#%%문제499. 위의 결과로 출력된 아래의 리스트에서 중앙값을 출력하시오 !
a = [1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871]
import numpy as np
a_n = np.array(a)
a_m = np.median(a_n)

del(a[:a.index(a_m)+1])
print(a)
a_n = np.array(a)
a_m = np.median(a_n)
print(a_m)

#%%문제500. 지금 위에서 출력한 중앙값 77이 내가 검색하고자 하는 67보다 크다면 아래의 결과 리스트만 출력되게 하시오
a = [1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871]
import numpy as np
a_n = np.array(a)
a_m = np.median(a_n)

del(a[:a.index(a_m)+1])
a_n = np.array(a)
a_m = np.median(a_n)
print(a_m)

if a_m > 67:
    del(a[a.index(a_m):])
else:
    del(a[:a.index(a_m)])
print(a)

#%%문제501. (오늘의 마지막 문제) EBS에 나온 영상데로 이진 탐색 을 구현하시오

# a 리스트에서 검색할 숫자를 입력하세요 ~

# 67은 이진탐색 3번만에 검색되었습니다.

# a 리스트에서 검색할 숫자를 입력하세요 ~

# 68은 리스트 안에 없습니다.

a = [1, 7, 11, 12, 14, 23, 871, 47, 51, 64, 67, 77, 139, 672,33]
import numpy as np
a = sorted(a)
a_n = np.array(a)
a_m = np.median(a_n)
print(a_m) # 47
print(a) # [1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 139, 672, 871]
print(len(a)) # 15
del(a[:8]) 

a_n = np.array(a)
a_m = np.median(a_n)
print(a_m)  # 77
print(a) # [51, 64, 67, 77, 139, 672, 871]
print(len(a)) # 7
del(a[3:])

a_n = np.array(a)
a_m = np.median(a_n)
print(a_m) #  64
print(a) # [51, 64, 67]
print(len(a)) # 3
del(a[:2])

a_n = np.array(a)
a_m = np.median(a_n)
print(a_m)

print(a) # [67]
print(len(a))  # 1 
a_n = np.array(a)
a_m = np.median(a_n)
print(a_m)
#%%
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
#a = [1, 7, 11, 12, 14, 23, 871, 47, 51, 64, 67, 77, 139, 672, 33, 23, 87, 34, 1, 4, 1232]
import numpy as np

num = int(input('a 리스트에서 찾고 싶은 숫자를 입력하세요~'))
a= set(a)
a = list(a) # 중복제거
a = sorted(a)

n= 0
while len(a)>1: # 중간값의 인덱스를 이용하면 중간 값이 없는 경우가 생기기 때문에 리스트의 갯수를 이용
    a_n = np.array(a)
    a_m = np.median(a_n)
    n+=1
    print(a_m) 
    print(a) 
    print(len(a))
    if a_m < num:
        del(a[:int((len(a)+1)/2)]) # 중간값과 비교후 갯수를 이용하여 인덱스 지정해준다.
    elif a_m > num:
        del(a[int((len(a)-1)/2):])
    else: # 중간값과 찾으려는 값이 같은 경우에는 항상 중간값보다 작은쪽에 존재 한다.4
        a= a[int((len(a)-1)/2)-1:int((len(a)-1)/2)+1]
if a[0]==num: # a 리스트의 마지막에 남은 숫자가 가장 근접한 숫자이므로 비교해준다.(중복제거 되었을시에만)
    print(str(num)+'이진탐색'+str(n)+'번만에 검색되었습니다.') # 67은 이진탐색 3번만에 검색되었습니다.
else: 
    print('없어요')
#%% 
n=0
while len(a)>2:
    a_m = np.median(a_n)
    a_n = np.array(sorted(a))
    print(a)
    print(n)
    print(a_m)
    n+=1
    if a_m > 67:
        del(a[a.index(a_m):])
    else:
        del(a[:a.index(a_m)])
print(a)




#%%

del(a[:a.index(a_m)+1])
a_n = np.array(a)
a_m = np.median(a_n)
print(a_m)

if a_m > 67:
    del(a[a.index(a_m):])
else:
    del(a[:a.index(a_m)])
print(a)


#%%한결이 코드

import numpy as np

a = [1, 7, 11, 12, 14, 23, 871, 47, 51, 64, 67, 77, 139, 672, 33, 23, 87, 34, 1, 4, 1232]
a= set(a)
a = list(a) # 중복제거
a = sorted(a)
b = str(67)

cnt = 1

finish=0

 

if int(b[-1]) in [1,3,6,7,8,0]: # '은/는' 불편해서 만듦

    d = '은'

else:

    d = '는'

b = int(b)

 

while True:

    a_m = round((len(a)-1)/2)


    if b == a[a_m]:

        print(f'{b}{d} 이진탐색 {cnt}번만에 검색되었습니다.')

        break

    elif b > a[a_m]:

        cnt +=1

        del(a[:a_m+1])

    else:

        cnt +=1

        del(a[a_m:])

    if len(a) == 0:

        print(f'{b}{d} 검색되지 않았습니다.')

        break
#%%
# a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a = [1, 7, 11, 12, 14, 23, 871, 47, 51, 64, 67, 77, 139, 672, 33, 23, 87, 34, 1, 4, 1232]
import numpy as np

num = int(input('a 리스트에서 찾고 싶은 숫자를 입력하세요~'))
a= set(a)
a = list(a) # 중복제거
a = sorted(a)

n= 0
while len(a)>1: # 중간값의 인덱스를 이용하면 중간 값이 없는 경우가 생기기 때문에 리스트의 갯수를 이용
    a_n = np.array(a)
    a_m = a[int((len(a)-1)/2)]
    n+=1
    print(a_m) 
    print(a) 
    print(len(a))
    if a_m < num:
        del(a[:int((len(a)+1)/2)]) # 중간값과 비교후 갯수를 이용하여 인덱스 지정해준다.
    elif a_m > num:
        del(a[int((len(a)-1)/2):])
    else: # 중간값과 찾으려는 값이 같은 경우에는 항상 중간값보다 작은쪽에 존재 한다.4
        a= a[int((len(a)-1)/2)-1:int((len(a)-1)/2)+1]
if a[0]==num: # a 리스트의 마지막에 남은 숫자가 가장 근접한 숫자이므로 비교해준다.(중복제거 되었을시에만)
    print(str(num)+'이진탐색'+str(n)+'번만에 검색되었습니다.') # 67은 이진탐색 3번만에 검색되었습니다.
else: 
    print('없어요')

#%%156 재귀 알고리즘
# 
# 
# 재귀 알고리즘은 처음에는 이해하기가 어려운 알고리즘이지만 많이 연습해서 잘 알아두면 loop문을 최소화 하면서 코드를
# 간단하게 작성할 수 있는 알고리즘입니다.

# 1. 재귀함수란? 반복문 + 스택구조가 결합된 함수 입니다.
#                         후입선출
#                         관련 동영상 감상

# 2. 재귀 함수의 특징?

# 재귀함수는 함수 내에서 다시 자기 자신을 호출한 후 그 함수가 끝날때 까지 함수 호출 이후의 명령문을 수행하지 않습니다.

# 3. 함수내에서 다른 함수를 호출하는 예제

def hap(a,b):
    return(a+b)

def gob(a,b):
    return (a*b)

def hap_gob(a,b):
    k = hap(a,b)
    m = gob(a,b)
    return k + m

print(hap_gob(2,3))
#%%4. 숫자를 입력하면 1부터 해당숫자까지의 합을 출력하는 함수를 생성하시오.

# print(add_func(5))

# 결과: 15

def add_func(num):
    return sum(range(num+1))

print(add_func(5))
#%%5. 위의 add_func 함수를 재귀함수로 구현하시오 !
# (재귀함수를 사용하면 loop문을 사용하지 않아도 됩니다.)

def add_func(n):
    if n == 0:
        return 0
    else:
        return n +add_func(n-1)

print(add_func(5))

#%%512. factorial 함수를 만드시오.

def fac_func(n):
    if n == 1:
        return 1
    else:
        return n*fac_func(n-1)

print(fac_func(5))
#%%문제513. 위의 factorial 함수를 재귀를 이용하지 말고 for loop 문으로 구현하시오!

def fac_func(n):
    a=1
    for i in range(1,n+1):
        a = a*i
    return a

print(fac_func(5))

# 재귀를 이용하면 2가지 장점?
# 1.loop문을 복잡하게 이용하지 않아도 됩니다.
# 2. 코드가 더 간결해 집니다.


#%%문제514. 오라클의 power 함수를 파이썬으로 구현하시오!

# SQL > select power(2,3) from dual; # 8 

def power(a,b):
    c=1
    for i in range(b):
        c = c*a
    return c
print(power(2,3))

print(2**3)

#%% 문제515.위의 power 함수를 loop문을 쓰지 말고 재귀 함수로 구현하시오!

def power(a,b):
    if b == 1:
        return a
    else:
        return a*power(a,b-1)
    
print(power(2,3))

#%% 문제516. 구구단 2단을 아래와 같이 출력하는 함수를 생성하시오!
# (for loop 문 사용해서 만드세요!)

# print( multi_table_2dan(9))

# 2 x 1 = 2
# 2 x 2 = 4

def multi_table_2dan(num):
    for i in range(1,num+1):
        print('2 x', str(i),' = ', 2*i)
    

multi_table_2dan(9)

#%%문제517. 두 숫자를 각각 입력해서 함수를 실행하면 두 숫자의 최대공약수가 출력되는 함수를 생성하시오! ( 재귀함수 사용하지 않고 loop 문 이용해서 하세요)

# print(gcd(16,24))

# 8

def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a% i == 0 & b%i ==0:
            return i
        
print (gcd(16,24))
        
#%%문제518. (필수 알고리즘 ) 5번째 최대공약수를 출력하는 함수를 재귀함수로 구현하시오~~~

def gcd(a,b):
    a2 =a
    b2= b
    i = min(a2,b2) 
    if a% i == 0 & b%i ==0:
        return i
    else:
        return gcd(a2-1,b2)

print (gcd(36,24))

# 오류 a 값이 같이 변하면서 서로 소수이면 답이 틀리게 나옮

#%% 오류 수정.

def gcd(a,b,c=True):
    
    a,b = min(a,b),max(a,b)
    i=a
    print(a+c-1,b,i,c)
    if (a+c-1)% i == 0 and b%i ==0:
        return i
    else:
        return gcd(a-1,b,c+1)
    
print (gcd(24,36))
#%%승순이 코드
ef gcd(n1,n2): 
    if n2 == 0:
        return n1  #
    else:
        return gcd(n2, n1%n2)
    
print(gcd(16,24))    

#%%



'유클리드 호제법' 활용한 함수 (위키트리 정의)
a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
즉, n1 < n2 일때, n1, n2의 최대공약수 = n2, n2/n1의 나머지 사이의 최대공약수와 같음.

예시)
1071과 1029의 최대공약수를 구하면,

1071은 1029로 나누어떨어지지 않기 때문에, 1071을 1029로 나눈 나머지를 구한다. ≫ 42
1029는 42로 나누어떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구한다. ≫ 21
42는 21로 나누어떨어진다.

 


n1 = 16, n2 = 24

n2 = 24 != 0 이므로 else 조건 적용

1) gcd(24, 16%24) -> n2 = 16%24 -> 16 
       2)  gcd(24, 16) // n2 = 16 //  16은 !=0 이므로 else 조건 gcd(16,24%16) -> n2 = 24%16 -> 8 ->gcd(16,8) 
           3)  gcd(16,8) // n2 = 8 //  8은 != 0 이므로 else 조건 gcd(8, 16%8) -> n2 = 16%8 ->  0 ->gcd(8,0) 
               4)  gcd(8,0)  // n2 = 0 이므로 if 조건 만족 n1인 8 return

 

#%%157. 필수 알고리즘6(LRU 알고리즘)
#Least Recent Used
#LRU 알고리즘이란 Oracle DATABASE의 메모리 관리를 효율적으로 하기 위해서 고안된 대표적인 알고리즘으로 최신 데이터를 메로이에
#유지시키고 오래된 데이터는 메모리에서 내보내게 하는 알고리즘.

#메모리에서 조회하게되면 1초가 걸린다. ==> cache hit
#메모리에 없어서 디스크에서 조회를 하면 5초가 걸린다. ==> cache miss

# 한번 디스크에서 읽은 데이터를 메모리에 올려놓고 메모리에서 빠르게 데이터를 조회할 있도록 LRU 알고리즘을 구현해서 만든 소프트웨어 입니다.
# 그런데 이 메모리 공간이 한정된 공간이다 보니 무한히 데이터를 올릴 수 없어서 오래된 데이터는 메모리에서 빠져나가게 되고
# 최신 데이터가 그 빠져나간 자리에 올라가게 됩니다.
# 최근에 내가 검색한 데이터는 다시 검색할 확률이 높은 데이터 이므로 메모리에 오래 두도록 하고 예전에 검색한 데이터는 메모리에서 빠져나가게 합니다.

# 스택: 후입선출
# 큐 : 선입선출

#%%문제519. 오늘의 마지막 문제 구구단 2단을 재귀 함수로 출력하시오 !
def multi_table_2dan(num):
    for i in range(1,num+1):
        print('2 x', str(i),' = ', 2*i)
#%%
def multi_table_2dan(num,a=1):
    if a == num+1:
        return
    else:
        n=a
        print('2 x', str(n),' = ', 2*(n))
        n=num
        multi_table_2dan(n,a+1)

multi_table_2dan(5)


#%%


def multi_table_2(n):
    if n == 0:
        return               # 함수를 종료시키기 위해 사용
    else:
        multi_table_2(n-1)
        print('2 x ', n, '=', 2 * n)
        
multi_table_2(6)
