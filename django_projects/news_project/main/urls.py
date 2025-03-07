from django.urls import path
from .views import index, blog, detail, create, delete, update, login, logout_view

app_name = 'main'


urlpatterns = [
    path("", index, name="index"),
    path("blogs/", blog, name="blogs"),
    path("blogs/<int:pk>", detail, name="detail"),
    path("create/", create, name="create"),
    path("blogs/delete/<int:pk>", delete, name="delete"),
    path("blogs/update/<int:pk>", update, name="update"),
    path("login/", login, name="login"),
    path("logout/", logout_view, name="logout"),
]