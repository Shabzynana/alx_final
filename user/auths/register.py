from django.shortcuts import render, redirect
from django.contrib import messages

from user.forms import UserRegisterForm
from user.models import User
from user.email import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            get_user = User.objects.get(email=request.POST.get('email'))
            send_mail(request, user, get_user)
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
