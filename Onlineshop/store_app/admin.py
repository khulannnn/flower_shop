from django.contrib import admin
from .models import Category, Product, Subcategory
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product, ProductAdmin)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('subcategory_name',)}
admin.site.register(Subcategory, SubcategoryAdmin)

