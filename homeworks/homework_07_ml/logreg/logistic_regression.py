#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn import metrics


class LogisticRegression:
    def __init__(self, n_iter=100, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.n_iter = n_iter
        self.lambda_coef = lambda_coef
        self.regulatization = regulatization
        self.alpha = alpha
        self.weights = np.array([])

    def fit(self, x_train, y_train):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x_train = np.concatenate((np.ones((x_train.shape[0], 1)), x_train), axis=1)
        self.weights = np.ones((x_train.shape[1], np.amax(y_train) + 1))
        for n in np.arange(self.n_iter):
            for i in np.arange(self.weights.shape[0]):
                for j in np.arange(self.weights.shape[1]):
                    for m in np.arange(y_train.shape[0]):
                        self.weights[i, j] -= self.lambda_coef * np.exp(x_train[m, :] @ self.weights[:, j]) *\
                                              x_train[m, i] / np.sum(np.exp(x_train[m, :] @ self.weights))
                        if j == y_train[m, 0]:
                            self.weights[i, j] += self.lambda_coef * x_train[m, i]

    def predict(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        x_test = np.concatenate((np.ones((x_test.shape[0], 1)), x_test), axis=1)
        y_pred = x_test @ self.weights
        for i in np.arange(y_pred.shape[0]):
            y_pred[i, :] = np.exp(y_pred[i, :]) / np.sum(np.exp(y_pred[i, :]))
        y_pred = np.argmax(y_pred, axis=1).reshape(-1, 1)
        return y_pred

    def predict_proba(self, x_test):
        """
        Predict probability using model.
        :param x_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        x_test = np.concatenate((np.ones((x_test.shape[0], 1)), x_test), axis=1)
        y_pred = x_test @ self.weights
        for i in np.arange(y_pred.shape[0]):
            y_pred[i, :] = np.exp(y_pred[i, :])/np.sum(np.exp(y_pred[i, :]))
        return y_pred

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.weights


# x_train = np.random.randint(low=-9, high=10, size=(6, 3))
# x_train_ones = np.concatenate((np.ones((x_train.shape[0], 1)), x_train), axis=1)
# weights = np.random.randint(low=-9, high=10, size=(4, 3))
# y_train = np.argmax(x_train_ones @ weights, axis=1).reshape(-1, 1)
# x_test = np.random.randint(low=-9, high=10, size=(6, 3))
# x_test_ones = np.concatenate((np.ones((x_test.shape[0], 1)), x_test), axis=1)
# y_true = np.argmax(x_test_ones @ weights, axis=1).reshape(-1, 1)
# test = LogisticRegression(lambda_coef=2)
# test.fit(x_train, y_train)
# print(test.predict_proba(x_test))
# for i in np.arange(y_true.shape[0]):
#     print(test.predict(x_test)[i, :], end=' ')
#     print(y_true[i, :])
# print(metrics.log_loss(y_true, test.predict_proba(x_test)))
