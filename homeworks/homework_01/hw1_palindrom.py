#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    phrase = input_string.lower()
    string = phrase
    inv_string = string[::-1]
    if string == inv_string:
        return True
    else:
        return False
