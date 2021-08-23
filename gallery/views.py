from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ImageForm
from .models import GalleryImages


def gallery(request):
    """
    A view to return gallery page
    """
    gallery = GalleryImages.objects.all()

    context = {
        'gallery': gallery,
    }

    return render(request, 'gallery/gallery.html', context)


def add_image(request):
    """ Add an image to the gallery """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added your image')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to add your image. Please ensure the form is valid.')
    else:
        form = ImageForm()

    template = 'gallery/add_image.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
