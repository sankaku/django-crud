from django.contrib import admin
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    """
    Representation in `Project` admin page
    """
    list_display = ['name', 'color']


class TaskAdmin(admin.ModelAdmin):
    """
    Representation in `Task` admin page
    """
    list_display = ['project', 'start_time', 'end_time', 'content']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
