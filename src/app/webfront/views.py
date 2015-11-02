# coding: utf-8

from django.shortcuts import render
from django.views.generic import View
from django.core import serializers

from app.users.models import User
from app.projects.models import Project


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
        pass


class LeftApiView(View):
    def post(self, request, user_id):
        pass