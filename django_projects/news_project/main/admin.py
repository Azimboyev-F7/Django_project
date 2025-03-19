from django.contrib import admin
from .models import New, Login


# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at')
    list_display_links = ('title',)
    list_max_show_all = 100
    list_per_page = 5
    search_fields = ('id', 'title')
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(New, NewAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'id')
    list_display_links = ('first_name',)
    list_max_show_all = 100
    list_per_page = 2

admin.site.register(Login)
