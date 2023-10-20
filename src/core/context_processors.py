from product.models import Product, Category, ProductReview
from django.db.models import Min, Max
def default(request):
    categories = Category.objects.all()
    min_max_price = Product.objects.aggregate(Min("price"),Max("price"))
    context = {
        "categ": categories,
        "min_max_price": min_max_price
    }
    return (context)