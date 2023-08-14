from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from user.models import User
from todolist.models import Task
from user.token import check_confirmed




@login_required(login_url='login')
@check_confirmed
def user_task(request, username):

    user = User.objects.filter(username=username).first()
    tasks = Task.objects.filter(user_id=user).order_by('end_date')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(tasks, 3) # 3 tasks per page
    try:
        page_task = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_task = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_task = paginator.page(paginator.num_pages)
    context = {
        'tasks': tasks,
        'page_task': page_task
    }
    return render(request, 'user/user_task.html', context)
