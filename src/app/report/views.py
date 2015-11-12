# coding: utf-8

from django.views.generic import View
from django.shortcuts import render


class ReportView(View):
    def get(self, request):
        return render(request, "report.html")
