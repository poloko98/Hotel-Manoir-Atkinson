from django.shortcuts import render
from .models import Reserva
from .forms import ReservaForm

def index(request):
    user = request.user
    if user.has_perm('atkn.recepcionista'):
        reservas= Reserva.objects.all()
        context = {'reservas': reservas}
        return render(request, 'atkn/lista_reservas.html',context )
    elif user.has_perm('atkn.administrador'):
        return render(request, 'atkn/index.html', )
    else :
        return render(request, 'atkn/index.html', )





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