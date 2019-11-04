from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

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