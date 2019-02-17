from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

# Importing dataset
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

#1: Naive Bayes
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))

#2: Linear SVM
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)
y_pred = clf.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))

#3: RBG SVM
clf = svm.SVC(gamma= 'auto', kernel='rbf', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)
y_pred = clf.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))