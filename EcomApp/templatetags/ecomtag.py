from django import template

from EcomApp.models import Setting
from Product.models import Product, Images, Category

register = template.Library()

@register.simple_tag
def ecom_cat():
    return Category.objects.all()
    
@register.simple_tag
def ecom_set():
    return Setting.objects.get(id=1)