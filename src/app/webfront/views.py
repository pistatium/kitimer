# coding: utf-8

import json

from django.shortcuts import render
from django.views.generic import View
from django.core import serializers
from django.http import JsonResponse

from app.users.models import User
from app.projects.models import Project, ProjectLog
from app.timer.models import TimeManager


class HomeView(View):
    def get(self, request):
        users = User.get_users(None)
        projects = Project.get_projects()

        return render(request, "index.html", {
            "users": serializers.serialize('json', users),
            "projects": serializers.serialize('json', projects),
        })


class ArrivedApiView(View):
    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        timer = TimeManager(user)
        timer.arrived()
        return JsonResponse({'success': True})


class LeftApiView(View):
    def post(self, request, user_id):
        data=json.loads(request.body.decode('utf-8'))
        user = User.objects.get(pk=user_id)
        timer = TimeManager(user)
        timer.left()
        ProjectLog.save_projects(user, data["joined_projects"])
