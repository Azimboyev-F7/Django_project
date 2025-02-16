from django.urls import path
from .views import index, blog, detail

app_name = 'main'


urlpatterns = [
    path("", index, name="index"),
    path("blogs/", blog, name="blogs"),
    path("blogs/<int:pk>", detail, name="detail"),
]