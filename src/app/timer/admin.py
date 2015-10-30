from django.contrib import admin

from .models import TimerLog, DayLog


@admin.register(TimerLog)
class TimerLogAdmin(admin.ModelAdmin):
    pass


@admin.register(DayLog)
class DayLogAdmin(admin.ModelAdmin):
    pass
