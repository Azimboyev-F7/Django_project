from django.contrib import admin
from .models import Recipe, Ingredient, Tag

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'title')
    search_fields = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('recipe', 'name')
    search_fields = ('id', 'recipe', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_filter = ('title', )
    search_fields = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at')