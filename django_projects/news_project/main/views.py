from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import New, Worker


# Create your views here.

def index(request):
    new = New.objects.all()
    context = {
        "new": new,
    }
    return render(request, "article/index.html", context)


def blog(request):
    new = New.objects.all()
    query = request.GET.get('q')

    if query:
        # new = New.objects.filter(title__icontains=query)
        # new = New.objects.filter(title__exact=query)
        new = New.objects.filter(title__contains=query)

    context = {
        "new": new,
    }
    return render(request, "article/blogs.html", context)


def detail(request,pk):
    new = New.objects.get(id=pk)
    context = {
        "object": new,

    }

    return render(request, "article/detail.html", context)

def create(request):

    if request.method == "POST":
        New.objects.create(title=request.POST['title'], content=request.POST['content'])
        return HttpResponse(content="Article created successfully <a href='../'>Go home</a>")

    context = {
        "object_list" : New.objects.all()
    }
    return render(request, "article/create.html", context)


def delete(request,pk):
    new = New.objects.get(id=pk)

    if request.method == "POST":
        new.delete()
        return redirect('main:blogs')

    context = {
        "object": new,
    }

    return render(request, "article/delete.html", context)