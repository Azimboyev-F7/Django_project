from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, logout, authenticate

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("/")
        raise ObjectDoesNotExist("username or password is incorrect")
    context = {}

    return render(request, 'auth/login.html', context)