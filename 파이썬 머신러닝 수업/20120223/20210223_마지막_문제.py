
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

weight=[ 72, 72, 70, 43, 48, 54, 51, 52, 73, 45, 60, 62, 64, 47, 51, 74, 88,64, 56, 56  ]
tall = [ 176, 172, 182, 160, 163, 165, 168, 163, 182, 148, 170, 166, 172, 169, 163, 170, 182, 174, 164, 160 ] 

dict_data = { 'weight' : [ 72, 72, 70, 43, 48, 54, 51, 52, 73, 45, 60, 62, 64, 47, 51, 74, 88, 64, 56, 56  ],
                  'tall' : [ 176, 172, 182, 160, 163, 165, 168, 163, 182, 148, 170, 166, 172, 169, 163, 170, 182, 174, 164, 160 ]   }

df = pd.DataFrame(dict_data)
print (df)

print(df.info())

df.plot(kind='scatter', x = 'weight', y = 'tall', c = 'coral', s = 10, figsize=(10,5))
plt.show()
plt.close()

# seaborn으로 산점도 그리기
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
sns.regplot(x='weight', y='tall', data=df, ax=ax1) # 회귀선 표시
sns.regplot(x='weight', y='tall', data=df, ax=ax2, fit_reg=False) #회귀선 미표시
plt.show()
plt.close()

# seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x='weight', y='tall', data=df) # 회귀선 없음
sns.jointplot(x='weight', y='tall', kind='reg', data=df) # 회귀선 표시
plt.show()
plt.close()

X=df[['weight']]
y=df['tall']

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X, y)

y_pred = lr.predict(X)
r_square = lr.score(X, y)
print(r_square)

# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교
y_hat = lr.predict(X)
plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y, hist=False, label="y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
plt.legend()
plt.show()
plt.close()