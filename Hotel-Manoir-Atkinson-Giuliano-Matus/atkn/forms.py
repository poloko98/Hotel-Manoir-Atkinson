from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ('email', 'nombre','comentario','telefono','fecha_inicio','fecha_fin','num_personas',)