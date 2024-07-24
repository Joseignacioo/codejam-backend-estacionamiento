from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

# Create your views here.
class CreateReservacionViewset(viewsets.ModelViewSet):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateReportesViewset(viewsets.ModelViewSet):
    queryset = Reportes.objects.all()
    serializer_class = ReportesSerializer

class CreateUsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]  # Solo accesible por admin

class CreateEstacionamientoViewSet(viewsets.ModelViewSet):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer