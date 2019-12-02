from django.shortcuts import render
from .models import Reserva
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return render(request, 'atkn/index.html', )
    

@login_required
def menu_adm(request):
    user = request.user
    if user.has_perm('atkn.recepcionista'):
        reservas= Reserva.objects.all()
        context = {'reservas': reservas}
        return render(request, 'atkn/menu_adm.html',context )
    else :
        return render(request, 'atkn/index.html', )

def nosotros(request):
    return render(request, 'atkn/Nosotros.html')

def habitaciones(request):
    return render(request, 'atkn/habitaciones.html')

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