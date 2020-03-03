import pandas as pd
import seaborn as sns
import numpy as np


import matplotlib.pyplot as plt

iris = pd.read_csv('Iris_kaggle.csv')

irisf=pd.DataFrame(iris)

data=pd.DataFrame(iris,columns=iris.columns)

print(data.head())

print(data[data.species=='Iris-versicolor'])
print(len(data[data.species=='Iris-versicolor']))






print("MOshir Rahman Rimu")
print(iris.shape)

print(iris.columns)
iris.head()

iris["species"].value_counts()

iris.plot(kind = 'scatter' , x='sepal_length' , y = 'sepal_width');

sns.set_style("whitegrid");

sns.FacetGrid(iris, hue="species", size=4).map(plt.scatter, "sepal_length", "sepal_width").add_legend();
plt.show();




sns.pairplot(iris , hue="species", palette = 'Dark2')
sns.pairplot(iris ,kind="reg", hue="species", diag_kind = 'kde')


from sklearn.model_selection import train_test_split

x = iris.drop('species', axis=1)
y = iris['species']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)




from sklearn.svm import SVC

svc_model = SVC()

svc_model.fit(x_train,y_train)

print(SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=3, gamma='auto_deprecated', kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False))   

predictions = svc_model.predict(x_test)



from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))



training_acc = svc_model.score(x_train,y_train)
validation_acc = svc_model.score(x_test,y_test)


print("training accuracy: %2f"%training_acc)
print("test accuracy: %2f"%validation_acc)

y_pred = svc_model.predict(x_test)

print(y_test)
print(y_pred)
