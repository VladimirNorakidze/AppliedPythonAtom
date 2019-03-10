#!/usr/bin/env python
# coding: utf-8


def max_values(data):
    max_name, max_link, max_tag, max_mark = (0, 0, 0, 0)
    for var in data:
        if len(var["Название"]) > max_name:
            max_name = len(var["Название"])
        if len(var["Ссылка"]) > max_link:
            max_link = len(var["Ссылка"])
        if len(var["Теги"]) > max_tag:
            max_tag = len(var["Теги"])
    return max_name, max_link, max_tag


def line_creator(func):
    def wrapper(data):
        head_str = ""
        max_name, max_link, max_tag, table_len, table_data = func(data)
        head_name = (max_name + 4 - len("Название")) // 2
        head_link = (max_link + 4 - len("Ссылка")) // 2
        head_tag = (max_tag + 4 - len("Теги")) // 2
        head_mark = 2
        if table_len != 0:
            head_str += "|" + " "*head_name + "Название" + " "*head_name + \
                        "|" + " "*head_link + "Ссылка" + " "*head_link + \
                        "|" + " "*head_tag + "Теги" + " "*head_tag + \
                        "|" + " "*head_mark + "Оценка" + " "*head_mark + "|"
        else:
            head_str += "|  Название  |  Ссылка  |  Теги  |  Оценка  |"
            table_len = len(head_str)
        return "-" * table_len + "\n" + head_str + \
               "\n" + table_data + "-" * table_len
    return wrapper


@line_creator
def creator(data):
    table = ""
    table_len = 0
    max_name, max_link, max_tag = max_values(data)
    mark_len = len("Оценка") + 1
    first = True
    for var in data:
        name = var['Название']
        link = var['Ссылка']
        tags = var['Теги']
        mark = var['Оценка']
        table += f"|  {name}" + " " * (2 + max_name - len(name))
        table += f"|  {link}" + " " * (2 + max_link - len(link))
        table += f"|  {tags}" + " " * (2 + max_tag - len(tags))
        table += "|" + " " * mark_len + f"{mark}" + "  |"
        if first:
            table_len = len(table)
            first = False
        table += "\n"
    return max_name, max_link, max_tag, table_len, table
