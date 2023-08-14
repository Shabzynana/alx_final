from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.urls import reverse_lazy


from .form import TaskForm
from .models import Task
# Create your views here.


# class TaskListView(ListView):
#     model = Task
#     template_name = "todolist/task_list.html"

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todolist/task_detail.html"



class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    Fields = ['title', 'content']
    form_class = TaskForm
    template_name = "todolist/task_create.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    Fields = ['title', 'content']
    form_class = TaskForm
    template_name = "todolist/task_create.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user_id:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "todolist/task_delete.html"
    success_url = '/'
    success_message = "task was deleted successfully"

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user_id:
            return True
        return False
