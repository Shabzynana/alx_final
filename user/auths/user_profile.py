from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from user.models import User
from user.token import check_confirmed



@login_required(login_url='login')
@check_confirmed
def profile(request, username):

    user = User.objects.filter(username=username).first()
    return render(request, 'user/profile.html', {'user': user})
