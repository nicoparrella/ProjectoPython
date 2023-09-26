from django import forms
from . import models

class TiktokerForm(forms.ModelForm):
    class Meta:
        model= models.Tiktoker
        fields=["nombre","apellido","email"]