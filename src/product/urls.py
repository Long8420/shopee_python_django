from django.urls import path
from .views import getAllProducts, apiCategory


app_name = 'products'


urlpatterns = [
    # Api
    path("api", getAllProducts.as_view(), name="get_all_products"),
    path("api/<int:pk>", getAllProducts.as_view(), name="update_products_byId"),
    path("api/category/", apiCategory.as_view(), name="api_categories"),
    path("api/category/<int:pk>", apiCategory.as_view(), name="api_categories_byId"),

    # View
]
