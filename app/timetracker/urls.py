from django.urls import path
from . import views

app_name = 'timetracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('task/new/', views.add_task, name='add_task'),
    path('task/save/', views.save_task, name='save_task'),
]
