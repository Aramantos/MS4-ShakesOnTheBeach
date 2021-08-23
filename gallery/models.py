from django.db import models


class GalleryImages(models.Model):

    class Meta:
        verbose_name_plural = 'Gallery Images'

    image = models.ImageField(null=False, blank=False)
    order_number = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.order_number
