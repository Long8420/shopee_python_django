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
    order_date = models.DateField(auto_now_add=True)
    product_status = models.BooleanField(choices= STATUS_CHOICES, max_length=50, default="process")

    class Meta:
        verbose_name = "Cart"

    def __str__(self):
        return self.title

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quanlity = models.IntegerField(default=0)
    invoices_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    price =  models.DecimalField(max_digits=9, decimal_places=3, default="1000")
    image = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Cart"

    
    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50"/> ' % ( self.image.url))