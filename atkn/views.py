from django.shortcuts import render
from .models import Reserva
from .forms import ReservaForm

def index(request):
    reservas = Reserva.objects.all()
    return render(request, 'atkn/index.html', {'reservas':reservas})





def contacto(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            Reserva = form.save(commit=False)
            Reserva.save()
    else:
        form= ReservaForm()
    return render(request, 'atkn/contacto.html', {'form': form})