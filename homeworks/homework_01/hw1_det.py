#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    A = list_of_lists
    if len(A[0]) != len(A):
        return None
    determinant = 0
    if len(A) == 1:
        return A[0][0]
    new_matr = [[0 for _ in range(len(A) - 1)] for _ in range(len(A) - 1)]
    for i in range(len(A)):
        j_0 = 0
        j = 1
        while j < len(A):
            k = 0
            k_0 = 0
            while k < len(A):
                if k == i:
                    k += 1
                    continue
                else:
                    new_matr[j_0][k_0] = A[j][k]
                    k_0 += 1
                    k += 1
            j_0 += 1
            j += 1
        res = calculate_determinant(new_matr)
        determinant += ((-1) ** i) * A[0][i] * res
    return determinant
