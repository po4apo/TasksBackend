from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'isDone', 'created_at']


admin.site.register(Task, TaskAdmin)
