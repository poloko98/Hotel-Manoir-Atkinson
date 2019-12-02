from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from atkn.quickstart.serializers import UserSerializer, ReservaSerializer
from atkn.models import Reserva

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservas to be viewed or edited.
    """
    queryset = Reserva.objects.all().order_by('-fecha_inicio')
    serializer_class = ReservaSerializer