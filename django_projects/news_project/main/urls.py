from django.urls import path
from .views import index, blog, detail, create, create_form, delete, update

app_name = 'main'


urlpatterns = [
    path("", index, name="index"),
    path("article/", blog, name="blogs"),
    path("article/<int:pk>", detail, name="detail"),
    path("create/", create, name="create"),
    path("create-form/", create_form, name="create_form"),
    path("article/delete/<int:pk>", delete, name="delete"),
    path("article/update/<int:pk>", update, name="update"),
]