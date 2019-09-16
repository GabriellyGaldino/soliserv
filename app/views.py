from django.shortcuts import render
from .forms import *

# Create your views here.

def cadastrar_usuario(request):
    form = UsuarioForm()
    return render(request, "form.html", {'form':form})