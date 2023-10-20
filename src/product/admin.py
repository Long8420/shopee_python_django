from django.contrib import admin

from product.models import Product,Variation,Category,wishList,ProductReview,ProductImage,Addresses,Vendor



class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ["title", "product_image", "category",  "description", "price", "product_status","featured","is_sale"]

class VendorAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image", "address", "contact","chat_resp_time","days_return"]
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating", "date"]
class wishListAdmin(admin.ModelAdmin):
    list_display = ["user", "product","date"]
class AddressesAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "status"]
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description","cate_image" ,"slug", "active", ]
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Addresses, AddressesAdmin)
admin.site.register(wishList, wishListAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Vendor, VendorAdmin)

admin.site.register(Variation)