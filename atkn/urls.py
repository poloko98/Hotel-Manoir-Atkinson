from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import include, url

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
from rest_framework import routers
from atkn.quickstart import views as wiw
from . import views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'users', wiw.UserViewSet)
router.register(r'reservas', wiw.ReservaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'contacto/', views.contacto, name='contacto'),
    path(r'lista_reservas/', views.lista_reserva, name='Reservas'),
    
    path(r'nosotros/', views.nosotros, name='Nosotros'),
    path(r'habitaciones/', views.habitaciones, name='habitaciones'),
    

    path(r'menu_adm/', views.menu_adm, name='Menu Administrador'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]