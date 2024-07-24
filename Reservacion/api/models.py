from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Usuario(models.Model):
    correo_electronico = models.EmailField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.pk and self.contraseña:
            self.contraseña = make_password(self.contraseña)
        super(Usuario, self).save(*args, **kwargs)
    def __str__(self):
        return self.correo_electronico

class Estacionamiento(models.Model):
    codigo = models.CharField(max_length=10)
    estado = models.BooleanField()

    def __str__(self):
        return self.codigo

class Reservacion(models.Model):
    ESTADOS_RESERVACION = [
        ('P', 'Pendiente'),
        ('C', 'Confirmada'),
        ('X', 'Cancelada'),
    ]
    TIPOS_RESERVACION = [
        ('DIA', 'DIA COMPLETO'),
        ('MAÑANA', 'SOLO MAÑANA 8:00-14:00'),
        ('TARDE', 'SOLO TARDE 14:00-20:00'),
    ]
    fecha_creacion = models.DateField(auto_now_add=True)
    tipo_reservacion = models.CharField(max_length=100, choices=TIPOS_RESERVACION)
    estado = models.CharField(max_length=1, choices=ESTADOS_RESERVACION)
    motivo_cancelacion = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    

class Reportes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return self.usuario


