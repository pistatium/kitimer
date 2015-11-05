# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, ProjectLogViewSet, DayLogViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'project_logs', ProjectLogViewSet)
router.register(r'day_logs', DayLogViewSet)

