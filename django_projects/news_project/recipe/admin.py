from django.contrib import admin
from django.utils.html import format_html
from .models import Recipe, Ingredient, Tag

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('image_tag' ,'id','title', 'author', 'created_at', 'updated_at')
    list_display_links = ('title', 'author')
    list_max_show_all = 100
    list_per_page = 5
    search_fields = ('id', 'title', 'author__username')
    auto_complete_fields = ('author',)
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at', 'slug')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="border-radius:5px;"/>'.format(obj.image.url))
        return "No Image"

    image_tag.short_description = 'Image'

admin.site.register(Recipe, RecipeAdmin)



class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'recipe', 'recipe__author','is_active')
    list_display_links = ('title','recipe')
    list_max_show_all = 100
    list_per_page = 10
    search_fields = ('title', 'recipe__title', 'recipe__author__username')
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at')




admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(Tag)