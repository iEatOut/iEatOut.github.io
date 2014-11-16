import string
import os
from sklearn import svm
import numpy as np
import scipy
from scipy import sparse

def cross_validation(clf, X, Y, num_folds):
    """
    :param clf: a classifier to use for training (eg. SVM / MultinomialNaiveBayes ...)
    :param X: vectors
    :param Y: labels
    :param num_folds: number of folds
    :return: accuracy as the average of k-fold cross-validation.
    """
    X = np.array(X)
    #X = sparse.csr_matrix(X)
    #X = X.todense()

    fold_size = int(len(X)) / int(num_folds)
    fold_size = int(fold_size)
    i = 0
    i = int(i)
    accs = []
    for fold in range(num_folds):
        test_mat = X[i*fold_size : (i+1)*fold_size]
        test_labels = Y[i*fold_size : (i+1)*fold_size]

        train_mat = X[0:i*fold_size].tolist() + X[(i+1)*fold_size:].tolist()
        if i*fold_size == 0:
            train_labels = Y[(i+1)*fold_size:]
        else:
            train_labels = Y[0:i*fold_size] + Y[(i+1)*fold_size:]
        clf.fit(train_mat, train_labels)
        predicted_labels = clf.predict(test_mat)

        # finding accuracy:
        correct = 0
        
        for index in range(len(predicted_labels)):
            if predicted_labels[index] == test_labels[index]:
                correct += 1
        acc = float(correct) / float(len(predicted_labels))
        accs.append(acc)

    return np.mean(accs)
