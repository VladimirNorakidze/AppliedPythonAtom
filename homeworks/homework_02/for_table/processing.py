#!/usr/bin/env python
# coding: utf-8


def data_to_json(data):
    lines = data.split("\n")
    output_list = []
    a = {}
    if len(lines[0].split("\t")) != 4 or lines[0] == "":
        return False
    for i in range(1, len(lines)-1):
        line = lines[i]
        line_list = line.split("\t")
        if len(line_list) != 4 or line_list[0] == "":
            return False
        a = {"Название": line_list[0],
             "Ссылка": line_list[1],
             "Теги": line_list[2],
             "Оценка": line_list[3]
             }
        output_list.append(a)
    return output_list


def check_data(data, json_status=False):
    if not json_status:
        if data == "file_not_found":
            print("Файл не валиден")
            return False
        elif not data:
            print("Формат не валиден")
            return False
        else:
            return True
    else:
        keys = ["Название", "Ссылка", "Теги", "Оценка"]
        for var in data:
            for key in keys:
                if key not in var:
                    print("Формат не валиден")
                    return False
    return True
