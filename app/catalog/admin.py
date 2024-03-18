from django.contrib import admin

from app.catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prise', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
