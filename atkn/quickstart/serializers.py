from django.contrib.auth.models import User, Group
from rest_framework import serializers
from atkn.models import Reserva

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ('email', 'nombre','comentario','telefono','fecha_inicio','fecha_fin','num_personas',)
 