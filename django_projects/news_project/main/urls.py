from django.urls import path
from .views import index, blog

app_name = 'main'


urlpatterns = [
    path("", index, name="index"),
    path("blogs/", blog, name="blogs"),
]