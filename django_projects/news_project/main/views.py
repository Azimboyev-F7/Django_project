from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import New, Worker
from .forms import NewsForm
from django.contrib import messages


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
    object = get_object_or_404(New,id=pk)
    form = NewsForm(instance=object)
    if request.method == "POST":
        form = NewsForm(request.POST, files=request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, "Article successfully updated")
            return redirect('main:blogs')

    context = {
        "object": object,
        "form": form
    }
    return render(request, "article/update.html", context)
