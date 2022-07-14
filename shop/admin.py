from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    fields = ['image']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductGalleryInline
    ]
    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    pass