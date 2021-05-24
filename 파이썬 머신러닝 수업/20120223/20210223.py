### Knn & naivebayes

# R 과 파이썬의 차이점 ?
# 1. stringAsFactors = True 를 안쓰고 그냥 로드
# 2. 명목형 데이터를 dummy 변수화 해야함


#%%

df = pd.get_dummies(df, drop_first=True) # 더미 변수 생성
# 옵션 : drop_first=True 를 사용하게 되면 생성된 더미 변수 중에서 하나의 컬럼(첫번째)를 삭제합니다. 

#%%

#■ 3장 의사결정 트리 

# 의사결정트리 --> 랜덤 포레스트 (앙상블 + 의사결정트리 )
# 


import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 

df = pd.read_csv('c:\\data\\mushrooms.csv')

df = pd.get_dummies(df, drop_first=True)
#print(df.shape)  # (8124, 23)
print(df)
print(df.shape) # (8124, 119)

# get_dummies 함수를 이용해서 값의 종류에 따라 
# 전부 0 아니면 1로 변환함 
#%%
# DataFrame 확인
print(df.shape)  # (8124, 23)
print(df.info())  # 전부 object (문자)형으로 되어있음
print(df.describe())

# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = df.iloc[:,2:].to_numpy() 
y = df.iloc[:,1].to_numpy()   
print(X)
print(y)

print(df.shape)  # (8124, 119)
print(len(X))  # 8124
print(len(y))  # 8124


from sklearn.model_selection import train_test_split 
                                                                                     
# 훈련 데이터 75, 테스트 데이터 25으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state = 10)

print(X_train.shape)   # (6093, 22)
print(y_train.shape)   # (6093,)



# 스케일링(z-score 표준화 수행 결과 확인)
#for col in range(4):
#    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
#for col in range(4):
#    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')


# 학습/예측(Training/Pradiction)

# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기
from sklearn import tree


#  의사결정트리 분류기를 생성 (criterion='entropy' 적용)
classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)


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
print(accuracy)  #  1.0   Decision tree 
                 #  0.9497   MultinomialNB
                 #  0.9615   GaussianNB
                 #  0.9350   BernoulliNB

 

문제.  iris 데이터를 의사결정트리로 분류하시오 ! (중요한 컬럼 확인 - 정보획득량이 제일 높은것 확인)

import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 

col_names = ['sepal-length', 'sepal-width','petal-length', 'petal-width','Class']

df =  pd.read_csv('d:\\data\\iris2.csv', encoding='UTF-8', header=None, names=col_names)

print(df.shape)  # (149, 5)
#print(df)

# DataFrame 확인
print(df.info())  # 전부 object (문자)형으로 되어있음
print(df.describe())
print(df)

# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = df.iloc[:,:-1].to_numpy() 
y = df.iloc[:,-1].to_numpy()   

print(len(X))  # 149
print(len(y))  # 149

from sklearn import preprocessing 

#X=preprocessing.StandardScaler().fit(X).transform(X)  
X=preprocessing.MinMaxScaler().fit(X).transform(X) 
#print(X)

from sklearn.model_selection import train_test_split 
                                                                                     
# 훈련 데이터 75, 테스트 데이터 25으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state = 10)

print(X_train.shape)   # (111, 4)
print(y_train.shape)   # (111,)


# 학습/예측(Training/Pradiction)
# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기
from sklearn import tree

#  의사결정트리 분류기를 생성 (criterion='entropy' 적용)
classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
#classifier = tree.DecisionTreeClassifier(criterion='gini', max_depth=3)
# 메뉴얼 : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

# 분류기 학습
classifier.fit(X_train, y_train)

# 특성 중요도
print(df.columns.values)
print("특성 중요도 : \n{}".format(classifier.feature_importances_))

import matplotlib.pyplot as plt
import numpy as np


def plot_feature_importances_cancer(model):
    n_features = df.shape[1]
    plt.barh(range(n_features-1),model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df.columns.values)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1,n_features)

plot_feature_importances_cancer(classifier)
plt.show()

#%%


y_pred= classifier.predict(X_test)

# 작은 이원교차표
from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    

# 정밀도 , 재현율, f1 score 확인 
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
#print(report)

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

dot_data = export_graphviz(classifier, out_file=None,
                           feature_names=df.columns.values[0:4],
                           class_names=classifier.classes_,
                           filled=True, rounded=True,
                           special_characters=True)

 
# 그래프 그리기

dot_data
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


# 그래프 해석
#첫번째 줄 : 분류 기준
#entropy : 엔트로피값
#sample : 분류한 데이터 개수
#value : 클래스별 데이터 개수
#class : 예측한 답
# 문제14.
# 문제15
#%%
#문제16 화장품 데이터 (skin.csv) 를 이용해서 의사결정 트리 모델을 생성하시오 !



# 의사결정트리 --> 랜덤 포레스트 (앙상블 + 의사결정트리 )
# 


import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 

df = pd.read_csv('c:\\data\\skin.csv')

df = pd.get_dummies(df, drop_first=True)
#print(df.shape)  # (8124, 23)
print(df)
print(df.shape) # (8124, 119)

# get_dummies 함수를 이용해서 값의 종류에 따라 
# 전부 0 아니면 1로 변환함 
#%%
# DataFrame 확인
print(df.shape)  # (8124, 23)
print(df.info())  # 전부 object (문자)형으로 되어있음
print(df.describe())

# X = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
X = df.iloc[:,:-1].to_numpy() 
y = df.iloc[:,-1].to_numpy()   
print(X)
print(y)

print(df.shape)  # (8124, 119)
print(len(X))  # 8124
print(len(y))  # 8124


from sklearn.model_selection import train_test_split 
                                                                                     
# 훈련 데이터 75, 테스트 데이터 25으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state = 10)

print(X_train.shape)   # (6093, 22)
print(y_train.shape)   # (6093,)



# 스케일링(z-score 표준화 수행 결과 확인)
#for col in range(4):
#    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')
    
#for col in range(4):
#    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')


# 학습/예측(Training/Pradiction)

# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기
from sklearn import tree


#  의사결정트리 분류기를 생성 (criterion='entropy' 적용)
classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)


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
print(accuracy)  #  1.0   Decision tree 
                 #  0.9497   MultinomialNB
                 #  0.9615   GaussianNB
                 #  0.9350   BernoulliNB

 

# 문제.  iris 데이터를 의사결정트리로 분류하시오 ! (중요한 컬럼 확인 - 정보획득량이 제일 높은것 확인)
#%%
import pandas as pd  # 데이터 전처리를 위해서 
import seaborn as sns # 시각화를 위해서 

# col_names = ['sepal-length', 'sepal-width','petal-length', 'petal-width','Class']

df =  pd.read_csv('c:\\data\\skin.csv', encoding='UTF-8')
df = df.iloc[:,1:]
df = pd.get_dummies(df, drop_first=True)
print(df.shape)  # (149, 5)
#print(df)

# DataFrame 확인
# print(df.info()) 
print(df.describe())
# print(df)
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
classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=6)
#classifier = tree.DecisionTreeClassifier(criterion='gini', max_depth=3)
# 메뉴얼 : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

# 분류기 학습
classifier.fit(X_train, y_train)

# 특성 중요도
print(df.columns.values)
print("특성 중요도 : \n{}".format(classifier.feature_importances_))
#%%
import matplotlib.pyplot as plt
import numpy as np


def plot_feature_importances_cancer(model):
    n_features = df.shape[1]-1
    plt.barh(range(n_features),model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df.columns.values[0:5])
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
#print(report)

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
dot_data = export_graphviz(classifier,
                           feature_names=df.columns.values[0:5],
                           class_names=['no','yes'],
                           filled=True, rounded=True,
                           special_characters=True)

 
# 그래프 그리기

# dot_data
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_svg('c:\\data\\skin.svg')
# print(graph)
# (Image(graph.create_png()))

#%%
carirovg.svg2png(url=('c:\\data\\skin.svg'), write_to('c:\\data\\skin.png'), dpi = 100)
#%%
import cairosvg

def svg2svg(bytestring=None, *, file_obj=None, url=None, dpi=96,
            parent_width=None, parent_height=None, scale=1, unsafe=False,
            background_color=None, negate_colors=False, invert_images=False,
            write_to=None, output_width=None, output_height=None):
    return surface.SVGSurface.convert(
        bytestring=bytestring, file_obj=file_obj, url=url, dpi=dpi,
        parent_width=parent_width, parent_height=parent_height, scale=scale,
        background_color=background_color,
        negate_colors=negate_colors, invert_images=invert_images,
        unsafe=unsafe, write_to=write_to, output_width=output_width,
        output_height=output_height)

#cairosvg.svg2png(#url="/path/to/input.svg", write_to="/tmp/output.png")
import matplotlib.pyplot as plt
import cairosvg
import numpy as np 

w = 2048
a = np.random.normal(0, 1, w**2).reshape(w, w)
plt.imshow(a, cmap=plt.cm.Reds, alpha=0.8)
#plt.axis('off')
plt.xticks([])
plt.yticks([])
plt.savefig("../../assets/images/markdown_img/180629_1521_simple_svg.svg")
plt.show()

### 이미 svg 파일이 있다면, 아래코드만 사용하면 됩니다. 
cairosvg.svg2png(url="../../assets/images/markdown_img/180629_1521_simple_svg.svg", 
                 write_to="../../assets/images/markdown_img/180629_1521_simple_png.png", 
                 dpi = 100
                )