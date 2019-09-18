from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def cadastrar_usuario(request):
    return render(request, "app/form.html", {})