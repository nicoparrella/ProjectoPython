from django.shortcuts import redirect, render

from . import models
from . import forms

# Create your views here.

def index(request):
    Tiktoker= models.Tiktoker.objects.all()
    contexto = {"Tiktoker":Tiktoker}
    return render(request, "Tiktoker/index.html",contexto)

def crear(request):
    if request.method == "POST":
        form = forms.TiktokerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Tiktoker:index")
    else :
        form= forms.TiktokerForm
        return render(request, "Tiktoker/crear.html", {"form":form})