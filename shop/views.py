from django.shortcuts import render
from django.utils.translation import gettext as _

from .models import Product


def shop_index(request):
    products = Product.objects.all()

    context = {
        'page_title': _('Shop'),
        'products': products
    }

    return render(request, 'shop/index.html', context=context)
