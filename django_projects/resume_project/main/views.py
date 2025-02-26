from django.shortcuts import render

# Create your views here.


def index(request):
    ctx = {

    }
    return render(request, 'orbit/index.html', ctx)

def index2(request):
    ctx = {

    }
    return render(request, 'orbit/index-2.html', ctx)
