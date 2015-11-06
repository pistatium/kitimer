# coding: utf-8


class TimerException(Exception):
    def __init__(self, user, date):
        self.user = user
        self.date = date


class AlreadyInputError(TimerException):
    def __str__(self):
        return "Already Input! user={}, date={}".format(self.user, self.date)


class BlankArrivedAtError(TimerException):
    def __str__(self):
        return "ArrivedAt is blank! user={}, date={}".format(self.user, self.date)


class BlankLeftAtError(TimerException):
    def __str__(self):
        return "LeftAt is blank! user={}, date={}".format(self.user, self.date)