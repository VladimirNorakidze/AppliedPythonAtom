#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        """
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        """
        full_list = []
        output_list = []
        for var in list_of_lists:
            full_list.extend(var)
        full_list = list(map(lambda x: (x, x), full_list))
        h = MaxHeap(full_list)
        length = k if k < len(h.heap) else len(h.heap)
        for i in range(length):
            output_list.append(h.extract_maximum()[0])
        return output_list
