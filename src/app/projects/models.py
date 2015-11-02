# coding: utf-8

from django.db import models

from app.users.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)

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

