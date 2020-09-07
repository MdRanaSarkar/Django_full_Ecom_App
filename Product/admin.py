from django.contrib import admin

# Register your models here.
from .models import Category, Product, Images


admin.site.register(Category)


admin.site.register(Images)


class productImageInline(admin.TabularInline):
    model = Images
    extra = 5


admin.site.register(Product)
