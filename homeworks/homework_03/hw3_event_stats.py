#!/usr/bin/env python
# coding: utf-8


import collections


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.activity = collections.deque([])

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        self.activity.appendleft((user_id, time))

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        users = []
        for var in self.activity:
            if time - self.FIVE_MIN <= var[1] <= time:
                users.append(var[0])
            else:
                break
        res = collections.Counter(users)
        if count in res.values():
            result = list(res.values()).count(count)
            print(result)
            return result
        else:
            return 0
