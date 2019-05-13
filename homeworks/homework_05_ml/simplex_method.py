#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    equations = a.shape[0]
    variables = a.shape[1]
    result = np.zeros(variables)
    c = np.expand_dims(c, axis=0)
    matrix = np.concatenate((a, -c), axis=0)
    matrix = np.concatenate((matrix, np.eye(equations + 1)), axis=1)
    b = np.expand_dims(np.append(b, 0), axis=1)
    matrix = np.concatenate((matrix, b), axis=1)
    while not all(matrix[-1] >= 0):
        pivot_column = np.argmin(matrix[-1])
        pivot_row = np.argmin(matrix[:, -1][:-1] / (matrix[:, pivot_column][:-1] + 1.0e-10))
        matrix[pivot_row, :] /= matrix[pivot_row, pivot_column]
        for idx in range(matrix.shape[0]):
            if idx != pivot_row:
                matrix[idx, :] = -matrix[idx, pivot_column]*matrix[pivot_row, :] + matrix[idx, :]
    for row in range(equations):
        for var in range(variables):
            if matrix[row, var] == 1:
                result[var] = matrix[row, -1]
                break
    return result
