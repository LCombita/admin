from django.db import models
from registration.models import User, Grantor
from project.models import Proyecto
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse_lazy


class ActoJuridico(models.Model):
    nombre_acto = models.CharField(max_length=100, unique=True, verbose_name='Acto Jurídico')

    class Meta:
        verbose_name = 'Acto Jurídico'
        verbose_name_plural = 'Actos Jurídicos'
        ordering = ['nombre_acto',]

    def __str__(self):
        return self.nombre_acto

        
class Reparto(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    protocolista = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name='Asistente Escrituración',limit_choices_to={'groups__name': 'escrituracion'})
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, db_index=True, verbose_name='Proyecto')
    acto_juridico = models.ManyToManyField(
        ActoJuridico, related_name='acto_juridico', db_index=True, verbose_name='Acto Jurídico')
    fecha_reparto = models.DateField(
        verbose_name='Fecha Reparto', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")
    escritura = models.CharField(
        max_length=5, null=True, blank=True, verbose_name='Número Escritura') 
    fecha_escritura = models.DateField(
        null=True, blank=True, verbose_name='Fecha Escritura')
    hoja_ruta = models.CharField(max_length=20, null = True, blank=True)
    anio_escritura = models.CharField(max_length=10, unique=True, null = True, blank=True)
    activo = models.BooleanField(
        default=True,verbose_name='Reparto Activo')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    editado = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')

    class Meta:
        verbose_name = 'Hoja de Ruta'
        verbose_name_plural = 'Hojas de Ruta'
    
    #def get_absolute_url(self):
    #    return reverse_lazy('deed:reparto-update', args=[self.object.id])

    def __str__(self):
        return str(self.hoja_ruta)


class Inmueble(models.Model):
    reparto = models.ForeignKey(
        Reparto, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto')
    inmueble = models.CharField(
        max_length=150, verbose_name='Inmueble', help_text='Describa qué tipo de inmueble es.')
    matricula = models.CharField(
        max_length=150, verbose_name='Matricula Inmobiliaria', help_text='Ingrese el número de matrícula completo')    

    class Meta:
        verbose_name='Inmueble'
        verbose_name_plural = 'Inmuebles'

    def __str__(self):
        return self.inmueble
    

class OtorganteReparto(models.Model):
    reparto = models.ForeignKey(
        Reparto, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto')
    otorgante = models.ForeignKey(
        Grantor, on_delete=models.CASCADE, db_index=True, verbose_name='Otorgante', limit_choices_to={'groups__name': 'otorgante'})
    factura = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Número Factura')
    derechos_notariales = models.DecimalField(
        max_digits=9, decimal_places=1, null=True, blank=True, verbose_name='Derechos Notariales')
    valor_registro = models.DecimalField(
        max_digits=9, decimal_places=1, null=True, blank=True, verbose_name='Registro')
    valor_rentas = models.DecimalField(
        max_digits=9, decimal_places=1, null=True, blank=True,verbose_name='Rentas')
    canje = models.BooleanField(
        default=False, verbose_name='Para Canje')

    
    #pendiente metodo para calcular el total

    class Meta:
        verbose_name = 'Otorgante'
        verbose_name_plural = 'Otorgantes'

    def __str__(self):
        return str(self.otorgante)


#SEÑALES
@receiver(post_save, sender=Reparto)
def actualizar_hojaruta(sender, instance, **kwargs):
    """Señal para actualizar el campo hoja_ruta, sancando el año de la fecha de reparto
    concatenado con el id."""
    
    if kwargs.get('created', False):
        re = Reparto.objects.get(id=instance.id)
        Reparto.objects.filter(id=instance.id).update(
            hoja_ruta=re.fecha_reparto.strftime('%Y') + str(instance.id))

@receiver(post_save, sender=Reparto)
def actualizar_anioescritura(sender, instance, **kwargs):
    #Señal para actualiar el campo anio_escritura, tomando el año de la fecha de la escritura,
    #se concatena con un - y el número de la escritura    
    if not kwargs.get('created', False):
        re = Reparto.objects.get(id=instance.id)
        if re.fecha_escritura and re.escritura:
            Reparto.objects.filter(id=instance.id).update(
                anio_escritura=re.fecha_escritura.strftime('%Y') + '-' + re.escritura)
        elif re.fecha_escritura or re.escritura:
            Reparto.objects.filter(id=instance.id).update(
                anio_escritura=None)
        else:
            pass

#consultas
#https://programmerclick.com/article/66081820135/