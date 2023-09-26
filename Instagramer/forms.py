from django import forms
from . import models

class InstagramerForm(forms.ModelForm):
    class Meta:
        model= models.Instagramer
        fields=["nombre","apellido","email"]