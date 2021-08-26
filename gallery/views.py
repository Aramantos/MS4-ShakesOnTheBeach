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


@login_required
def edit_image(request, image_id):
    """ Edit an image in the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized personel can do that.')
        return redirect(reverse('home'))

    image = get_object_or_404(GalleryImages, pk=image_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the image!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to update image. Please ensure the form is valid.')
    else:
        form = ImageForm(instance=image)
        messages.info(request, f'You are editing the image for order number {image.order_number}')

    template = 'gallery/edit_image.html'
    context = {
        'form': form,
        'image': image,
    }

    return render(request, template, context)


@login_required
def delete_image(request, image_id):
    """ Delete an image from the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized personel can do that.')
        return redirect(reverse('home'))

    image = get_object_or_404(GalleryImages, pk=image_id)
    image.delete()
    messages.success(request, 'Image deleted!')
    return redirect(reverse('gallery'))
