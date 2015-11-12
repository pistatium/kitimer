# coding: utf-8

from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import ReportView

urlpatterns = [
    url(r'^$', ReportView.as_view(), name='report'),
]