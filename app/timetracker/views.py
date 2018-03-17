from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task


def index(request):
    tasks_list = Task.objects.order_by('start_time')
    context = {
        'tasks_list': tasks_list,
    }

    return render(request, 'timetracker/index.html', context)
