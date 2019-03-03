#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if (isinstance(x, int) or isinstance(x, float)) and \
            (isinstance(y, int) or isinstance(y, float)):
        if operator == "plus" or operator == "+":
            return x + y
        elif operator == "minus" or operator == "-":
            return x - y
        elif operator == "mult" or operator == "*":
            return x * y
        elif operator == "divide" or operator == "/":
            if y != 0:
                return x / y
            else:
                return None
        else:
            return None
    else:
        return None
