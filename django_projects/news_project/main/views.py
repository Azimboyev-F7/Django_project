# from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import New, Login
from .forms import NewsForm, LoginForm
from django.contrib import messages


# Create your views here.

def index(request):
    new = New.objects.all()
    context = {
        "new": new,
    }
    return render(request, "article/index.html", context)


def blog(request):
    login = Login.objects.first()
    new = New.objects.all()
    query = request.GET.get('q')

    if query:
        # new = New.objects.filter(title__icontains=query)
        # new = New.objects.filter(title__exact=query)
        new = New.objects.filter(title__contains=query)

    context = {
        'login': login,
        "new": new,
    }
    return render(request, "article/blogs.html", context)


def detail(request,pk):
    new = New.objects.get(id=pk)
    context = {
        "object": new,

    }

    return render(request, "article/detail.html", context)

# def createe(request):
#
#     if request.method == "POST":
#         New.objects.create(title=request.POST['title'], content=request.POST['content'])
#         return HttpResponse(content="Article created successfully <a href='../'>Go home</a>")
#
#     context = {
#         "object_list" : New.objects.all()
#     }
#     return render(request, "article/create.html", context)

def create(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully created")
            return redirect('main:blogs')
    context = {
        "object_list" : New.objects.all(),
        'form': form
    }
    return render(request, "article/create.html", context)


def delete(request,pk):
    new = New.objects.get(id=pk)

    if request.method == "POST":
        new.delete()
        messages.error(request, "Article successfully deleted")
        return redirect('main:blogs')

    context = {
        "object": new,
    }

    return render(request, "article/delete.html", context)

def update(request,pk):
    objects = get_object_or_404(New,id=pk)
    form = NewsForm(instance=objects)
    if request.method == "POST":
        form = NewsForm(request.POST, files=request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully updated")
            return redirect('main:blogs')

    context = {
        "object": objects,
        "form": form
    }
    return render(request, "article/update.html", context)



def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Login successfully")
            return redirect('main:blogs')

    context = {
        'login_form': Login.objects.all(),
        "form": form
    }
    return render(request, "article/login.html", context)


def logout_view(request):
    user = Login.objects.first()

    if request.method == "POST":
        user.delete()
        messages.error(request, "Logout successfully")
        return redirect('main:blogs')

    context = {
        "user": user,
    }
    return render(request, "article/logout.html", context)

def navbar(request):
    form = NewsForm()
    logins = Login.objects.first()
    ctx = {
        "form": form,
        "logins": logins,
    }
    return render(request, 'navbar.html', ctx)