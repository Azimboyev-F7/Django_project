from django.shortcuts import render
from .models import New, Worker


# Create your views here.

def index(request):
    new = New.objects.all()
    context = {
        "new": new,
    }
    return render(request, "index.html", context)


def blog(request):
    new = New.objects.all()
    context = {
        "new": new,
    }
    return render(request, "blogs.html", context)


def detail(request,pk):
    new = New.objects.get(id=pk)
    context = {
        "object": new,

    }

    return render(request, "detail.html", context)