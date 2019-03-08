#!/usr/bin/env python
# coding: utf-8


class IncorrectFormat(Exception):
    pass


def data_to_json(data):
    lines = data.split("\n")
    output_list = []
    a = {}
    for i in range(1, len(lines)-1):
        line = lines[i]
        line_list = line.split("\t")
        if len(line_list) != 4 or line_list[0] == "":
            raise IncorrectFormat("Формат не валиден")
        a = {"Название": line_list[0],
             "Ссылка": line_list[1],
             "Теги": line_list[2],
             "Оценка": line_list[3]
             }
        output_list.append(a)
    return output_list


def check_data(data):
    keys = ["Название", "Ссылка", "Теги", "Оценка"]
    for var in data:
        for key in keys:
            if key not in var:
                raise IncorrectFormat("Формат не валиден")
    return True
