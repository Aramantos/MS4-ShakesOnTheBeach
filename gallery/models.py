from django.db import models


class GalleryImages(models.Model):

    class Meta:
        verbose_name_plural = 'Gallery Images'

    image = models.ImageField(null=True, blank=True)
    order_number = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.order_number
