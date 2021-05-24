### 파이썬 읽고 쓰기 문법


# 1.  파이썬에서 아래와 같이 seaborn 에 내장되어 있는 타이타닉 데이터를 내려받습니다. 


import  seaborn  as sns
import pandas as pd

tat = sns.load_dataset('titanic')

print(tat)

tat2 = pd.DataFrame(tat)

tat2.to_csv('c:\\data\\tatanic.csv', sep=',',  na_rep='NaN')   # missing data representation (결측값 표기)


#%% sklean 에서 boston 데이터 불러오기


from sklearn.datasets import load_boston #scikit-learn의 datasets에서 sample data import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


boston = load_boston() # boston dataset load
# print(boston.keys()) # 각 key 확인
# print(boston.DESCR) # boston datasets description
# print(boston)
# print(boston.data)
# print(boston.feature_names)
# print(boston)
# 데이터 프레임으로 변환
df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
df['price'] = boston.target
# print(df)
df.to_csv('c:\\data\\boston.csv',sep=',', na_rep='NaN')





