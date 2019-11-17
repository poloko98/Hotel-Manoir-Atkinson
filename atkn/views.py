from django.shortcuts import render
from .models import Reserva
from .forms import ReservaForm

def index(request):
    reservas = Reserva.objects.all()
    return render(request, 'atkn/index.html', {'reservas':reservas})


def contacto(request):
    return render(request, 'atkn/contacto.html', {})

def habitaciones(request):
    return render(request, 'atkn/habitaciones.html', {})

def Nosotros(request):
    return render(request, 'atkn/Nosotros.html', {})

def contacto(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            Reserva = form.save(commit=False)
            Reserva.save()
    else:
        form= ReservaForm()
    return render(request, 'atkn/contacto.html', {'form': form})


def lista_reserva(request):
    reservas= Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'atkn/lista_reservas.html',context)