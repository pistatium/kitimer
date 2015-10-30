# coding: utf-8

from django.shortcuts import render
from django.views.generic import View

from app.users.models import User


class HomeView(View):
    def get(self, request):
        users = User.get_users(None)
        return render(request, "index.html", {
            "users": users,
        })