from django.contrib import admin
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    """
    Representation in `Project` admin page
    """


class TaskAdmin(admin.ModelAdmin):
    """
    Representation in `Task` admin page
    """


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
