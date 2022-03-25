from datetime import datetime
from django.db import models
from deed.models import Reparto
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime


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
    orden = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'
        ordering = ['orden']

    def __str__(self):
        return self.nombre_etapa


class RepartoEtapa(models.Model):
    GENERAL = 'G'
    IMPUESTO = 'I'
    REVISION = 'R'
    tipo_repartoetapa_choices = [
        (GENERAL, 'GENERAL'),
        (IMPUESTO, 'IMPUESTO'),
        (REVISION, 'REVISION'),
    ]
    tipo_repartoetapa = models.CharField(
            max_length=1, choices=tipo_repartoetapa_choices, default=GENERAL)
    reparto = models.ForeignKey(
        Reparto, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto')
    etapa = models.ForeignKey(
        Etapa, on_delete=models.CASCADE, db_index=True, verbose_name='Etapa')
    orden = models.SmallIntegerField(null=True, blank=True)
    fecha_inicio = models.DateField(
        verbose_name='Fecha Inicio', null=True, blank=True)
    fecha_final = models.DateField(
        verbose_name='Fecha Final', null=True, blank=True)
    finalizado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Etapa Hoja Ruta'
        verbose_name_plural = 'Etapas Hoja Ruta'
        ordering = ['id']
    
    def __str__(self):
        return str(self.etapa) + "-" + str(self.reparto)


class ObservacionEtapa(models.Model):
    reparto_etapa = models.ForeignKey(
        RepartoEtapa, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto-Etapa')
    fecha_hora = models.DateTimeField(auto_now_add=True, verbose_name='Fecha-Hora-Observacion')
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
    fecha_revision = models.DateField(verbose_name='Fecha Final')
    reproceso = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Revisión'
        verbose_name_plural = 'Revisiones'

    def __str__(self):
        return self.descripcion


#CONFIGURACION DE RUTAS PARA CARGAR LOS ARCHIVOS DE Impuesto
"""Estas dos funciones configuran la ruta en la que se va a almacenar los archivos con las
liquidaciones de rentas y registro. En caso de que se vaya cambiar el archivo, elimina el anterior
y deja el nuevo archivo cargado con el fin de no guardar archivos innecesarios."""
def rentas_upload_to(instance, filename):
    old_instance=Impuesto.objects.get(pk=instance.pk)
    old_instance.file_boleta_rentas.delete()
    return 'iryr/' + filename

def registro_upload_to(instance, filename):
    old_instance=Impuesto.objects.get(pk=instance.pk)
    old_instance.file_boleta_registro.delete()
    return 'iryr/' + filename

class Impuesto(models.Model):
    """Este modelo es creado para almacenar la información relacionada con el impuesto 
    de rentas y registro. Se relaciona con stage.RepartoEtapa, ya que los impuestos son una
    etapa asociada al trámite."""
    
    reparto_etapa = models.ForeignKey(
        RepartoEtapa, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto - Etapa')
    boleta_rentas = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Boleta Rentas')
    fecha_boleta_rentas = models.DateField(
        verbose_name='Fecha Boleta Rentas', null=True, blank=True)
    file_boleta_rentas = models.FileField(upload_to=rentas_upload_to, null=True, blank=True)
    boleta_registro = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Boleta Registro')
    fecha_boleta_registro = models.DateField(
        verbose_name='Fecha Boleta Registro', null=True, blank=True)
    file_boleta_registro = models.FileField(upload_to=registro_upload_to, null=True, blank=True)

    class Meta:
        verbose_name = 'Impuesto'
        verbose_name_plural = 'Impuestos'


@receiver(post_save, sender=Reparto)
def agregar_etapas_reparto(sender, instance, **kwargs):
    """Esta señal consulta las etapas existentes en stage.Etapa y se crean las instancias de 
    stage.RepartoEtapa para la instancia de deed.Reparto que se está creando en el momento."""

    if kwargs.get('created', False):
        i = 1
        et = Etapa.objects.filter().order_by('orden')
        for e in et:
            RepartoEtapa.objects.create(reparto=instance, etapa=e, orden=i)
            i=i+1
            print("desde el ciclo for: ", i)
        i=1

