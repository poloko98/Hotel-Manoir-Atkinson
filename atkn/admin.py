from django.contrib import admin

from .models import Reserva, Image

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['email','nombre','comentario','telefono', 'fecha_inicio', 'fecha_fin','num_personas']
    search_fields= ['nombre','email','fecha_inicio']
    list_filter= ['fecha_inicio','fecha_fin','email']
    list_per_page = 20



admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Image)

