# coding: utf-8

import json

from django.shortcuts import render
from django.views.generic import View
from django.core import serializers
from django.http import JsonResponse

from app.users.models import User
from app.projects.models import Project, ProjectLog
from app.timer.models import TimeManager, DayLog
from app.timer.errors import TimerException

class HomeView(View):
    def get(self, request):
        users = User.get_users(None)
        projects = Project.get_projects()
        day_logs = []
        return render(request, "index.html", {
            "users": serializers.serialize('json', users),
            "projects": serializers.serialize('json', projects),
            "day_logs": serializers.serialize('json', day_logs),
        })


class ArrivedApiView(View):
    def post(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            timer = TimeManager(user)
            timer.arrived()
            return JsonResponse({'success': True})
        except TimerException as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


class LeftApiView(View):
    def post(self, request, user_id):
        try:
            data=json.loads(request.body.decode('utf-8'))
            user = User.objects.get(pk=user_id)
            timer = TimeManager(user)
            day_log = timer.left()
            ProjectLog.save_projects(day_log, data["joined_projects"])
            return JsonResponse({'success': True})
        except TimerException as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
