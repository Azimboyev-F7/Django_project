from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Recipe, Ingredient, Tag
from django.contrib.auth.models import User, AbstractBaseUser, Permission
from .forms import RecipeForm, IngredientCreateForm
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


def my_recipe(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to see your recipe")
        reverse_url = reverse('auth_user:login') + '?next=' + request.path
        return redirect(reverse_url)
    recipes = Recipe.objects.filter(author=request.user)
    print(recipes)
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipe/my_recipe.html', context)
    




def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients = Ingredient.objects.filter(recipe__author=recipe.author.id)
    is_author = request.user == recipe.author
    print(is_author)
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'is_author': is_author
    }
    return render(request, 'recipe/detail.html', context)


def recipe_create(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to create a recipe")
        reverse_url = reverse('auth_user:login') + '?next=' + request.path
        return redirect(reverse_url)
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('recipe:list')
    context = {
        'form': form
    }
    return render(request, 'recipe/create_form.html', context)

def recipe_update(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to update a recipe")
        reverse_url = reverse('auth_user:login') + '?next=' + request.path
        return redirect(reverse_url)
    form = RecipeForm(instance=recipe)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author.id = request.user.id
            recipe.save()
            form.save_m2m()
            reverse_url = reverse('recipe:detail', args=[recipe.slug])
            return redirect(reverse_url)
    context = {
        'form': form
    }
    return render(request, 'recipe/update.html', context)


def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to delete a recipe")
        reverse_url = reverse('auth_user:login') + '?next=' + request.path
        return redirect(reverse_url)
    
    if request.method == "POST":
        recipe.delete()
        messages.error(request, f"'{recipe.title}' successfully deleted")
        return redirect('recipe:list')

    context = {
        'object': recipe
    }

    return render(request, 'recipe/delete_recipe.html', context)



def ingredient_create(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to create an ingredient")
        reverse_url = reverse('auth_user:login') + '?next=' + request.path
        return redirect(reverse_url)
    recipe = get_object_or_404(Recipe, slug=request.slug)
    form = IngredientCreateForm()
    if request.method == "POST":
        form = IngredientCreateForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False) 
            ingredient.recipe = recipe
            ingredient.save()
            messages.success(request, "Ingredient successfully created")
            reverse_url = reverse('recipe:detail', args=[recipe.slug])
            return redirect(reverse_url)
        
    context = {
        'form': form
    }
    return render(request, 'recipe/ingredient_create.html', context)
