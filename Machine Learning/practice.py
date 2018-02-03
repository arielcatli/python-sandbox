# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:05:31 2017

@author: Ariel Domingo Catli
"""
from sklearn import svm
from sklearn.datasets import load_digits
import cv2

digits = load_digits()

X = digits.data
Y = digits.target

clf = svm.SVC(gamma = 0.0001, C=100)
clf.fit(X,Y)

cv2.imshow("Image", digits.images[42])
print(clf.predict(X[42]))

cv2.waitKey(0)
cv2.destroyAllWindows()

#print(clf.predict([[1,1]]))