from django.contrib import admin
from .models import Recipe, Ingredient, Tag

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_display_links = ('title', 'author')
    list_max_show_all = 100
    list_per_page = 5
    search_fields = ('id', 'title', 'author')
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Recipe, RecipeAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'recipe', 'recipe__author','is_active')
    list_display_links = ('title','recipe')
    list_max_show_all = 100
    list_per_page = 5
    search_fields = ('id', 'title', 'recipe')
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at')




admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(Tag)