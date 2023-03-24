from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_email_verification import send_email

from .forms import UserRegisterForm, LoginForm, UserUpdateForm
from .models import User
from todolist.models import Task
from .email import make_email, make_emaill
from .token import verify_token, check_confirmed

import datetime


def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # email = request.POST.get('email')
            get_user = User.objects.get(email=request.POST.get('email'))
            make_email(request, user, get_user)
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def resend(request):

    user = request.user.id
    get_user = User.objects.get(id=user)
    make_emaill(request, user, get_user)
    return redirect('unconfirmed')

def login_user(request):
    form = LoginForm()
    if request.method == 'GET':
        cache.set('next', request.GET.get('next', None))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username=form.cleaned_data['username'],
            username= request.POST.get('username')
            password= request.POST.get('password')

            try:
                user = User.objects.get(username=username)
                print(username)
            except:
                messages.error(request, "username does not exist")

            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,'Logged in successfully')

                next_url = cache.get('next')
                if next_url == None:
                    return redirect("index")
                return redirect(next_url)

            else:
                messages.error(request,'invalid username or password')

    return render(request, 'user/login.html',{'form': form})


def signout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("index")

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and verify_token.check_token(user, token):
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('index')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('index')

@login_required(login_url='login')
def unconfirmed(request):

    user = request.user.id
    print(user)
    current_user = User.objects.get(id=user)
    print (current_user.email)

    if current_user.confirmed:
        return redirect('index')
    return render(request, 'user/unconfirmed.html')


@login_required(login_url='login')
@check_confirmed
def profile(request, username):

    user = User.objects.filter(username=username).first()
    return render(request, 'user/profile.html',{'user': user})

@login_required(login_url='login')
@check_confirmed
def account(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', user.username)

    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'user/account.html', {'form':form})

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
