from django.contrib import admin

from .models import TimerLog, DayLog


@admin.register(TimerLog)
class TimerLogAdmin(admin.ModelAdmin):
    pass


@admin.register(DayLog)
class DayLogAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'arrived_at', 'left_at')
    list_filter = ('user', 'date')
    pass
