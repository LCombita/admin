from django.db import models
from deed.models import Reparto
from django.dispatch import receiver
from django.db.models.signals import post_save


class Etapa(models.Model):
    SELECCIONE = 'SEL'
    RECEPCION = 'REC'
    EXTENCION = 'EXT'
    OTORGAMIENTO = 'OTO'
    AUTORIZACION = 'AUT'
    tipo_etapa_choices = [
        (SELECCIONE, 'SELECCIONE'),
        (RECEPCION, 'RECEPCION'),
        (EXTENCION, 'EXTENCION'),
        (OTORGAMIENTO, 'OTORGAMIENTO'),
        (AUTORIZACION, 'AUTORIZACION'),
    ]

    tipo_etapa = models.CharField(
            max_length=3, choices=tipo_etapa_choices, default=SELECCIONE)
    nombre_etapa = models.CharField(
        max_length=150, verbose_name='Etapa')
    activo = models.BooleanField(
        default=True, verbose_name='Activa')

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __str__(self):
        return self.nombre_etapa


class RepartoEtapa(models.Model):
    reparto = models.ForeignKey(
        Reparto, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto')
    etapa = models.ForeignKey(
        Etapa, on_delete=models.CASCADE, db_index=True, verbose_name='Etapa')
    fecha_inicio = models.DateField(
        verbose_name='Fecha Inicio', null=True, blank=True)
    fecha_final = models.DateField(
        verbose_name='Fecha Final', null=True, blank=True)

    class Meta:
        verbose_name = 'Etapa Hoja Ruta'
        verbose_name_plural = 'Etapas Hoja Ruta'
        ordering = ['id']


class ObservacionEtapa(models.Model):
    reparto_etapa = models.ForeignKey(
        RepartoEtapa, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto - Etapa')
    observacion = models.CharField(
        max_length=150, verbose_name='Observación')

    class Meta:
        verbose_name = 'Observación'
        verbose_name_plural = 'Observaciones'

    def __str__(self):
        return self.observacion


class Revision(models.Model):
    reparto_etapa = models.ForeignKey(
        RepartoEtapa, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto - Etapa')
    fecha_revision = models.DateField(
        verbose_name='Fecha Final', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")
    reproceso = models.BooleanField(
        default=False, verbose_name='Hubo Reproceso')
    descripcion = models.CharField(
        max_length=200, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Revisión'
        verbose_name_plural = 'Revisiones'

    def __str__(self):
        return self.descripcion


class Impuesto(models.Model):
    reparto_etapa = models.ForeignKey(
        RepartoEtapa, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto - Etapa')
    boleta_rentas = models.CharField(
        max_length=20, verbose_name='Boleta Rentas')
    fecha_boleta_rentas = models.DateField(
        verbose_name='Fecha Boleta Rentas', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")
    boleta_registro = models.CharField(
        max_length=20, verbose_name='Boleta Registro')
    fecha_boleta_registro = models.DateField(
        verbose_name='Fecha Boleta Registro', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")

    class Meta:
        verbose_name = 'Impuesto'
        verbose_name_plural = 'Impuestos'


@receiver(post_save, sender=Reparto)
def agregar_etapas_reparto(sender, instance, **kwargs):
    if kwargs.get('created', False):
        et = Etapa.objects.filter()
        for e in et:
            RepartoEtapa.objects.create(reparto=instance, etapa=e)