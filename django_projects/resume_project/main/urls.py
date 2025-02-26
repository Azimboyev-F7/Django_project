from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('index/', index, name='index'),
    path('', index2, name='index-2'),
]

