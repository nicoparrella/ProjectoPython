from django.shortcuts import redirect, render

from . import models
from . import forms

# Create your views here.

def index(request):
    Instagramer= models.Instagramer.objects.all()
    contexto = {"Instagramer":Instagramer}
    return render(request, "Instagramer/index.html",contexto)

def crear(request):
    if request.method == "POST":
        form = forms.InstagramerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Instagramer:index")
    else :
        form= forms.InstagramerForm
        return render(request, "Instagramer/crear.html", {"form":form})