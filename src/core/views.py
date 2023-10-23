from django.shortcuts import render
from django.views import View
from product.models import Product, Category, ProductReview
from core.forms import ProductReviewForm
from django.db.models import Avg
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(product_status="published", featured=True)
        category = Category.objects.all()
        context = {
            "products": products,
            "categories": category,
        }
        return render(request, 'shopeepage/index.html', context)


def view_product_detail(request, id):
    product = Product.objects.get(id=id)
    p_image = product.p_images.all()
    category = Category.objects.all()
    product_ralated = Product.objects.filter(category=product.category).exclude(id=id)[:4] #get all products of category exclude id get and get limited 4
    review = ProductReview.objects.filter(product=product)
    # product review forms
    review_form = ProductReviewForm()
    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()
        if user_review_count > 0:
            make_review = False

            
    context = {
        'productDetail': product,
        'p_image': p_image,
        'categories': category,
        'product_ralated': product_ralated,
        'review': review,
        'review_form': review_form,
        'make_review': make_review
        }

    return render(request, 'shopeepage/product_detail.html', context)

def view_shop_list(request):
    category = Category.objects.all()
    products = Product.objects.filter(product_status="published", featured=True)
    product_all = Product.objects.all()
    saleOff = Product.objects.filter(is_sale=True)
    context = {
            "products": products,
            "categories": category,
            "sale": saleOff,
            "product_all": product_all
        }
    return render(request, 'shopeepage/shop_list.html', context)


def ajax_add_review(request, id):
    product = Product.objects.get(id=id)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )
    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating']
    }
    average_review = ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))

    return JsonResponse(
        {'bool': True,
        'context': context,
        'avg_review': average_review}
    )


def search_view(request):
    query = request.GET.get("q")

    products = Product.objects.filter(title__icontains = query).order_by("-date")
    category = Category.objects.all()

    context = {
        "products": products,
        "query": query,
        "category": category
    }
    return render(request, 'shopeepage/search.html', context)


def filter_product(request):
    categories = request.GET.getlist("category[]")
    products =   Product.objects.filter(product_status="published").order_by("-id").distinct()

    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()
    
    context ={
        "products": products
    }
    data = render_to_string("shopeepage/async/product_detail.html", context)
    return JsonResponse({"data": data})