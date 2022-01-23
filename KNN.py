import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

dataset = load_iris()
X_train, X_test, y_train , y_test = train_test_split(dataset["data"],dataset["target"],random_state=0)

kn=KNeighborsClassifier(n_neighbors=5)
kn.fit(X_train, y_train)

prediction = kn.predict(X_test)
confusion_matrix(y_test,prediction)
