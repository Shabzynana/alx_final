from django.urls import path
from .views import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
# from .views import list_view, detail_view, update_view, create_view


urlpatterns = [
    # path('',list_view, name="list"),
    # path('',TaskListView.as_view(), name="list_task"),
    path('create/task',TaskCreateView.as_view(), name="create_task"),
    path('task/<int:pk>',TaskDetailView.as_view(), name="task_detail"),
    path('task/<int:pk>/update',TaskUpdateView.as_view(), name="task_update"),
    path('task/<int:pk>/delete',TaskDeleteView.as_view(), name="task_delete"),



    # path('create/',create_view, name="create"),
    # path('detail/<int:id>', detail_view, name="detail"),
    # path('update/<int:id>', update_view, name="update"),
]
