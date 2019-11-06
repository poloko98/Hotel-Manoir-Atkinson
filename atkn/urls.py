from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^contacto/$', views.contacto, name='contacto'),
    path(r'^habitaciones/$', views.habitaciones, name='habitaciones'),
    path(r'^nosotros/$', views.Nosotros, name='Nosotros'),
]
