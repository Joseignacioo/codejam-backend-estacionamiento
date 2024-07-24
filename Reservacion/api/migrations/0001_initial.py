# Generated by Django 5.0.6 on 2024-07-24 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo_electronico', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('tipo_reservacion', models.CharField(choices=[('DIA', 'DIA COMPLETO'), ('MAÑANA', 'SOLO MAÑANA 8:00-14:00'), ('TARDE', 'SOLO TARDE 14:00-20:00')], max_length=100)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('C', 'Confirmada'), ('X', 'Cancelada')], max_length=1)),
                ('motivo_cancelacion', models.CharField(blank=True, max_length=100, null=True)),
                ('estacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estacionamiento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
    ]
