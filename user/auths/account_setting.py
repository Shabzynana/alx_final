from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from user.forms import UserUpdateForm
from user.token import check_confirmed





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
