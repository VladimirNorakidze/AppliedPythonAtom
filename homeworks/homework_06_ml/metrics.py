#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    mse_loss = np.sum((y_true[:] - y_hat[:])**2) / len(y_true)
    return mse_loss


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    mae_loss = np.sum(np.abs(y_true[:] - y_hat[:])) / len(y_true)
    return mae_loss


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    mean_y = np.sum(y_true) / len(y_true)
    ss_tot = np.sum((y_true[:] - mean_y)**2)
    ss_res = mse(y_true, y_hat) * len(y_true)
    r2_score_loss = 1 - ss_res / ss_tot
    return r2_score_loss
