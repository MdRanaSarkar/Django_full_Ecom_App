from django.urls import path
from .views import Home, product_single, category_product, About, contact, SearchView


urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', contact, name='contact_dat'),
    path('product/<int:id>/', product_single, name='product_single'),
    path('product/<int:id>/<slug:slug>/', category_product, name='category_product'),
    path('search/', SearchView, name='SearchView'),



]
