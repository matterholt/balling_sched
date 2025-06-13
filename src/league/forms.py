from django import forms
from django.db.models import fields_all

from .models import Schedule

class EventForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = (
            'start_time','end_time','game_type','field_location'
        )
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ScheduleCSVUploadForm(forms.Form):
    csv_file = forms.FileField()
