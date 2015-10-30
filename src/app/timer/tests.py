# coding: utf-8

from datetime import datetime

from django.test import TestCase
from django.utils import timezone


from app.users.models import User
from app.timer.models import TimeManager, TimerLog, DayLog


class TimerTest(TestCase):

    ARRIVED_AT = timezone.make_aware(datetime(2015, 10, 1, 9, 50))
    LEFT_AT = timezone.make_aware(datetime(2015, 10, 1, 19, 30))

    def setUp(self):
        self.user = User(name="test")
        self.user.save()

    def test_arrived(self):
        manager = TimeManager(self.user)
        manager.arrived(self.ARRIVED_AT)

        day_log = DayLog.findOrCreate(self.user, self.ARRIVED_AT.date())
        timer_logs = TimerLog.findAll(self.user, self.ARRIVED_AT.date())

        self.assertEqual(day_log.arrived_at, self.ARRIVED_AT)
        self.assertEqual(len(timer_logs), 1)
        self.assertEqual(timer_logs[0].action_type, TimerLog.ARRIVED)
        self.assertEqual(timer_logs[0].time, self.ARRIVED_AT)

    def test_left(self):
        manager = TimeManager(self.user)
        manager.left(self.LEFT_AT)

        day_log = DayLog.findOrCreate(self.user, self.LEFT_AT.date())
        timer_logs = TimerLog.findAll(self.user, self.LEFT_AT.date())

        self.assertEqual(day_log.left_at, self.LEFT_AT)
        self.assertEqual(len(timer_logs), 1)
        self.assertEqual(timer_logs[0].action_type, TimerLog.LEFT)
        self.assertEqual(timer_logs[0].time, self.LEFT_AT)

    def test_arrive_and_left(self):
        manager = TimeManager(self.user)
        manager.arrived(self.ARRIVED_AT)
        manager.left(self.LEFT_AT)

        day_log = DayLog.findOrCreate(self.user, self.ARRIVED_AT.date())
        timer_logs = TimerLog.findAll(self.user, self.ARRIVED_AT.date())

        self.assertEqual(day_log.arrived_at, self.ARRIVED_AT)
        self.assertEqual(day_log.left_at, self.LEFT_AT)
        self.assertEqual(day_log.work_time, 520)
        self.assertEqual(len(timer_logs), 2)
