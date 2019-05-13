#!/usr/bin/env python
# coding: utf-8

import numpy as np


class LinearRegression:

    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5, lim_error=1.0e-5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_coef = lambda_coef
        self.regularization = regulatization
        if regulatization is None:
            self.alpha = 0
        else:
            self.alpha = alpha
        self._weights = None
        self.lim_error = lim_error

    @staticmethod
    def _normalization(x):
        return (x - x.mean())/(x.std() + 1.0e-7)

    def _gradient(self, x_train, y_train, add_term):
        y_hat = self.predict(x_train)
        return (2 * np.dot(x_train.T, (y_hat - y_train))) / x_train.shape[0] + add_term

    def fit(self, x_train, y_train):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :return: None
        """
        assert x_train.shape[0] == y_train.shape[0], "Размерности X и Y не совпадают"
        if self._weights is None:
            self._weights = np.random.randn(x_train.shape[1])
        x_train = self._normalization(x_train)
        old = np.ones_like(self._weights)
        err = np.sum(old)
        while err > self.lim_error:
            if self.regularization.upper() == "L1":
                add_term = self.alpha*np.sign(self._weights)
            else:
                add_term = 2 * self.alpha * self._weights
            self._weights -= self.lambda_coef * self._gradient(x_train, y_train, add_term)
            self._gradient(x_train, y_train, add_term)
            new = self._weights
            err = np.sum(np.abs(old - new))
            old = new
        return None

    def predict(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        if self._weights is None:
            raise AssertionError("Модель не обучена")
        x_test = self._normalization(x_test)
        return np.dot(self._weights, x_test.T)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if self._weights is None:
            raise AssertionError("Модель не обучена")
        return self._weights
