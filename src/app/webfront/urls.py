# coding: utf-8

from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import HomeView, ArrivedApiView, LeftApiView


urlpatterns = [
    url(r'arrived_dialog', TemplateView.as_view(template_name='arrived_dialog.html'), name='arrived_dialog'),
    url(r'left_dialog', TemplateView.as_view(template_name='left_dialog.html'), name='left_dialog'),
    url(r'api/users/(\d+)/arrived', ArrivedApiView.as_view(), name='arrived_api'),
    url(r'api/users/(\d+)/left', LeftApiView.as_view(), name='left_api'),

    url(r'^$', HomeView.as_view(), name='home'),
]