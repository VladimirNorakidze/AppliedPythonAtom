#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    def append_obj(dic, key, obj):
        if isinstance(dic[key], list):
            if isinstance(obj, list):
                dic[key].extend(obj)
            else:
                dic[key].append(obj)
        else:
            dic[key] = [dic[key]]
            if isinstance(obj, list):
                dic[key].extend(obj)
            else:
                dic[key].append(obj)
        return dic

    def return_dict(obj, keys):
        newest_dict = {}
        if not isinstance(obj, (list, set, dict)):
            if keys in newest_dict:
                newest_dict = append_obj(newest_dict, keys, obj)
            else:
                newest_dict.update({obj: keys})
        else:
            for var in obj:
                returned = return_dict(var, key)
                for i, j in returned.items():
                    if i in newest_dict:
                        newest_dict = append_obj(newest_dict, i, j)
                    else:
                        newest_dict.update({i: j})
        return newest_dict

    if isinstance(source_dict, dict):
        new_dict = {}
        for key, value in source_dict.items():
                returned = return_dict(value, key)
                for i, j in returned.items():
                    if i in new_dict:
                        new_dict = append_obj(new_dict, i, j)
                    else:
                        new_dict.update({i: j})
        return new_dict
    else:
        return None
