
from django.urls import path
from .views import HomeView,view_product_detail,view_shop_list,ajax_add_review,search_view,filter_product

app_name = "core"
urlpatterns = [
    path("", HomeView.as_view(), name='index'),
    path("product/<id>/", view_product_detail, name='view_productById'),
    path("shop-list", view_shop_list, name='view_shopList'),

    # api add review
    path("ajax-add-review/<id>", ajax_add_review, name='ajax_add_review'),
    # search
    path("search/", search_view, name='search'),
    path("filter-product/", filter_product, name='filter-product')
    
]
