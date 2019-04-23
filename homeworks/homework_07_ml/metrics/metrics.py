#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    return -1/y_true.shape[0]*np.sum(y_true*np.log(y_pred) + (1 - y_true)*np.log(1 - y_pred))


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return np.sum(np.equal(y_true, y_pred))/y_pred.shape[0]


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return np.sum(y_pred*y_true)/np.sum(y_pred)


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return np.sum(y_pred*y_true)/np.sum(y_true)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    zeros = (y_true == 0)
    fpr = np.sum(zeros & (y_pred == 1)) / np.sum(zeros)
    return (1 + recall(y_true, y_pred) - fpr)/2
