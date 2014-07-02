# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from models import *


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1



class CategoryAdmin(MPTTModelAdmin):
    tree_title_field = 'name'
    tree_display = ('name',)
    #mptt_level_indent = 15    #растояние смещения
    list_display = ['name']     #, 'get_ancestors'
    search_fields = ['name',]

    #inlines = [ProductInline]

        



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', ]
    search_fields = ['name', 'description']
    pass



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)