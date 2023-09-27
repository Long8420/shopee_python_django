
from django.contrib import admin
from django.urls import path,include
from .views import getAllProducts

urlpatterns = [
    path("", getAllProducts.as_view(), name="get_all_products"),
    path("<int:pk>", getAllProducts.as_view(), name="update_products_byId"),
]
