from django.contrib import admin
from .models import New, Worker


# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title',)
    list_max_show_all = 100
    list_per_page = 5
    search_fields = ('id', 'title')
    date_hierarchy = 'created_at'
    ordering = ('-id', )
    readonly_fields = ('created_at', 'updated_at')



admin.site.register(New, NewAdmin)

admin.site.register(Worker)
