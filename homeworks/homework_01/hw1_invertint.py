#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    if number >= 0:
        str_number = str(number)
        inv_str_number = str_number[::-1]
        return int(inv_str_number)
    else:
        inv_str_number = "-" + str((-1)*number)[::-1]
        return int(inv_str_number)