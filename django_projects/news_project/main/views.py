from django.shortcuts import render
from .models import New, Worker


# Create your views here.

def index(request):
    new = New.objects.get(id=1)
    new_1 = New.objects.get(id=2)
    new_2 = Worker.objects.get(id=1)
    context = {
        "new": new,
        "new_1": new_1,
        "new_2": new_2,
    }
    return render(request, "index.html", context)


def blog(request):
    new = New.objects.all()
    context = {
        "new": new,
    }
    return render(request, "blogs.html", context)