from django.contrib import admin
from .models import GalleryImages


class GalleryImagesAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'order_number',
    )


admin.site.register(GalleryImages, GalleryImagesAdmin)
