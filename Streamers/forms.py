from django import forms
from . import models

class StreamersForm(forms.ModelForm):
    class Meta:
        model= models.Streamers
        fields=["nombre","apellido","email"]