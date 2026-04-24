0
from sklearn.datasets import load_iris
import pandas as pds
import numpy as npy
import matplotlib.pyplot as plot0411
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
iris = load_iris()
x = pds.DataFrame(iris['data'], columns=iris['feature_names'])
y = pds.DataFrame(iris['target'], columns=['target'])
iris0411 = pds.concat([x,y], axis=1) # 利用concat橫向合併(axis=1直行)
print(iris0411.head())

1
print("此鳶尾花資料集的數量:", iris0411.shape)
print("鳶尾花資料集col名稱，各別是:", iris0411.keys())
print("鳶尾花資料集之第一個的資料內容:", iris0411.iloc[0,:])
print("鳶尾花資料集之第一個真實值:",iris0411['target'][0])

2
flower_markers = ('^', 'o', 'x')
marker_colors = ('purple', 'green', 'cyan')
y = iris0411['target'].values
for i in (npy.unique(y)):  #enumerate將可編列的數據編成序列
    p = iris0411[y == i]
    plot0411.scatter(x=p['sepal length (cm)'],  y=p['petal length (cm)'], c=marker_colors[i], marker=flower_markers[i],  label=i) #scatter散布圖
plot0411.xlabel('sepal length (cm)') #xlabel名稱(萼片)
plot0411.ylabel('petal length (cm)') #ylabel名稱(花瓣)
plot0411.legend(loc='lower right') #標示名稱置放位置右下角
plot0411.show()

3
iris0411_1 = iris0411[['sepal length (cm)','petal length (cm)','target']]
iris0411_1 = iris0411[iris0411['target'].isin([1,2])]  #在範圍1-2中的資料取出就好，0的不要,類別1,類別2只取個50筆資料    
print(iris0411_1['target'].value_counts())

4
x_train, x_test, y_train, y_test = train_test_split(iris0411_1[['sepal length (cm)','petal length (cm)']], iris0411_1[['target']], test_size=0.1, random_state=22)#test_size是測試值,而random_state=42是原本的初始正確率
standard_scaler = StandardScaler() #標準化資料
x_train_std = standard_scaler.fit_transform(x_train)
x_test_std = standard_scaler.fit_transform(x_test)
print("鳶尾花訓練資料之訓練集維度大小:   ", x_train_std.shape)
print("鳶尾花測試資料之測試集維度大小:   ", x_test_std.shape)

5
model0411 = LogisticRegression()
model0411.fit(x_train_std, y_train['target'])
print ('係數_Coefficients: ', model0411.coef_)
print ('截距_Intercept: ',model0411.intercept_)

6
print(model0411.predict(x_test_std))
print(y_test['target'].values)
print(model0411.predict_proba(x_test_std))

7
confusion_matrix_show = confusion_matrix(y_test['target'],model0411.predict(x_test_std))
print(confusion_matrix_show)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test['target'], model0411.predict(x_test_std))
print("正確率 (Accuracy):", accuracy)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test['target'], model0411.predict(x_test_std))
print("正確率 (Accuracy):", accuracy)