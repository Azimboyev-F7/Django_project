from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import auth
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import MyUserCreationForm, MyAuthenticationForm

# def _login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "You are now logged in")
#             return redirect("/")
#         raise ObjectDoesNotExist("username or password is incorrect")
#     context = {}
#
#     return render(request, 'auth/login.html', context)

def login_views(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("main:blogs")
    form = MyAuthenticationForm()
    if request.method == "POST":
        form = MyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"User now logged in")
            return redirect('/')
    context = {
        'form': form,
    }

    return render(request, 'auth/login.html', context)



def logout_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Before logging out need log in")
        return redirect("auth_user:login")
    if request.method == "POST":
        logout(request)
        messages.success(request, "You are now logged out")
        return redirect("/")
    context = {}
    return render(request, 'auth/logout.html', context)

def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("main:blogs")
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are now registered")
            return redirect("auth_user:login")

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)

def notifications(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'notifications.html', context)