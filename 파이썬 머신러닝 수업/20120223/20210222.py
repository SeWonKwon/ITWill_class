#%% 

import pandas as pd  # 데이터 전처리
import seaborn as sns # 시각화를 위해서 
import numpy as np

df = pd.read_csv("C:\\data\\wisc_bc_data.csv") 
# 설명 : R 과는 다르게 stringsAsFactors = True 를 지정하지 않아도 됩니다. 
pd.set_option('display.max_columns', 500)# 출력창 설정

# DataFrame 확인
print(df.shape) # raw와 columns
print(df.info()) #  R의 str(df)
print(df.describe()) # R에서의 summary(df) 의 결과와 유사합니다. 
#%%
# 행을 선택하는 방법 emp[행][열] --> emp[조건][컬럼명]
print(df.iloc[0:5, ]) 
print(df.iloc[-5: ,])

# 열을 선택하는 방법
print(df.iloc[ :, [0,1] ]) 
print(df.iloc[ :, : ]) 
#%%
판다스 데이터 프레임이 어떻게 구성되었는가? 

게시글 19번 
numpy 리스트 (일반 리스트) 로 컬럼 하나를 구성 --> 시리즈
numpy 리스트 (일반 리스트) 로 컬럼 여러개를 구성 --> 데이터 프레임
#%%데이터 전처리 : 정규화 ---> 훈련과 테스트로 데이터를 분리

# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = df.iloc[:, 2:].to_numpy() # df 데이터 프레임의 2번째 열부터 끝까지를 넘파이로array로
# print(X)         
y = df['diagnosis'].to_numpy()   
print(y)


#%%
# 데이터 정규화를 수행한다. 
# 1. 스케일(scale) : 평균은 0이고 표준편차 1인 데이터로 분포 시킴
# 2. min/max 정규화 : 0~1 사이의 숫자로 변경
# 아래의 코드는 min/max 정규화는 아니고 scale 입니다.
#%%        
from sklearn import preprocessing 
X=preprocessing.StandardScaler().fit(X).transform(X) 

from sklearn.model_selection import train_test_split 
                                                                
                     
# 훈련 데이터 70, 테스트 데이터 30으로 나눈다. 4개의 인자값
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.3, random_state = 10)
# 설명: test_size=0.3 으로 했기때문에 훈련과 테스트가 7대 3 비율로 나뉩니다. 
# random_state = 10 은 seed 값 설정 하는 부분입니다. 


print(X_train.shape) 
print(y_train.shape) 

#%%

# 스케일링(z-score 표준화 수행 결과 확인)
for col in range(4):
    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
for col in range(4):
    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')

#%%
# 학습/예측(Training/Pradiction)
from sklearn.neighbors import KNeighborsClassifier

# k-NN 분류기를 생성 # n_neighbors= 가 k 값
classifier = KNeighborsClassifier(n_neighbors=5)

# 분류기 학습
classifier.fit(X_train, y_train) # 훈련 데이터와 훈련 데이터의 라벨로 훈련을 한다. 

# 예측
y_pred= classifier.predict(X_test) # 테스트 데이터를 예측한다. 
print(y_pred)
#%%
# 모델 평가
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    # 이원 교차표

# 민감도, 재현율, F1스코아 
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy) # 0.964912

#%% 문제1. 위의 코드에서 적절한 k 값을 알아내는 for 문을 구현하세요
# $ graph
errors = []
for i in range(1, 31):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    errors.append(np.mean(pred_i != y_test))
print(errors)
#%%
for k,i in enumerate(errors):
    print(k, '--->',i)

import matplotlib.pyplot as plt

plt.plot(range(1, 31), errors, marker='o')
plt.title('Mean error with K-Value')
plt.xlabel('k-value')
plt.ylabel('mean error')
plt.show()
#%% 문제2. 위에서 알아낸 가장 에러가 낮은 k 값은 7,8,9,10 이었습니다. 
            # 그러면 k 값을 7을 넣었을때의 정확도를 보시오~
            
classifier = KNeighborsClassifier(n_neighbors=7 ) # 로 수정한후 코드

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy) #0.97

#설명: 0.97 의 정확도가 나옵니다. 의료 데이터이므로 정확도가 아주 높아야 합니다. 그런데
# 정확도가 100%가 나오면 좋겠는데 100% 의 정확도가 나오기 어려우므로 FN을 0으로 만들면
# 정확도가 100%가 아니더라도 쓰겠다. 
# FN -> False Negative 
# 관심범주는 positive (암) 이므로 Negative 는 정상환자입니다.
# False Negative --> 암환자를 정상환자로 잘못 예측했다. 
#%%문제3. 위의 코드에서 적절한 k 값을 알아내는 for 문을 구현하세요.
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np


acclist = []
err_list = []
fn_list = []

for i in range(1,30):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
    fn_list.append(fn)
    acclist.append(accuracy_score(y_test, y_pred))
    err_list.append(np.mean(y_pred != y_test))

    print(f'k : {i} , acc : {accuracy_score(y_test, y_pred)} , FN : {fn}')



#%%
plt.figure(figsize=(12,6))
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=1, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)

plt.subplot(131) # 추가로 그래프를 그린다. 
plt.plot(acclist,color='blue', marker='o', markerfacecolor='red')
plt.title('Accuracy', size=15)
plt.xlabel("k value")
plt.ylabel('Accuracy')

plt.subplot(132)
plt.plot(err_list, color='red', marker='o', markerfacecolor='blue')
plt.title('Error', size=15)
plt.xlabel("k value")
plt.ylabel('error')

plt.subplot(133)
plt.plot(fn_list, color='green', marker='o', markerfacecolor='yellow')
plt.title('FN Value', size=15)
plt.xlabel("k value")
plt.ylabel('fn value')

plt.show()

#%% 문제4.  iris 데이터를 knn 으로 분류하세요 ! 

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import pandas  as pd

# 1. 데이터 준비
col_names = ['sepal-length', 'sepal-width','petal-length', 'petal-width','Class']

# csv 파일에서 DataFrame을 생성
dataset = pd.read_csv('c:\\data\\iris2.csv', encoding='UTF-8', header=None, names=col_names)
#print(dataset)

# print(dataset.head(20))
df= dataset
X = df.iloc[:, :-1].to_numpy() # df 데이터 프레임의 2번째 열부터 끝까지를 넘파이로array로
# print(X)         
y = df['Class'].to_numpy()   
# print(y)

#%%        
from sklearn import preprocessing 
X=preprocessing.StandardScaler().fit(X).transform(X) 

from sklearn.model_selection import train_test_split 
                                                                
                     
# 훈련 데이터 70, 테스트 데이터 30으로 나눈다. 4개의 인자값
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.3, random_state = 10)
# 설명: test_size=0.3 으로 했기때문에 훈련과 테스트가 7대 3 비율로 나뉩니다. 
# random_state = 10 은 seed 값 설정 하는 부분입니다. 


print(X_train.shape) 
print(y_train.shape) 

#%%

# 스케일링(z-score 표준화 수행 결과 확인)
for col in range(4):
    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
for col in range(4):
    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')

#%%
# 학습/예측(Training/Pradiction)
from sklearn.neighbors import KNeighborsClassifier

# k-NN 분류기를 생성 # n_neighbors= 가 k 값
classifier = KNeighborsClassifier(n_neighbors=14)

# 분류기 학습
classifier.fit(X_train, y_train) # 훈련 데이터와 훈련 데이터의 라벨로 훈련을 한다. 

# 예측
y_pred= classifier.predict(X_test) # 테스트 데이터를 예측한다. 
print(y_pred)
#%%

from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred, digits=2, output_dict=True)
print(report['macro avg']['precision'])

#%%
# 모델 평가
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    # 이원 교차표

# 민감도, 재현율, F1스코아 
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy) # 0.955555


#%%

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np


acclist = []
err_list = []
fn_list = []


# [14  0  0  0 16  1  0  0 14]
# t1 , t2, t3, t4, t5, t6, t7, t8, t9 
print(metrics.confusion_matrix(y_test, y_pred).ravel())

for i in range(1,30):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    t1 , t2, t3, t4, t5, t6, t7, t8, t9 = metrics.confusion_matrix(y_test, y_pred).ravel()
    fn = t2+t3+t4+t6+t7+t8
    fn_list.append(fn)
    acclist.append(accuracy_score(y_test, y_pred))
    err_list.append(np.mean(y_pred != y_test))

    print(f'k : {i} , acc : {accuracy_score(y_test, y_pred)} , FN : {fn}')

#%%
# col_names=['k','acc','errorr']
 
# s1 = pd.core.series.Series(range(1,30)) 
# s2 = pd.core.series.Series(acclist)
# s3 = pd.core.series.Series(err_list)
df_s = pd.DataFrame(data=dict(k=range(1,30),acc=acclist,err=err_list))
# print(df_s)
print(df_s[df_s['acc']==1])
#%%
acclist = []
err_list = []
f1_list = []

for i in range(1,30):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    report = classification_report(y_test, y_pred, digits=2, output_dict=True)
    f1 = report['macro avg']['f1-score']
    f1_list.append(f1)
    acclist.append(report['macro avg']['precision'])
    err_list.append(np.mean(y_pred != y_test))

    print(f'k : {i} , acc : {accuracy_score(y_test, y_pred)} , F1-score : {f1}')

df_s = pd.DataFrame(data=dict(k=range(1,30),acc=acclist,err=err_list,F1_score=f1_list))

print(df_s[df_s['acc']==1])


plt.figure(figsize=(12,6))
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=1, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)

plt.subplot(131) # 추가로 그래프를 그린다. 
plt.plot(acclist,color='blue', marker='o', markerfacecolor='red')
plt.title('Accuracy', size=15)
plt.xlabel("k value")
plt.ylabel('Accuracy')

plt.subplot(132)
plt.plot(err_list, color='red', marker='o', markerfacecolor='blue')
plt.title('Error', size=15)
plt.xlabel("k value")
plt.ylabel('error')

plt.subplot(133)
plt.plot(fn_list, color='green', marker='o', markerfacecolor='yellow')
plt.title('F1-Score', size=15)
plt.xlabel("k value")
plt.ylabel('fn value')

plt.show()

#%% 문제6.  유방암 데이터의 정확도를 올리기 위해서 정규화를 min / max 정규화로 변경하시오. 

# k = 12  0.97의 k 값 12의 유방암 knn 모델 코드 

# 정규화 ? 1. Min / Max 2. Scale -> N(0,1)
# 보통 Min/Max 가 더 좋은결과가 나오는지 확인해보자. 

# ■ [쉬움주의] 유방암 데이터의 악성종양을 knn 으로 분류하기

import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 
from sklearn import preprocessing # 정규화
from sklearn.model_selection import train_test_split # Train,Test 구분
from sklearn.neighbors import KNeighborsClassifier # Knn 알고리즘

df = pd.read_csv("c:\\data\\wisc_bc_data.csv") 

X = df.iloc[:, 2:].to_numpy() 

y = df['diagnosis'].to_numpy()   

# Min/Max 로 변환
X=preprocessing.MinMaxScaler().fit(X).transform(X) 
# X=preprocessing.StandardScaler().fix(X).transform(X) # N(0,1) 정규
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state = 10)

# k-NN 분류기를 생성
classifier = KNeighborsClassifier(n_neighbors=12)

# 분류기 학습
classifier.fit(X_train, y_train)

# 예측
y_pred= classifier.predict(X_test)
print(y_pred)

# 모델 평가
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    


# 이원 교차표 보는 코드 
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy)
#0.9883040935672515

# Min/Max 정규화시에 0.9883040935672515 로 0.01  퍼 올라간다. FN 5->2 로 감소.



#%% 2장. 나이브 베이즈를 파이썬으로 구현하기 

# R이 좋은 함수와 패키지가 파이썬 보다 더 많다. (역사가 더 깊다.)
# 파이썬으로 머신러닝을 구현하는 경우가 현업에서는 더 많습니다. 
# 앞에서 knn 으로 머신러닝 구현할때 R 과의 차이점은 ? factor 로 변환할 필요가 없었다.

#%% iris 데이터 분류
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import pandas  as pd

# 1. 데이터 준비
col_names = ['sepal-length', 'sepal-width','petal-length', 'petal-width','Class']

# csv 파일에서 DataFrame을 생성
dataset = pd.read_csv('c:\\data\\iris2.csv', encoding='UTF-8', header=None, names=col_names)
#print(dataset)

# DataFrame 확인
print(dataset.shape) # (row개수, column개수)
print(dataset.info()) # 데이터 타입, row 개수, column 개수, 컬럼 데이터 타입
print(dataset.describe()) # 요약 통계 정보

print(dataset.iloc[0:5]) # dataset.head()
print(dataset.iloc[-5:]) # dataset.tail()


# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = dataset.iloc[:,:-1].to_numpy() # DataFrame을 np.ndarray로 변환
#print(X)

# 전체 데이터 세트를 학습 세트(training set)와 검증 세트(test set)로 나눔
# y = 전체 행, 마지막 열 데이터
y = dataset.iloc[:, 4].to_numpy()
#print(y)


# 데이터 분리 
from sklearn.model_selection import train_test_split

# 전체 데이터 세트를 학습 세트(training set)와 검증 세트(test set)로 나눔
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 10)
print(len(X_train), len(X_test))

print(X_train[:3])
print(y_train[:3])


# 3. 거리 계산을 위해서 각 특성들을 스케일링(표준화)
# Z-score 표준화: 평균을 0, 표준편차 1로 변환

from sklearn.preprocessing import StandardScaler

# 3. 거리 계산을 위해서 각 특성들을 스케일링(표준화)
# Z-score 표준화: 평균을 0, 표준편차 1로 변환
scaler = StandardScaler() # Scaler 객체 생성
scaler.fit(X_train) # 스케일링(표준화)를 위한 평균과 표준 편차 계산
X_train = scaler.transform(X_train) # 스케일링(표준화 수행)
X_test = scaler.transform(X_test)

# 스케일링(z-score 표준화 수행 결과 확인)
for col in range(4):
    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
    
for col in range(4):
    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')    

# 4. 학습/예측(Training/Pradiction)
from sklearn.naive_bayes import BernoulliNB # 베르누이 나이브 베이즈 
from sklearn.naive_bayes import GaussianNB # 가우시안 나이브 베이즈
#model = GaussianNB() # Gaussian Naive Bayes 모델 선택 - 연속형 자료

# model = GaussianNB(var_smoothing=1e-09) 
# Gaussian Naive Bayes 모델 선택 - 연속형 자료
# var_smoothing=  laplace 값으로 하이퍼 파라미터다. 
model = GaussianNB() # 하이퍼 파라미터를 주지 않아도 잘된다. 
# model = GaussianNB(var_smoothing=1e-09) 
# model = BernoulliNB()
# model = BernoulliNB(alpha=1e-09)

model.fit( X_train, y_train )

# 예측
y_pred= model.predict(X_test)
print(y_pred)


#5. 모델 평가
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)

# 대각선에 있는 숫자가 정답을 맞춘 것, 그 외가 틀린 것

from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 이원 교차표 보는 코드 
from sklearn import metrics
naive_matrix = metrics.confusion_matrix(y_test,y_pred)
print(naive_matrix)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy)
#%% 문제7. 위의 나이브 베이즈 모델의 성능을 더 올리시오 ~

# BernoulliNB : 0.73333 ---> GaussianNB : ?

model = GaussianNB(var_smoothing=1e-09)

# [[10  0  0]
#  [ 0 13  0]
#  [ 0  0  7]]
# 1.0
#%%
import numpy as np
    
# 6. 모델 개선 - laplace 값을 변화시킬 때, 에러가 줄어드는 지
errors = []
for i in  np.arange(0.0, 1.0, 0.001):
    model = GaussianNB( var_smoothing= i)
    model.fit(X_train, y_train)
    pred_i = model.predict(X_test)
    errors.append(np.mean(pred_i != y_test))
print(errors)

# 여기서 에러가 가장 적은 것을 선택
#%%
import matplotlib.pyplot as plt

plt.plot( np.arange(0.0, 1.0, 0.001), errors, marker='o')
plt.title('Mean error with laplace-Value')
plt.xlabel('laplace')
plt.ylabel('mean error')
plt.show()

#%% 문제 8. 유방암 데이터의 나이브 베이즈 모델을 파이썬으로 생성하고 정확도를 확인하시오 !

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import pandas  as pd
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("C:\\data\\wisc_bc_data.csv") 

print(dataset.columns)
print(dataset.info())
X = dataset.iloc[:,2:].to_numpy() 
print(X)

y = dataset.iloc[:,1 ].to_numpy()
print(y)

#%%
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 10)
print(len(X_train), len(X_test))

print(X_train[:3])
print(y_train[:3])
#%%
scaler = MinMaxScaler()
# scaler = StandardScaler() # Scaler 객체 생성
scaler.fit(X_train) # 스케일링(표준화)를 위한 평균과 표준 편차 계산
X_train = scaler.transform(X_train) # 스케일링(표준화 수행)
X_test = scaler.transform(X_test)

# 스케일링(z-score 표준화 수행 결과 확인)
for col in range(4):
    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
    
for col in range(4):
    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')    
#%%
# 4. 학습/예측(Training/Pradiction)
from sklearn.naive_bayes import BernoulliNB # 베르누이 나이브 베이즈 
from sklearn.naive_bayes import GaussianNB # 가우시안 나이브 베이즈
#model = GaussianNB() # Gaussian Naive Bayes 모델 선택 - 연속형 자료

# model = GaussianNB(var_smoothing=1e-09) 
# Gaussian Naive Bayes 모델 선택 - 연속형 자료
# var_smoothing=  laplace 값으로 하이퍼 파라미터다. 
model = GaussianNB() # 하이퍼 파라미터를 주지 않아도 잘된다. 
# model = GaussianNB(var_smoothing=1e-09) 
# model = BernoulliNB()
# model = BernoulliNB(alpha=1e-09)

model.fit( X_train, y_train )

# 예측
y_pred= model.predict(X_test)
print(y_pred)


#5. 모델 평가
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)

# 대각선에 있는 숫자가 정답을 맞춘 것, 그 외가 틀린 것
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 이원 교차표 보는 코드 
from sklearn import metrics
naive_matrix = metrics.confusion_matrix(y_test,y_pred)
print(naive_matrix)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy)
# 0.947

#%% 문제9. 위의 나이브 베이즈 모델을 생성할때 위에서는 min/max 대신에 scale 함수를
# 적용해서 수행하고 정확도를 확인하시오 

scaler = StandardScaler()

# 0.947 로 동일하다. 

#%% 문제10. wine 데이터를 나이브 베이즈 모델로 분류하시오 ~!

# 데이터 선별: 유방암 데이터, iris 데이터와 같이 종속변수가 분류이면서
#             수치형 데이터인 데이터로 선별을 합니다. 
# 변수가 정규 분포를 가정해서 확률을 구한다.

import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 

df = pd.read_csv("c:\\data\\wine.csv") 

# DataFrame 확인
print(df.shape)
print(df.info()) 
print(df.describe())
print(df)
#%%
# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = df.iloc[:, 1:].to_numpy() 
y = df['Type'].to_numpy()   
#print(y)

print(df.shape)  # (178, 14)
print(len(X))  # 178
print(len(y))  # 178

          #%%             
from sklearn import preprocessing 

# X=preprocessing.StandardScaler().fit(X).transform(X) 
# X=preprocessing.MinMaxScaler().fit(X).transform(X) 
X=X
from sklearn.model_selection import train_test_split 
                                                                
                     
# 훈련 데이터 70, 테스트 데이터 30으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1, random_state = 10)

print(X_train.shape) 
print(y_train.shape) 


# 스케일링(z-score 표준화 수행 결과 확인)
for col in range(4):
    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
for col in range(4):
    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')

#%%

# 학습/예측(Training/Pradiction)
#from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# k-NN 분류기를 생성
#classifier = KNeighborsClassifier(n_neighbors=12)

# 나이브베이즈 분류기를 생성
classifier = GaussianNB( var_smoothing=1e-09 ) # 


# 분류기 학습
classifier.fit(X_train, y_train)

# 예측
y_pred= classifier.predict(X_test)
print(y_pred)

# 작은 이원교차표
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    


# 정밀도 , 재현율, f1 score 확인 
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy)  #  0.888

#%% 문제11. 위의 와인 데이터 분류의 나이브 베이즈 모델의 정확도는 0.88이었습니다.
# 이번에는 knn 으로 해보세요. 

import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 

df = pd.read_csv("c:\\data\\wine.csv") 

# DataFrame 확인
print(df.shape)
print(df.info()) 
print(df.describe())
print(df)
#%%
# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = df.iloc[:, 1:].to_numpy() 
y = df['Type'].to_numpy()   
#print(y)

print(df.shape)  # (178, 14)
print(len(X))  # 178
print(len(y))  # 178

          #%%             
from sklearn import preprocessing 

# X=preprocessing.StandardScaler().fit(X).transform(X) 
X=preprocessing.MinMaxScaler().fit(X).transform(X) 
# X=X
from sklearn.model_selection import train_test_split 
                                                                
                     
# 훈련 데이터 70, 테스트 데이터 30으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1, random_state = 10)

print(X_train.shape) 
print(y_train.shape) 


# 스케일링(z-score 표준화 수행 결과 확인)
for col in range(4):
    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
for col in range(4):
    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')

#%%

import numpy as np
# k-NN 분류기를 생성
#classifier = KNeighborsClassifier(n_neighbors=12)

from sklearn.neighbors import KNeighborsClassifier

acclist = []
err_list = []
f1_list = []

for i in range(1,30):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    report = classification_report(y_test, y_pred, digits=2, output_dict=True)
    f1 = report['macro avg']['f1-score']
    f1_list.append(f1)
    acclist.append(report['macro avg']['precision'])
    err_list.append(np.mean(y_pred != y_test))

    print(f'k : {i} , acc : {accuracy_score(y_test, y_pred)} , F1-score : {f1}')

df_s = pd.DataFrame(data=dict(k=range(1,30),acc=acclist,err=err_list,F1_score=f1_list))
print(df_s)
# print(df_s[df_s['acc']>=0.9])
#%%
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=1, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)

plt.subplot(131) # 추가로 그래프를 그린다. 
plt.plot(acclist,color='blue', marker='o', markerfacecolor='red')
plt.title('Accuracy', size=15)
plt.xlabel("k value")
plt.ylabel('Accuracy')

plt.subplot(132)
plt.plot(err_list, color='red', marker='o', markerfacecolor='blue')
plt.title('Error', size=15)
plt.xlabel("k value")
plt.ylabel('error')

plt.subplot(133)
plt.plot(f1_list, color='green', marker='o', markerfacecolor='yellow')
plt.title('F1-Score', size=15)
plt.xlabel("k value")
plt.ylabel('fn value')

plt.show()


#%%
# k-NN 분류기를 생성 # n_neighbors= 가 k 
classifier = KNeighborsClassifier(n_neighbors=3)

# 분류기 학습
classifier.fit(X_train, y_train)

# 예측
y_pred= classifier.predict(X_test)
print(y_pred)

# 작은 이원교차표
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    


# 정밀도 , 재현율, f1 score 확인 
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy)  #  0.888


#%% 파이썬 나이브 베이즈 사이킷런 함수 3가지

1. BernoulliNB : 이산형 데이터를 분류할 때 적합
2. GaussianNB : 연속형 데이터를 분류할 때 적합
3. MultinomialNB : 
    
#%% 독버섯 데이터를 나이브 베이즈 모델로 분류하기 
import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 

#1.파이썬에서:
# 더미 변수 -1개
df = pd.read_csv('c:\\data\\mushrooms.csv')
df = pd.get_dummies(df, drop_first=True)
X = df.iloc[:, 1:].to_numpy() 
y = df.iloc[:,0].to_numpy()  
print(df)
#%% 전부 더미 변수화
df = pd.read_csv('c:\\data\\mushrooms.csv')
df = pd.get_dummies(df)
X = df.iloc[:, 2:].to_numpy() 
y = df.iloc[:,1].to_numpy()  
print(df)

#%%


print(df.shape)  
print(len(X))  
print(len(y))  

print(df.shape)
print(df.info()) 
print(df.describe())
print(df)

X = df.iloc[:, 1:].to_numpy() 
y = df.iloc[:,0].to_numpy()   
#print(y)
print(df.shape)  # (8124, 23)
print(len(X))  # 8124
print(len(y))  # 8124

#%%
                       
from sklearn import preprocessing 

# X=preprocessing.StandardScaler().fit(X).transform(X) 
#X=preprocessing.MinMaxScaler().fit(X).transform(X) 

from sklearn.model_selection import train_test_split 
                                                                
                     
# 훈련 데이터 70, 테스트 데이터 30으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state = 10)

print(X_train.shape) 
print(y_train.shape) 

#%%
# # 스케일링(z-score 표준화 수행 결과 확인)
# for col in range(4):
#     print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
# for col in range(4):
#     print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')


#%%
# 학습/예측(Training/Pradiction)
#from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

# k-NN 분류기를 생성
#classifier = KNeighborsClassifier(n_neighbors=12)

# 나이브베이즈 분류기를 생성
# classifier = GaussianNB() # 
# classifier = MultinomialNB(alpha=0.000001)
classifier = MultinomialNB()

# 분류기 학습
classifier.fit(X_train, y_train)

# 예측
y_pred= classifier.predict(X_test)
print(y_pred)

# 작은 이원교차표
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    


# 정밀도 , 재현율, f1 score 확인 
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

# 정확도 확인하는 코드 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred)
print(accuracy)  #  0.941








#%%문제??. ongoing 하는 타이타닉 모델을 나이브베이즈 모델을 파이썬으로 구현해서 도전하시오.

from sklearn import metrics
import numpy as np

# 1단계 csv ---> 데이터 프레임으로 변환

import pandas as pd
import seaborn as sns

df = pd.read_csv("c:\\data\\kaggledata\\titanic\\train_titanic.csv")

# 컬럼이 모두다 출력될 수 있도록 출력할 열의 개수 한도를 늘리기
pd.set_option('display.max_columns',15)
#%%
# 2단계 결측치 확인하고 제거하거나 치환한다.
# 2.1 타이타닉 데이터 프레임의 자료형을 확인한다.

mask4 = (df.Age<10) | (df.Sex=='female') 
df['child_women']=mask4.astype(int)

print ( df.columns)


# 2.2 결측치(NaN) 을 확인한다.
# 2.3 deck 컬럼과 embark_town 컬럼을 삭제한다.
# 설명 : deck 결측치가 많아서 컬럼을 삭제해야함.
# embark 와 embark_town 이 같은 데이터여서 embark 컬럼을 삭제해야함

rdf = df.drop(['PassengerId','Cabin','Name','Ticket'], axis =1)
print(rdf)

# 2.4 age(나이) 열에 나이가 없는 모든행을 삭제한다.
# 데이터가 한개라도 없으면 drop 해라 (how = 'any')
# 모든 데이터가 없으면 drop 해라 (how = 'all')

print(rdf.shape)

# 나이의 결측치를 최빈값으로 치환한다. 
most_freq = rdf['Age'].value_counts(dropna=True).idxmax()  
rdf['Age'].fillna(most_freq, inplace=True)
print(rdf.shape)

# 2.5 embark 열의 NaN 값을 승선도시중 가장 많이 출현한 값으로 치환하기
most_freq = rdf['Embarked'].value_counts().idxmax()
rdf['Embarked'].fillna(most_freq, inplace = True)
print(rdf)

# 3단계 범주형 데이터를 숫자형으로 변환하기
# 3.1 feature selection (분석에 필요한 속성을 선택)
ndf = rdf[['Survived','Pclass','Sex','Age','SibSp','Parch','Embarked','child_women']]
ndf.head()

# 선택된 컬럼중 2개(sex, embarked) 가 범주형이다.
#3.2 범주형 데이터를 숫자로 변환하기(원핫 인코딩)

gender = pd.get_dummies(ndf['Sex'])
ndf = pd.concat([ndf,gender], axis= 1)
onehot_embarked = pd.get_dummies(ndf['Embarked'])
ndf = pd.concat([ndf,onehot_embarked],axis=1)
ndf.drop(['Sex','Embarked'], axis=1, inplace = True)

# 4단계 정규화
# 4.1 독립변수와 종속변수(라벨) 을 지정한다.
# survived  pclass   age  sibsp  parch  female  male  C  Q  S
#   라벨                       데이터
# 종속변수                     독립변수

print(ndf.columns)
x = ndf[ ['Pclass', 'Age' ,'SibSp', 'Parch' ,'female' ,'male', 'C' ,'Q' ,'S',
          'child_women'] ]

y = ndf['Survived'] # 종속변수
print(x)

# 4.2 독립변수들을 정규화 한다.
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(x).transform(x)

# 테스트 데이터도 훈련 데이터와 같이 데이터를 구성한다. 

# 훈련 데이터 처럼 테스트 데이터도 파생변수를 추가한다. 
x_ktest = pd.read_csv("d:\\data\\test.csv")
mask4 = (x_ktest.Age<10) | (x_ktest.Sex=='female') 
x_ktest['child_women']=mask4.astype(int)
print ( x_ktest.columns)

# 2.2 결측치(NaN) 을 확인한다.

# 2.3 deck 컬럼과 embark_town 컬럼을 삭제한다.
# 설명 : deck 결측치가 많아서 컬럼을 삭제해야함.
#  embark 와 embark_town 이 같은 데이터여서 embark 컬럼을 삭제해야함

rdf_x_ktest = x_ktest.drop(['PassengerId','Cabin','Name','Ticket'], axis =1)
print(rdf_x_ktest)

# 나이의 결측치를 최빈값으로 치환한다. 
most_freq = rdf_x_ktest['Age'].value_counts(dropna=True).idxmax()  
rdf_x_ktest['Age'].fillna(most_freq, inplace=True)
print(rdf_x_ktest.shape)

# embark 열의 NaN 값을 승선도시중 가장 많이 출현한 값으로 치환하기
most_freq = rdf_x_ktest['Embarked'].value_counts().idxmax()
rdf_x_ktest['Embarked'].fillna(most_freq, inplace = True)
print(rdf_x_ktest)

# 3단계 범주형 데이터를 숫자형으로 변환하기
# 3.1 feature selection (분석에 필요한 속성을 선택)
#ndf = rdf[['Survived','Pclass','Sex','Age','Sibsp','Parch','Embarked','child_women']]

ndf_x_ktest = rdf_x_ktest

# 선택된 컬럼중 2개(sex, embarked) 가 범주형이다.
#3.2 범주형 데이터를 숫자로 변환하기(원핫 인코딩)
gender = pd.get_dummies(ndf_x_ktest['Sex'])
ndf_x_ktest = pd.concat([ndf_x_ktest,gender], axis= 1)
onehot_embarked = pd.get_dummies(ndf_x_ktest['Embarked'])
ndf_x_ktest = pd.concat([ndf_x_ktest,onehot_embarked],axis=1)
ndf_x_ktest.drop(['Sex','Embarked'], axis=1, inplace = True)

# 4단계 정규화
# 4.1 독립변수와 종속변수(라벨) 을 지정한다.
# survived  pclass   age  sibsp  parch  female  male  C  Q  S
#   라벨                       데이터
# 종속변수                     독립변수
print(ndf_x_ktest.columns)

x = ndf_x_ktest[ ['Pclass', 'Age' ,'SibSp', 'Parch' ,'female' ,'male', 'C' ,'Q' ,'S',
                       'child_women'] ]

#y = ndf_x_ktest['Survived'] # 종속변수

# 4.2 독립변수들을 정규화 한다.
from sklearn import preprocessing
X_test = preprocessing.StandardScaler().fit(x).transform(x)
print(len(X))

from sklearn.naive_bayes import BernoulliNB
model = BernoulliNB( alpha = 0.4 )
model.fit( X, y )
y_hat = model.predict( X_test )
print( y_hat)

# 케글에 올리기 위한 포멧으로 데이터를 구성한다. 

for  i, a  in  enumerate(y_hat):
    print (i+892,',',a)








