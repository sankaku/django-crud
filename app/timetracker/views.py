from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Task
from django.urls import reverse
from datetime import datetime
from .forms import TaskForm


def index(request):
    tasks_list = Task.objects.order_by('start_time')
    context = {
        'tasks_list': tasks_list,
    }

    return render(request, 'timetracker/index.html', context)


def add_task(request):
    project_list = Project.objects.order_by('id')
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    initial_time = {'start_time': now, 'end_time': now}
    new_task_form = TaskForm(initial=initial_time)
    context = {
        'project_list': project_list,
        'new_task_form': new_task_form,
    }

    return render(request, 'timetracker/add_task.html', context)


def save_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        project_id = form.cleaned_data['project']
        project = get_object_or_404(Project, pk=project_id)
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        content = form.cleaned_data['content']
        task = Task(project=project, start_time=start_time,
                    end_time=end_time, content=content)
        task.save()
        return HttpResponseRedirect(reverse('timetracker:index'))

    else:
        project_list = Project.objects.order_by('id')
        context = {
            'project_list': project_list,
            'new_task_form': form,
            'selected_project': int(form.cleaned_data['project']),
        }
        return render(request, 'timetracker/add_task.html', context)
