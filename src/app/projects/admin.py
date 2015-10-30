from django.contrib import admin

from .models import Project, ProjectLog


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectLog)
class ProjectLogAdmin(admin.ModelAdmin):
    pass