#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn import metrics


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regularization=None, alpha=0.5):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_coef = lambda_coef
        self.regularization = regularization
        self.alpha = alpha
        self.weights = np.array([])
        self.learned = False

    def fit(self, x_train, y_train, n_iter=50):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x_train = np.concatenate((np.ones((x_train.shape[0], 1)), x_train), axis=1)
        self.weights = np.ones((x_train.shape[1], np.amax(y_train) + 1))
        der_amend = 0
        if self.regularization == 'L1':
            der_amend = 2 * self.alpha * self.weights
        elif self.regularization == 'L2':
            der_amend = self.alpha * np.ones((self.weights.shape[0], self.weights.shape[1]))
        elif self.regularization is None:
            der_amend = np.zeros((self.weights.shape[0], self.weights.shape[1]))
        for n in np.arange(n_iter):
            for i in np.arange(self.weights.shape[0]):
                for j in np.arange(self.weights.shape[1]):
                    for m in np.arange(y_train.shape[0]):
                        self.weights[i, j] -= self.lambda_coef * np.exp(x_train[m, :] @ self.weights[:, j]) *\
                                              x_train[m, i] / np.sum(np.exp(x_train[m, :] @ self.weights)) +\
                                              der_amend[i, j]
                        if j == y_train[m, 0]:
                            self.weights[i, j] += self.lambda_coef * x_train[m, i]
        self.learned = True

    def predict(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.learned:
            x_test = np.concatenate((np.ones((x_test.shape[0], 1)), x_test), axis=1)
            y_pred = x_test @ self.weights
            for i in np.arange(y_pred.shape[0]):
                y_pred[i, :] = np.exp(y_pred[i, :]) / np.sum(np.exp(y_pred[i, :]))
            y_pred = np.argmax(y_pred, axis=1).reshape(-1, 1)
            return y_pred
        else:
            print("Model isn't learned")

    def predict_proba(self, x_test):
        """
        Predict probability using model.
        :param x_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        if self.learned:
            x_test = np.concatenate((np.ones((x_test.shape[0], 1)), x_test), axis=1)
            y_pred = x_test @ self.weights
            for i in np.arange(y_pred.shape[0]):
                y_pred[i, :] = np.exp(y_pred[i, :])/np.sum(np.exp(y_pred[i, :]))
            return y_pred
        else:
            print("Model isn't learned")

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if self.learned:
            return self.weights
        else:
            print("Model isn't learned")
