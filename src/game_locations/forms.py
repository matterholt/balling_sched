from django import forms
from .models import Venue


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['short_name', 'name', 'address', 'city', 'state', 'zip_code']


class UploadVenueForm(forms.Form):
    file = forms.FileField()
