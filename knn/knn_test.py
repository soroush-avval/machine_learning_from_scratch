import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

iris = datasets.load_iris()
X, y = iris.data, iris.target

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

print("corresponding shapes of data and targets are;\ndata: {},\ntarget: {}\nsplit is done with 0.2 ratio resulting in {} for train and {} for test".format(X.shape, y.shape, int(X.shape[0]*0.8), int(X.shape[0]*0.2)))

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolors='k', s=20)
plt.show()

from knn import KNN

clf = KNN(k=5)
clf.fit(x_train, y_train)
predictions = clf.predict(x_test)

acc = np.sum(predictions==y_test) / len(y_test)
print(acc)