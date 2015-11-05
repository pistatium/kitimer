# coding: utf-8

from django.db import models
from django.utils import timezone

from app.users.models import User
from app.timer.models import DayLog


class Project(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_projects(cls):
        return cls.objects.all()


class ProjectLog(models.Model):
    project = models.ForeignKey(Project)
    day_log = models.ForeignKey(DayLog, related_name='projects')
    commit_rate = models.FloatField(default=1.0)
    memo = models.TextField(blank=True)

    def __str__(self):
        return "{} {}".format(self.day_log, self.project)

    @classmethod
    def save_projects(cls, day_log, project_names):
        logs = []
        for name in project_names:
            project = Project.objects.get(pk=name)
            log = cls(
                project=project,
                day_log=day_log,
                commit_rate= 1 / len(project_names),
            )
            log.save()
            logs.append(log)
        return logs

    @classmethod
    def get_logs(cls, date=None):
        if not date:
            date = timezone.now().date()
        return cls.objects.filter(day_log__date=date)
