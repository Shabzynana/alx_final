from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.cache import cache
from django.contrib import messages


from user.forms import UserRegisterForm, LoginForm, UserUpdateForm
from user.models import User


import datetime


def login_user(request):
    form = LoginForm()
    if request.method == 'GET':
        cache.set('next', request.GET.get('next', None))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user = User.objects.get(email=email)
                print(user)
                log = authenticate(request,email=email,password=password)
                if log:
                    login(request,log)
                    messages.success(request,'Logged in successfully')

                    next_url = cache.get('next')
                    if next_url == None:
                        return redirect("index")
                    return redirect(next_url)

                elif user is not None or user.password is None:
                    print('Incorrect password')
                    messages.error(request, "Incorrect password")
            except:
                messages.error(request, f"User with email: {email} does not exist")

    return render(request, 'user/login.html',{'form': form})
