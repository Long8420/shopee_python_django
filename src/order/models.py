from django.db import models
from cart.models import Cart
# from django.contrib.auth.models import User
from userauths.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255,default='')
    order_description = models.TextField(default='')
    is_complete = models.BooleanField(default="False")
