from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Task
from django.urls import reverse
from datetime import datetime
from .forms import TaskForm, ProjectForm


def index(request):
    tasks_list = Task.objects.order_by('start_time')
    context = {
        'tasks_list': tasks_list,
    }

    return render(request, 'timetracker/index.html', context)


def list_projects(request):
    projects_list = Project.objects.order_by('id')
    context = {
        'projects_list': projects_list,
    }
    return render(request, 'timetracker/list_projects.html', context)


def show_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_list = Project.objects.order_by('id')
    initial_data = {
        'project': task.project,
        'start_time': task.start_time,
        'end_time': task.end_time,
        'content': task.content,
    }
    form = TaskForm(initial=initial_data)

    context = {
        'project_list': project_list,
        'selected_project': task.project.id,
        'task_form': form,
    }

    return render(request, 'timetracker/task.html', context)


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


def add_project(request):
    new_project_form = ProjectForm()
    context = {
        'new_project_form': new_project_form,
    }

    return render(request, 'timetracker/add_project.html', context)


def save_project(request):
    form = ProjectForm(request.POST)

    if form.is_valid():
        name = form.cleaned_data['name']
        color = form.cleaned_data['color']
        project = Project(name=name, color=color)
        project.save()
        return HttpResponseRedirect(reverse('timetracker:index'))

    else:
        context = {
            'new_project_form': form,
        }
        return render(request, 'timetracker/add_project.html', context)
