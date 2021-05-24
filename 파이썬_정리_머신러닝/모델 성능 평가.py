### 모델 성능 평가 




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
#%%
errors = []
for i in range(1, 31):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    errors.append(np.mean(pred_i != y_test))
print(errors)


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

