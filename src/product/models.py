from django.db import models
# from django.utils.html import mark_safe
from django.utils.html import mark_safe
from django.utils.html import format_html
# Create your models here.
from userauths.models import User

STATUS_CHOICES = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivery"),
)

STATUS = (
    ("darft", "Darft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In-Review"),
    ("published", "Published"),
)

RATING = (
    (1, "⭐"),
    (2, "⭐⭐"),
    (3, "⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (5, "⭐⭐⭐⭐⭐"), 
)


def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Category(models.Model):
    title = models.CharField(default='', max_length=100)
    slug = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review",)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=3, default="1000")
    old_price =models.DecimalField(max_digits=9, decimal_places=3, default="1000")
    class Meta:
        verbose_name = "Product"

    def __str__(self):
        return self.title
    
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/> ' % ( self.image.url))

    def get_precentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price


class ProductImage(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Products Image"
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
  
    def __str__(self):
        return self.title

class Vendor(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    chat_resp_time = models.CharField(max_length=200)
    shipping_on_time = models.CharField(max_length=200)
    authentic_rating = models.CharField(max_length=200)
    days_return = models.CharField(max_length=200)
    warranty_period = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Vendor"

    def __str__(self):
        return self.title
    
    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/> ' % ( self.image.url))


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Product Reviews"

    def __str__(self):
        return self.product.title
    def get_rating (self):
        return self.rating

class wishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "wishlists"

    def __str__(self):
        return self.product.title

# ---------------- Addresses ----------------

class Addresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    address = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Address"
