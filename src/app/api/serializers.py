# coding: utf-8

from rest_framework import serializers

from app.users.models import User
from app.projects.models import ProjectLog
from app.timer.models import TimerLog, DayLog


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'slack_name', 'icon_url')


class ProjectLogSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.StringRelatedField()

    class Meta:
        model = ProjectLog
        fields = ('project', 'day_log', 'commit_rate', 'memo')


class TimerLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimerLog
        fields = ('action_type', 'time', 'user')


class DayLogSerializer(serializers.ModelSerializer):
    project_logs = ProjectLogSerializer(many=True, read_only=True)

    class Meta:
        model = DayLog
        fields = ('arrived_at', 'left_at', 'user', 'date', 'project_logs', 'work_time', 'rest_time')
