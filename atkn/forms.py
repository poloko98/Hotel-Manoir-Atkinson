from django import forms
from .models import Reserva,Image

class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ('email', 'nombre','comentario','telefono','fecha_inicio','fecha_fin','num_personas',)

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["nombre", "foto"]