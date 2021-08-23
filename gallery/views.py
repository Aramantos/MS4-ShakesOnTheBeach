from django.shortcuts import render


def gallery(request):
    """
    A view to return gallery page
    """
    return render(request, 'gallery/gallery.html')
