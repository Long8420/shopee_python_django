from django.urls import path
# from .views import getAllProducts, apiCategory
from . import views

urlpatterns = [
    path("", views.IndexClass.as_view(), name="index"),

]