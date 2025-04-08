from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Recipe, Ingredient, Tag
from django.contrib.auth.models import User, AbstractBaseUser, Permission
from .forms import RecipeForm
# Create your views here.


def recipe_list(request):
    recipes = Recipe.objects.all()
    query = request.GET.get('q')
    if query:
        recipes = recipes.filter(author__username__icontains=query)
    context = {
        'recipes': recipes,
    }

    return render(request, 'recipe/index.html', context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients = Ingredient.objects.filter(recipe__author=recipe.author.id)
    is_author = request.user == recipe.author
    print(is_author)
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipe/detail.html', context)


def recipe_create(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author.id = request.user.id
            recipe.save()
            form.save_m2m()
            reverse_url = reverse('recipe:list')
            return redirect(reverse_url)
    content = {
        'form': form
    }
    return render(request, 'recipe/create_form.html', content)