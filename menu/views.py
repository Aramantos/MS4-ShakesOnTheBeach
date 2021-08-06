from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category


def menu(request):
    """ A view to return the menu page """

    menu = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            menu = menu.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('menu'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu = menu.filter(queries)

    context = {
        'menu': menu,
        'search_term': query,
    }

    return render(request, 'menu/menu.html', context)


def menu_product_detail(request, product_id):
    """ A view to show individual menu products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'menu/menu_product_detail.html', context)
