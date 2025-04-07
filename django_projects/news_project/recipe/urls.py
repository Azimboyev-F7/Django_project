from django.urls import path
from .views import recipe_list, recipe_detail, recipe_create

app_name = "recipe" 


urlpatterns = [
    path("list/", recipe_list, name="list"),
    path("<slug:slug>", recipe_detail, name='detail'),
    path("create-form/", recipe_create, name="recipe_create"),
]