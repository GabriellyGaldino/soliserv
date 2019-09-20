from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as log

# Create your views here.

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log(request, user)
            return redirect('dashboard')
    return render(request, "login.html")


def dashboard(request):
    #Setor.objects.order_by('-pub_date')[:5]
    return render(request, "dashboard.html")

def initial(request):
    return render(request,"form.html")

def banheiro(request):
    # if request.method=="POST":
    #     descricao = request.POST.get('descricao')
    #     situacao = request.POST.get('situacao')
    #     form = authenticate(request, descricao=descricao, situacao=situacao)
    #     if form is not None:
    #         return redirect('initial')
    return render(request, 'banheiro.html')

def sala(request):
    return render(request, "sala.html")

def auditorio(request):
    return render(request, "auditorio.html")

def laboratorio(request):
    return render(request, "laboratorio.html")