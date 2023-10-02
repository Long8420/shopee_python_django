from django.db import models

from product.models import Variation
from CustomUser.models import CustomeUser
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #
    updated_at = models.DateTimeField(auto_now=True) #update lan cuoi cung


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quanlity = models.IntegerField(default=0)