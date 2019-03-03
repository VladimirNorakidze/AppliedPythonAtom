#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    bracket = {"(": ")", "{": "}", "[": "]"}
    spisok = []
    for c in input_string:
        if c in "({[":
            spisok.append(c)
        elif c in "}])":
            if len(spisok) != 0 and bracket[spisok[-1]] == c:
                spisok.pop()
            else:
                return False
    return True
