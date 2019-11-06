from django.shortcuts import render

def index(request):
    return render(request, 'atkn/index.html', {})

def contacto(request):
    return render(request, 'atkn/contacto.html', {})

def habitaciones(request):
    return render(request, 'atkn/habitaciones.html', {})

def Nosotros(request):
    return render(request, 'atkn/Nosotros.html', {})

