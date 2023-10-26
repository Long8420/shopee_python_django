from django.db import models

from product.models import Variation
# from CustomUser.models import CustomeUser
from userauths.models import User
from django.utils.html import mark_safe

# Create your models here.
STATUS_CHOICES = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivery"),
)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #
    updated_at = models.DateTimeField(auto_now=True) #update lan cuoi cung
    price =  models.DecimalField(max_digits=9, decimal_places=3, default="1000")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True, null=True)
    product_status = models.CharField(choices= STATUS_CHOICES, max_length=50, default="process")

    class Meta:
        verbose_name = "Cart"

    # def __str__(self):
    #     return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    quanlity = models.IntegerField(default=0)
    invoices_no = models.CharField(max_length=200, null=True)
    product_status = models.CharField(choices= STATUS_CHOICES, max_length=50, default="process")
    price =  models.DecimalField(max_digits=9, decimal_places=3, default="1000")
    image =  models.CharField(max_length=200)
    total = models.DecimalField(max_digits=9, decimal_places=3, default="100")
    class Meta:
        verbose_name = "CartOrderProduct"

    
    def cart_img(self):
        return mark_safe('<img src="%s" width="50" height="50"/> ' % ( self.image))