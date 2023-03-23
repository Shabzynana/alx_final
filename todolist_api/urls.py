from django.urls import re_path as url
from django.urls import path, include
from .views import (
    TaskApiView,TaskIdApiView
)

urlpatterns = [

    path('api/task', TaskApiView.as_view()),
    path('api/task/<int:task_id>', TaskIdApiView.as_view()),
]
