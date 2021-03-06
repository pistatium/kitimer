# coding: utf-8

from datetime import datetime, time

from django.db import models
from django.db import transaction
from django.utils import timezone

from app.users.models import User
from .errors import AlreadyInputError, BlankArrivedAtError, BlankLeftAtError


class TimerLog(models.Model):
    ARRIVED = "arrived"
    LEFT = "left"
    ACTION_TYPES = (
        (ARRIVED, '出社'),
        (LEFT, '退社')
    )
    time = models.DateTimeField()
    action_type = models.CharField(choices=ACTION_TYPES, max_length=16)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} {} {}".format(self.user, self.action_type, self.time)

    @classmethod
    def findAll(cls, user, date):
        start_day = timezone.make_aware(datetime.combine(date, time.min))
        end_day = timezone.make_aware(datetime.combine(date, time.max))
        range = (start_day, end_day)
        logs = cls.objects.filter(user=user).filter(time__range=range)
        if logs:
            return logs
        return []


class DayLog(models.Model):
    INVALID_WORK_TIME = -1

    date = models.DateField()
    arrived_at = models.DateTimeField(null=True, blank=True)
    left_at = models.DateTimeField(null=True, blank=True)
    work_time = models.IntegerField(default=INVALID_WORK_TIME)  # min
    rest_time = models.IntegerField(default=60)  # min
    user = models.ForeignKey(User)

    class Meta:
        index_together = [
            ("date", "user"),
        ]

    def __str__(self):
        return "{} {}".format(self.date, self.user)

    @classmethod
    def find_or_create(cls, user, date):
        log = cls.objects.filter(user=user, date=date).first()
        if log:
            return log
        return DayLog(user=user, date=date)

    @classmethod
    def get_logs(cls, date=None):
        if not date:
            date = timezone.now().date()
        return cls.objects.filter(date=date)


class TimeManager:
    def __init__(self, user):
        self.user = user

    @transaction.atomic
    def arrived(self, arrived_at=None, date=None):
        if not arrived_at:
            arrived_at = timezone.now()
        if not date:
            date = arrived_at.date()

        day_log = DayLog.find_or_create(self.user, date)
        if day_log.arrived_at:
            raise AlreadyInputError(self.user, date)
        day_log.arrived_at = arrived_at
        day_log.save()

        time_log = TimerLog(
            time=arrived_at,
            action_type=TimerLog.ARRIVED,
            user=self.user
        )
        time_log.save()
        return day_log

    @transaction.atomic
    def left(self, left_at=None, date=None):
        if not left_at:
            left_at = timezone.now()
        if not date:
            date = left_at.date()
        day_log = DayLog.find_or_create(self.user, date)
        if day_log.left_at:
            raise AlreadyInputError(self.user, date)
        day_log.left_at = left_at
        if day_log.arrived_at:
            self.clean(day_log=day_log)
        day_log.save()

        time_log = TimerLog(
            time=left_at,
            action_type=TimerLog.LEFT,
            user=self.user
        )
        time_log.save()
        return day_log

    def clean(self, date=None, day_log=None):
        if not day_log:
            if not date:
                date = timezone.now().date()
            day_log = DayLog.find_or_create(self.user, date)

        if not day_log.arrived_at:
            raise BlankArrivedAtError(self.user, date)
        if not day_log.left_at:
            raise BlankLeftAtError(self.user, date)
        in_office_minutes = (day_log.left_at - day_log.arrived_at).seconds / 60
        day_log.work_time = max(in_office_minutes - day_log.rest_time, 0)
        day_log.save()
