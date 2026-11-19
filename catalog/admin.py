from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'created_at', 'updated_at']
    list_filter = ['price', 'is_active']
    search_fields = ['category', 'title', 'description', 'price']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


