from django.shortcuts import render
from django.views import View
from product.models import Product, Category
from django.db.models import Count
# Create your views here.

class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(product_status="published")
        category = Category.objects.all()
        context = {
            "products": products,
            "categories": category,
        }
        return render(request, 'homepage/index.html', context)


def view_product_detail(request, id):
    product = Product.objects.get(id=id)
    p_image = product.p_images.all()

    context = {'productDetail': product,
        'p_image': p_image}

    return render(request, 'homepage/detail.html', context)
