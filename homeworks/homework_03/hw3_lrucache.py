#!/usr/bin/env python
# coding: utf-8


import time
import collections


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        self.maxsize = maxsize
        self.ttl = ttl
        self._args_cache = collections.deque([])
        self._time_cache = collections.deque([])
        self._result_cache = collections.deque([])

    def _clearing_cache(self):
        while True:
            if time.time() - self._time_cache[-1] > self.ttl:
                self._time_cache.pop()
                self._args_cache.pop()
                self._result_cache.pop()

    def _checking_cache(self, args, kwargs):
        for i, var in enumerate(self._args_cache):
            if args == var[0]:
                return [True, i]
        else:
            self._put_cache(args, kwargs)
            return [False, -1]

    def _put_cache(self, args, kwargs):
        self._args_cache.appendleft((args, kwargs))
        self._time_cache.appendleft(time.time())

    def __call__(self, *args, **kwargs):
        # TODO вызов функции
        if callable(args[0]):
            self.function = args[0]
        else:
            if self._time_cache:
                self._clearing_cache()
            check_status, idx = self._checking_cache(args, kwargs)
            if check_status:
                return self._result_cache[idx]
            else:
                result = self.function(*args, **kwargs)
                self._result_cache.appendleft(result)
                return result
