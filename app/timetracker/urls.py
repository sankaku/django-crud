from django.urls import path
from . import views

app_name = 'timetracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('task/new/', views.add_task, name='add_task'),
    path('task/create/', views.create_task, name='create_task'),
]
