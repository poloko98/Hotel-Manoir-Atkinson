from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^contacto/$', views.contacto, name='contacto'),
]