from django.urls import path
from . import views

app_name = 'timetracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.list_projects, name='list_projects'),
    path('task/new/', views.add_task, name='add_task'),
    path('task/save/', views.save_task, name='save_task'),
    path('task/<int:task_id>/', views.show_task, name='show_task'),
    path('project/new/', views.add_project, name='add_project'),
    path('project/save/', views.save_project, name='save_project'),
    path('project/<int:project_id>/', views.show_project, name='show_project'),
]
