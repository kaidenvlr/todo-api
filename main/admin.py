from django.contrib import admin

from main.models import Team, TaskLevel, TaskList, Task


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(TaskLevel)
class TaskLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'team']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'task_list', 'task_level', 'is_done']
