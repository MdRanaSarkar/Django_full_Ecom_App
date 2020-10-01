from django.urls import path
from OrderApp.views import Add_to_Shoping_cart,cart_detials,cart_delete
urlpatterns = [
path('addingcart/<int:id>/', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
path('cart_details/',cart_detials,name='cart_detials'),
path('cart_delete/<int:id>/', cart_delete, name='cart_delete'),


]