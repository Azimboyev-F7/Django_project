from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404

from auth_user.forms import MyUserCreationForm
from .models import New, Login
from .forms import NewsForm, LoginForm, MyUserCreationForm
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

    next_page = request.GET.get('next')
    print(next_page)
    if next_page == '/create-form/' or next_page == '/create/':
        messages.warning(request, "You are not superuser")
        return redirect("main:blogs")
    
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


def detail(request,slug):
    new = New.objects.get(slug=slug)
    context = {
        "object": new,
    }

    return render(request, "article/detail.html", context)


@login_required(login_url='auth_user:login')
@permission_required(perm='request.user.is_superuser', login_url='main:blogs')
def create(request):
    # if not request.user.is_superuser:
    #     messages.error(request, "You must be logged in as admin to create an article")
    #     return redirect("main:blogs")
    if request.method == "POST":
        New.objects.create(title=request.POST['title'], content=request.POST['content'])
        return HttpResponse(content="Article created successfully <a href='../'>Go home</a>")

    context = {
        "object_list" : New.objects.all()
    }
    return render(request, "article/create.html", context)


@login_required(login_url='auth_user:login')
@permission_required(perm='request.user.is_superuser', login_url='main:blogs')
def create_form(request):
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
    return render(request, "article/create-form.html", context)


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


def navbar(request):
    form = NewsForm()
    logins = Login.objects.first()
    print(logins)
    ctx = {
        "form": form,
        "logins": logins,
    }
    return render(request, 'navbar.html', ctx)
