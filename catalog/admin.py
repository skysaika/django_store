from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'price', 'in_stock')
    list_display_links = ('title',)
    list_editable = ('price',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)






