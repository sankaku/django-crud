from django.db import models


class Project(models.Model):
    """
    Types of projects.

    name: the name of the project
    color: color code of the project. This is for displaying projects in view page.
    """
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    A single record of doing project.

    start_time: start time
    end_time: end time
    project: the project that the task belongs to
    content: specific content
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    content = models.CharField(max_length=200)
