from django.shortcuts import render
from products.models import ProductCategory, Product
from siteconfig.models import HeroSlide, WhyChooseUs, CoreValue, Statistic


def home(request):
    hero_slides = HeroSlide.objects.filter(is_active=True)
    categories = ProductCategory.objects.filter(is_active=True)
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    why_items = WhyChooseUs.objects.filter(is_active=True)
    core_values = CoreValue.objects.filter(is_active=True)
    stats = Statistic.objects.filter(is_active=True)
    return render(request, 'core/home.html', {
        'hero_slides': hero_slides,
        'categories': categories,
        'featured_products': featured_products,
        'why_items': why_items,
        'core_values': core_values,
        'stats': stats,
    })


def about(request):
    core_values = CoreValue.objects.filter(is_active=True)
    stats = Statistic.objects.filter(is_active=True)
    return render(request, 'core/about.html', {
        'core_values': core_values,
        'stats': stats,
    })


def contact(request):
    categories = ProductCategory.objects.filter(is_active=True)
    return render(request, 'core/contact.html', {
        'categories': categories,
    })
