from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import render, redirect
import six
from functools import wraps


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.id) + six.text_type(timestamp)  + six.text_type(user.is_active)
        )

verify_token = AccountActivationTokenGenerator()



class AccountActivationTokenGeneratorr(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.id) + six.text_type(timestamp)  + six.text_type(user.is_active)
        )

verifyy_token = AccountActivationTokenGeneratorr()


def check_confirmed(func):
    @wraps(func)
    def decorated_function(request, *args, **kwargs):
        current_user = request.user
        if current_user.confirmed is False:
            return redirect('unconfirmed')
        return func(*args, **kwargs)

    return decorated_function
