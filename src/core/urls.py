
from django.urls import path
from .views import HomeView, view_product_detail

app_name = "core"
urlpatterns = [
    path("", HomeView.as_view(), name='index'),
    path("product/<id>/", view_product_detail, name='view_product'),
]
