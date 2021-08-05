from django.shortcuts import render, get_object_or_404

from .models import Product


def menu(request):
    """ A view to return the menu page """

    menu = Product.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu.html', context)


def menu_product_detail(request, product_id):
    """ A view to show individual menu products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'menu/menu_product_detail.html', context)
