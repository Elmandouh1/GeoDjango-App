from django import forms 
from .models import Measurement 


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement 
        fields = ('destination', )