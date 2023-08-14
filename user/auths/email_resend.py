from django.shortcuts import render, redirect

from user.models import User
from user.email import resend_mail



def resend(request):

    user = request.user.id
    get_user = User.objects.get(id=user)
    resend_email(request, user, get_user)
    return redirect('unconfirmed')
