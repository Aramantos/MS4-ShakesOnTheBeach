from django import forms
from .models import GalleryImages


class ImageForm(forms.ModelForm):

    class Meta:
        model = GalleryImages
        fields = '__all__'
