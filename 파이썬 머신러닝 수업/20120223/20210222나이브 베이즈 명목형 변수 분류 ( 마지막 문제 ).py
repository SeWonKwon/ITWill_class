### 나이브 베이즈 명목형 변수 분류 ( 마지막 문제 )

import sys
import numpy as np
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)
pd.set_option('display.max_columns', 500)


df = pd.read_csv('c:\\data\\mushrooms.csv')

# 명목형 갯수 -1 개의 갯수로 더미 변수를 만들어야 정확도가 더 올라갑니다. 
df = pd.get_dummies(df, drop_first=True) # 더미 변수 생성

X = df.iloc[:,2:].to_numpy() 
y = df.iloc[:,0].to_numpy()  

from sklearn.model_selection import train_test_split                                                                                 
# 훈련 데이터 75, 테스트 데이터 25으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state = 10)

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
import numpy as np
from sklearn.metrics import classification_report

r= np.arange(0.0001, 0.0011 , 0.0001)
acclist = []
err_list = []
f1_list = []
for i in r:
    nb = MultinomialNB(alpha=i)
    # nb = BernoulliNB(alpha=i)
    # nb = GaussianNB(var_smoothing=i)
    nb.fit(X_train, y_train)
    y_pred = nb.predict(X_test)
    
    report = classification_report(y_test, y_pred, digits=2, output_dict=True)
    f1 = report['macro avg']['f1-score']
    f1_list.append(f1)
    acclist.append(report['accuracy'])
    err_list.append(np.mean(y_pred != y_test))
print(nb)
df_s = pd.DataFrame(data=dict(laplace=r, acc=acclist, err=err_list, F1_score=f1_list))

target = 0.99
df_s2 = (df_s[df_s['acc']>target])
print(df_s2)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=1, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)

plt.subplot(131) # 추가로 그래프를 그린다. 
plt.plot(r, acclist,color='blue', marker='o', markerfacecolor='red')
plt.title('Accuracy', size=15)
plt.xlabel("laplace")
plt.ylabel('Accuracy')

plt.subplot(132)
plt.plot(r, err_list, color='red', marker='o', markerfacecolor='blue')
plt.title('Error', size=15)
plt.xlabel("laplace")
plt.ylabel('error')

plt.subplot(133)
plt.plot(r, f1_list, color='green', marker='o', markerfacecolor='yellow')
plt.title('F1-Score', size=15)
plt.xlabel("laplace")
plt.ylabel('F1 Score')

plt.show()
# 결론:  더미 변수 갯수를 항목 갯수-1개로 조정하고, MultinomialNB 를 이용한  laplace 가 아래와 같을때 
#   laplace       acc       err  F1_score
#   0.0001  1.000000  0.000000  1.000000
#   0.0002  0.999508  0.000492  0.999506













# 결론:  더미 변수 갯수를 항목 갯수-1개로 조정하고, MultinomialNB 를 이용한  laplace 가 아래와 같을때 