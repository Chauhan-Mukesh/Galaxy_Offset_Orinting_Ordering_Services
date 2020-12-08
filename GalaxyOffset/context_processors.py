from .models import Product


def extras(request):
    categories = Product.objects.all()
    return {'categories': categories}
