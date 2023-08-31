from django.urls import path
from myapp import views

urlpatterns = [
    path('task_data', views.task_view, name='task'),
]