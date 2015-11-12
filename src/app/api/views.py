# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

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


class DayLogFilter(django_filters.FilterSet):
    user_id = django_filters.ModelChoiceFilter(name='user_id', to_field_name='id', queryset=User.objects.all())
    date_range = django_filters.DateFromToRangeFilter(name='date')

    class Meta:
        model = DayLog
        fields = ['date_range', 'user_id']


class DayLogViewSet(viewsets.ModelViewSet):
    queryset = DayLog.get_logs()
    #queryset = DayLog.objects.all()
    serializer_class = DayLogSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DayLogFilter
