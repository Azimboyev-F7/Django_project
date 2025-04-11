from django.urls import path
from .views import recipe_list, recipe_detail, recipe_create, recipe_update, recipe_delete, my_recipe, ingredient_create

app_name = "recipe" 


urlpatterns = [
    path("list/", recipe_list, name="list"),
    path("detail/<slug:slug>", recipe_detail, name='detail'),
    path("create-form/", recipe_create, name="recipe_create"),
    path("update/<slug:slug>", recipe_update, name="recipe_update"),
    path("delete/<slug:slug>", recipe_delete, name="recipe_delete"),
    path("my-recipe/", my_recipe, name="my_recipe"),
    path("ingredient-create/<slug:slug>", ingredient_create, name="ingredient_create"),
]