from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from user.models import User



@login_required(login_url='login')
def unconfirmed(request):

    user = request.user.id
    print(user)
    current_user = User.objects.get(id=user)
    print (current_user.username)

    if current_user.confirmed:
        return redirect('index')
    return render(request, 'user/unconfirmed.html')
