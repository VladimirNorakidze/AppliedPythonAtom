#!/usr/bin/env python
# coding: utf-8


def data_to_json(data):
    lines = data.split("\n")
    output_list = []
    a = {}
    for i in range(1, len(lines)-1):
        line = lines[i]
        line_list = line.split("\t")
        a = {"Название": line_list[0],
             "Ссылка": line_list[1],
             "Теги": line_list[2],
             "Оценка": line_list[3]
             }
        output_list.append(a)
    return output_list
