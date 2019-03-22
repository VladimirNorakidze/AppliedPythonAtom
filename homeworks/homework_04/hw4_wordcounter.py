#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager, Queue
import os


def word_count_inference(path_to_dir):
    """
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    """

    def func(q1, q2):
        item = q1.get()
        if item is not None:
            filename, path = item
            with open(path + "/" + filename, "r") as f:
                obj = f.read().strip()
            num_words = len(obj.split())
            q2.put((filename, num_words))

    manager = Manager()
    result = manager.dict()
    files = os.listdir(path=path_to_dir)
    q1 = Queue(5)
    q2 = Queue(5)
    for file in files:
        p = Process(target=func, args=(q1, q2))
        p.start()
        q1.put((file, path_to_dir))
        res = q2.get()
        result.update({res[0]: res[1]})
        p.join()
    total = sum(result.values())
    result.update({"total": total})
    return result
