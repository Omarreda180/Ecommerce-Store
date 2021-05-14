from django.shortcuts import render, get_object_or_404

from .models import Product, Category
from cart.models import CartItem
from cart.views import _cart_id

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products' : products,
    } 

    return render(request, 'store/index.html', context)

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()
        
    context = {
        'products' : products,
        'products_count' : products_count,
    }
    return render(request, 'store/store/store.html', context)

def product_details(request, category_slug, product_details_slug):
    try:
        single_product = get_object_or_404(Product,category__slug=category_slug, slug=product_details_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        return e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/store/product_details.html', context)
