from django.db import models
from registration.models import User


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100, unique=True, verbose_name='Cliente')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre_cliente',]

    def __str__(self):
        return self.nombre_cliente


class Proyecto(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, db_index=True, verbose_name='Cliente')
    tramitador = models.ManyToManyField(
        User, db_index=True, related_name='tramitador', verbose_name='Tramitador', limit_choices_to={'groups__name': 'tramitador'})
    nombre_proyecto = models.CharField(max_length=100, unique=True, verbose_name='Proyecto')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['nombre_proyecto',]

    def __str__(self):
        return self.nombre_proyecto
