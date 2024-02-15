from django.contrib import admin
from .models import MenuCategory, MenuItem


@admin.register(MenuCategory)
class TreeMenuCategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['__str__']


@admin.register(MenuItem)
class TreeMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'path', 'parent']
    list_display = ['__str__', 'category', 'path', 'parent']
