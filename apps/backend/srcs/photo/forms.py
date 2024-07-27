from django import forms

from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = (
            "title",
            "author",
            "src",
            "description",
            "price",
        )
