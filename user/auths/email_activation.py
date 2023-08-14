from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages

from user.models import User
from user.token import verify_token

import datetime




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

        messages.success(request, f"Thank you {user.username} for your email confirmation.")
        return redirect('index')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('index')
