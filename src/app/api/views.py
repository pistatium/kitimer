# coding: utf-8

from rest_framework import viewsets

from .serializers import UserSerializer, ProjectLogSerializer, DayLogSerializer
from app.users.models import User
from app.projects.models import ProjectLog
from app.timer.models import DayLog


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.get_users(status=None)
    serializer_class = UserSerializer


class ProjectLogViewSet(viewsets.ModelViewSet):
    queryset = ProjectLog.get_logs()
    serializer_class = ProjectLogSerializer


class DayLogViewSet(viewsets.ModelViewSet):
    queryset = DayLog.get_logs()
    serializer_class = DayLogSerializer
