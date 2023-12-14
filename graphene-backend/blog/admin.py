from django.contrib import admin

# Register your models here.
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import BlogPage

class BlogPageAdmin(ModelAdmin):
    model = BlogPage
    title = 'Articles'
    menu_label = 'Articles'
    menu_icon = 'Blog-line'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'url_path')

modeladmin_register(BlogPageAdmin)