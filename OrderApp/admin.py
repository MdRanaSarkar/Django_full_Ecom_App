from django.contrib import admin

# Register your models here.
from OrderApp.models import  ShopCart, ShopingCartForm,Order, OderProduct



class ShopCartAdmin(admin.ModelAdmin):
	list_display=['product','user','quantity','price','amount']
	list_filter=['user']






admin.site.register(ShopCart,ShopCartAdmin)




class OrderProductline(admin.TabularInline):
    model = OderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone', 'total', 'status', 'transaction_id']
    list_filter = ['status']
    readonly_fields = ('user', 'first_name', 'last_name',
                       'phone', 'address', 'city', 'country', 'total', 'ip', 'transaction_id', 'image_tag')
    can_delete = False
    inlines = [OrderProductline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register(Order, OrderAdmin)

admin.site.register(OderProduct, OrderProductAdmin)


    



   
   
    


    



