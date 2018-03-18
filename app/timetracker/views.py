from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Task
from django.urls import reverse
from datetime import datetime


def index(request):
    tasks_list = Task.objects.order_by('start_time')
    context = {
        'tasks_list': tasks_list,
    }

    return render(request, 'timetracker/index.html', context)


def add_task(request):
    project_list = Project.objects.order_by('id')
    now = datetime.now().strftime("%Y-%m-%dT%H:%M")
    context = {
        'project_list': project_list,
        'now': now,
    }

    return render(request, 'timetracker/add_task.html', context)


def create_task(request):
    try:
        project_id = request.POST['project']
        project = get_object_or_404(Project, pk=project_id)
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        content = request.POST['content']
        task = Task(project=project, start_time=start_time,
                    end_time=end_time, content=content)
        task.save()
    except (IndexError) as e:
        project_list = Project.objects.order_by('id')
        context = {
            'error_message': 'Incorrect input!\n{0}\n{1}'.format(e.args),
            'project_list': project_list,
        }
        return render(request, 'timetracker/add_task.html', context)
    else:
        return HttpResponseRedirect(reverse('timetracker:index'))
