from django.shortcuts import render
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
    return render(request, "article/create.html")