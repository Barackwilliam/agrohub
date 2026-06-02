from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def products_list(request):
    categories = ProductCategory.objects.filter(is_active=True).prefetch_related('products')
    featured = Product.objects.filter(is_featured=True, is_active=True)[:6]
    return render(request, 'products/list.html', {
        'categories': categories,
        'featured': featured,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(category=product.category, is_active=True).exclude(pk=product.pk)[:4]
    return render(request, 'products/detail.html', {
        'product': product,
        'related': related,
    })
