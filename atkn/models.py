from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _



class Reserva(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    telefono = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    num_personas = models.IntegerField()
    def __str__(self):
        return self.fecha_inicio.__str__()+' / '+self.fecha_fin.__str__()+' '+self.nombre

    class Meta:
        permissions = (
            ('administrador',_('Es administrador')),
            ('recepcionista',_('Es recepcionista')),
        )


class Image(models.Model):
    nombre= models.CharField(max_length=500)
    foto= models.ImageField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.nombre + ": " + str(self.foto)
   


