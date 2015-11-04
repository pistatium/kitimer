# coding: utf-8

from django.db import models
from django.utils import timezone

from app.users.models import User


class Project(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_projects(cls):
        return cls.objects.all()


class ProjectLog(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    date = models.DateField()
    commit_rate = models.FloatField(default=1.0)
    memo = models.TextField(blank=True)

    def __str__(self):
        return "{} {} {}".format(self.project, self.user, self.date)

    @classmethod
    def save_projects(cls, user, project_names, date=None):
        if not date:
            date = timezone.now().date()
        logs = []
        for name in project_names:
            project = Project.objects.get(pk=name)
            log = cls(
                project=project,
                user=user,
                date=date,
                commit_rate= 1 / len(project_names),
            )
            log.save()
            logs.append(log)
        return logs
