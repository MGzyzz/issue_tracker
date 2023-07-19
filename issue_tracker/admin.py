from django.contrib import admin
from issue_tracker.models.types_and_statuses import Status, Types
from issue_tracker.models.task import Task
from issue_tracker.models.project import Project

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'summary', 'status', 'type', 'time_of_create', 'update_time']
    list_filter = ['summary', 'description', 'status', 'type']
    search_fields = ['summary', 'status', 'type']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date']
    list_filter = ['title', 'description']
    search_fields = ['title']


admin.site.register(Status, StatusAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
# Register your models here.
