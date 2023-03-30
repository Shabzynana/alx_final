from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils.html import strip_tags



from .token import verify_token, verifyy_token
from .models import User


def make_email(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('user/activate.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': verify_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
#     plain = strip_tags(message)
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = 'html'

    if email.send():
        messages.success(request, f'Dear {user.username}, please go to you email {to_email} inbox and click on \
            received activation link to confirm and complete the registration.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

def make_emaill(request, user, to_email):
    user_id = request.user.id
    get_user = User.objects.get(id=user_id)
    mail_subject = 'Activate your user account.'
    message = render_to_string('user/activate2.html', {
        'user': get_user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(get_user.id)),
        'token': verifyy_token.make_token(get_user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
#     plain = strip_tags(message)
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = 'html'

    if email.send():
        messages.success(request, f'Dear {get_user.username}, please go to you email {to_email} inbox and click on \
            received activation link to confirm and complete the registration.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')
