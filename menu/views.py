from django.shortcuts import render

from .models import Product


def menu(request):
    """ A view to return the menu page """

    menu = Product.objects.all()

    context = {
        'menu': menu,
    }

    return render(request, 'menu/menu.html', context)
