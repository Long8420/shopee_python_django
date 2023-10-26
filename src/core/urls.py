
from django.urls import path
from .views import HomeView,view_product_detail,view_shop_list,ajax_add_review,search_view,filter_product,add_to_cart,cart_view,delete_item_from_cart,update_from_cart,checkout_view,order_complete

app_name = "core"
urlpatterns = [
    path("", HomeView.as_view(), name='index'),
    path("product/<id>/", view_product_detail, name='view_productById'),
    path("shop-list", view_shop_list, name='view_shopList'),

    # api add review
    path("ajax-add-review/<id>", ajax_add_review, name='ajax_add_review'),
    # search
    path("search/", search_view, name='search'),
    path("filter-product/", filter_product, name='filter-product'),


    path("add-to-cart/", add_to_cart, name="add-to-cart"),

    # Cart view
    path("cart-list/",  cart_view, name="cart-list"),
    
    # delete cart
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),
    # update cart
    path("update-cart/", update_from_cart, name="update-cart"),
    #  payment
    path("checkout/", checkout_view, name="checkout"),
    path("order-complete/", order_complete, name="order-complete"),



]
