from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^contacto/', views.contacto, name='contacto'),
    path(r'^habitaciones/$', views.habitaciones, name='habitaciones'),
    path(r'^nosotros/$', views.Nosotros, name='Nosotros'),
    path(r'^lista_reservas/', views.lista_reserva, name='Reservas'),
    path(r'login/', auth_views.LoginView.as_view(), name='login'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_forms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),
     re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
]
    

