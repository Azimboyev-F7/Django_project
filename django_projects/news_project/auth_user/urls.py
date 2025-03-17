from django.urls import path
from .views import login_views, logout_view, register_view, notifications

app_name = "auth_user"

urlpatterns = [
    path("login/", login_views, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("notifications/", notifications, name="notifications"),
]


