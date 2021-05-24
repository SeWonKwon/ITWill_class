### 문제17. R을 활용하는 머신러닝에서 사용했던 독일 은행 데이터의 채무 불이행자를 예측 하고 의사결정트리 나무를 시각화 하시오 ! 

import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 
import numpy as np
# np.set_printoptions(threshold=sys.maxsize)
pd.set_option('display.max_columns', 500)
# col_names = ['sepal-length', 'sepal-width','petal-length', 'petal-width','Class']

df =  pd.read_csv('c:\\data\\credit.csv', encoding='UTF-8')
# DataFrame 확인
print(df.info()) 
# print(df.describe())
# print(df)
print(df.head())
# print(df.columns.values)
#%%
# 'checking_balance' : 더미
# 'months_loan_duration' 인트
# 'credit_history' 'purpose' 더미
# 'amount' 인트
# 'savings_balance' 더미 
# 'employment_duration' 더미
# 'percent_of_income' 인트
# 'years_at_residence' 인트 
# 'age' 
# 'other_credit' 
# 'housing'
# 'existing_loans_count'
# 'job'
# 'dependents' 
# 'phone' 
# 'default'

 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   checking_balance      1000 non-null   object
 1   months_loan_duration  1000 non-null   int64 
 2   credit_history        1000 non-null   object
 3   purpose               1000 non-null   object
 4   amount                1000 non-null   int64 
 5   savings_balance       1000 non-null   object
 6   employment_duration   1000 non-null   object
 7   percent_of_income     1000 non-null   int64 
 8   years_at_residence    1000 non-null   int64 
 9   age                   1000 non-null   int64 
 10  other_credit          1000 non-null   object
 11  housing               1000 non-null   object
 12  existing_loans_count  1000 non-null   int64 
 13  job                   1000 non-null   object
 14  dependents            1000 non-null   int64 
 15  phone                 1000 non-null   object
 16  default               1000 non-null   object
#%%
# df = df.iloc[:,1:]
df = pd.get_dummies(df, drop_first=True)
print(df.shape)  # (149, 5)
#print(df)

# DataFrame 확인
# print(df.info()) 
print(df.describe())
# print(df)
print(df.head())
#%%
X = df.iloc[:,:-1].to_numpy() 
y = df.iloc[:,-1].to_numpy()   
#%%
print(len(X))  # 149
print(len(y))  # 149



from sklearn.model_selection import train_test_split 
                                                                                     
# 훈련 데이터 75, 테스트 데이터 25으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state = 10)

print(X_train.shape)   # (111, 4)
print(y_train.shape)   # (111,)


# 학습/예측(Training/Pradiction)
# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기
from sklearn import tree

#  의사결정트리 분류기를 생성 (criterion='entropy' 적용)
classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)
#classifier = tree.DecisionTreeClassifier(criterion='gini', max_depth=3)
# 메뉴얼 : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

# 분류기 학습
classifier.fit(X_train, y_train)

# 특성 중요도
print(df.columns.values)
print("특성 중요도 : \n{}".format(classifier.feature_importances_))

#%%


# 문제18.  위의 의사결정트리의 모델을 의사결정트리 + 앙상블 기법을 적용한
#            랜덤포레스트로 구현하시오 !

from sklearn import tree
from  sklearn.ensemble   import  RandomForestClassifier 

#  의사결정트리 분류기를 생성 (criterion='entropy' 적용)
#classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
#classifier = tree.DecisionTreeClassifier(criterion='gini', max_depth=3)
# 메뉴얼 : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

classifier = RandomForestClassifier( n_estimators=10000, criterion='entropy',
                                            oob_score=True,
                                            random_state= 10, verbose=1 )  

classifier.fit( X_train, y_train )

print ( classifier.oob_score_)
#%%
import matplotlib.pyplot as plt
import numpy as np


def plot_feature_importances_cancer(model):
    n_features = df.shape[1]-1
    plt.barh(range(n_features),model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df.columns.values[0:-1],rotation='15')
    
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1,n_features)

plot_feature_importances_cancer(classifier)
plt.show()
#%%
print(df.columns.values)
# print(.feature_importances_)
#%%

y_pred= classifier.predict(X_test)

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
print( accuracy) 

import pydotplus
from sklearn.tree import export_graphviz
from IPython.core.display import Image
import matplotlib.pyplot as plt

# 그래프 설정

# out_file=None : 결과를 파일로 저장하지 않겠다.
# filled=True : 상자 채우기
# rounded=True : 상자모서리 둥그렇게 만들기
# special_characters=True : 상자안에 내용 넣기
#%%
print(classifier.classes_)
#%%
# dot_data = export_graphviz(classifier,
#                            feature_names=df.columns.values[0:-1],
#                            class_names=['no','yes'],
#                            filled=True, rounded=True,
#                            special_characters=True)
dot_data = export_graphviz(classifier,
                           feature_names=df.columns.values[0:-1],
                           class_names=['no','yes'],
                           filled=True, rounded=True)
# dot_data
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_svg('c:\\data\\credit.svg')
# print(graph)
# (Image(graph.create_png()))
