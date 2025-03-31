from django.contrib import admin
from .models import Recipe, Ingredient, Tag

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_at')
    list_display_links = ('title',)
    list_max_show_all = 100
    list_per_page = 5
    search_fields = ('id', 'title')
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Ingredient)
admin.site.register(Tag)