from django.contrib import admin
from cart.models import CartItem, Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_editable = ['paid_status','product_status']
    list_display = ["user", "price", "paid_status", "order_date", "product_status"]
class CartOrderProductAdmin(admin.ModelAdmin):
    list_display = ["cart", "item", "quanlity", "price", "product_status","cart_img","invoices_no"]

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartOrderProductAdmin)