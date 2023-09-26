from django.shortcuts import redirect, render

from . import models
from . import forms

# Create your views here.

def index(request):
    Streamers= models.Streamers.objects.all()
    contexto = {"Streamers":Streamers}
    return render(request, "Streamers/index.html",contexto)

def crear(request):
    if request.method == "POST":
        form = forms.StreamersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Streamers:index")
    else :
        form= forms.StreamersForm
        return render(request, "Streamers/crear.html", {"form":form})