#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn import metrics


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    loss = 0
    for i in np.arange(y_true.shape[0]):
        loss += np.log(y_pred[i, y_true[i, 0]])
    return -loss/y_true.shape[0]


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    confusion = confusion_matrix(y_true, np.argmax(y_pred, axis=1).reshape(-1, 1))
    return np.trace(confusion)/np.sum(confusion)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    confusion = confusion_matrix(y_true, np.argmax(y_pred, axis=1).reshape(-1, 1))
    result = np.array([])
    for i in np.arange(y_pred.shape[1]):
        result = np.append(result, confusion[i, i]/np.sum(confusion[:, i]))
    return result


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    confusion = confusion_matrix(y_true, np.argmax(y_pred, axis=1).reshape(-1, 1))
    result = np.array([])
    for i in np.arange(y_pred.shape[1]):
        result = np.append(result, confusion[i, i]/np.sum(confusion[i, :]))
    return result


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    tpr = recall(y_true, y_pred)
    fpr = 1 - presicion(y_true, y_pred)
    return fpr*tpr/2 + (1 + tpr)*(1 - fpr)/2


def confusion_matrix(y_true, y_pred):
    confusion = np.zeros((y_pred.shape[0], y_pred.shape[0]))
    for i, j in np.concatenate((y_true, y_pred), axis=1):
        confusion[i, j] += 1
    return confusion
