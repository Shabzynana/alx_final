from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages



def signout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")
