from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .auths import index,login,register,logout,unconfirmed,email_resend,email_activation,user_profile,account_setting,user_task
# from . import views


urlpatterns = [
    path('', index.index, name='index'),
    path('login/', login.login_user, name='login'),
    path('register/', register.register, name='register'),
    path('logout/', logout.signout, name='logout'),
    path('unconfirmed/', unconfirmed.unconfirmed, name='unconfirmed'),
    path('email_resend/', email_resend.resend, name='resend'),
    path('activate/<uidb64>/<token>', email_activation.activate, name='activate'),
    path('profile/<username>', user_profile.profile, name='profile'),
    path('account/', account_setting.account, name='account'),
    path('todo/<username>', user_task.user_task, name='user_task'),


    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name='password_reset_complete'
    ),

]








# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/', views.login_user, name='login'),
#     path('register/', views.register, name='register'),
#     path('logout/', views.signout, name='logout'),
#     path('unconfirmed/', views.unconfirmed, name='unconfirmed'),
#     path('email_resend/', views.resend, name='resend'),
#     path('account/', views.account, name='account'),
#     path('profile/<username>', views.profile, name='profile'),
#     path('todo/<username>', views.user_task, name='user_task'),
#
#
#     path('activate/<uidb64>/<token>', views.activate, name='activate'),
#     path(
#         'password-reset/',
#         auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
#         name='password_reset'
#     ),
#     path(
#         'password-reset/done/',
#         auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
#         name='password_reset_done'
#     ),
#     path(
#         'password-reset-confirm/<uidb64>/<token>',
#         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
#         name='password_reset_confirm'
#     ),
#     path(
#         'password-reset-complete/',
#         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
#         name='password_reset_complete'
#     ),
#
# ]
