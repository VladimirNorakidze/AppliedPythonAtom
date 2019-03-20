#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self, bucket_num=64):
        # TODO Сделать правильно =)
        super().__init__(bucket_num=bucket_num)

    def get(self, value, default_value=None):
        # TODO достаточно переопределить данный метод
        result = super().get(value, default_value=default_value)
        if result is not None:
            return True
        else:
            return None

    def put(self, value):
        # TODO метод put, нужно переопределить данный метод
        super().put(value, value)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.capacity

    def values(self):
        # TODO возвращать итератор значений
        return super().values()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        new_hashset = HashSet()
        for element in another_hashset.keys():
            if element in self.keys():
                new_hashset.put(element)
        return new_hashset
