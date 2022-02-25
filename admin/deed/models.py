from turtle import update
from django.db import models
from django.utils.timezone import now
from registration.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class ActoJuridico(models.Model):
    nombre_acto = models.CharField(max_length=100, unique=True, verbose_name='Acto Jurídico')

    class Meta:
        verbose_name = 'Acto Jurídico'
        verbose_name_plural = 'Actos Jurídicos'

    def __str__(self):
        return self.nombre_acto


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100, unique=True, verbose_name='Cliente')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre_cliente


class Proyecto(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, db_index=True, verbose_name='Cliente')
    tramitador = models.ManyToManyField(
        User, db_index=True, related_name='tramitador', verbose_name='Tramitador')
    nombre_proyecto = models.CharField(max_length=100, unique=True, verbose_name='Proyecto')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre_proyecto

#funciones para reparto
def HojaRuta():
        """retorna el id para mostrarlo en el formulario como hoja de ruta"""
        return str(Reparto.id)

def AnioEscritura(self):
        """concatena el año de la fecha de escritura con el número de la escritura"""
        if self.fecha_escritura:
            a = self.fecha_escritura.strftime('%Y')
            ae = a + '-' + str(self.escritura)
            return ae
        else:
            return None
        
class Reparto(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    protocolista = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True, verbose_name='Asistente Escrituración')
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, db_index=True, verbose_name='Proyecto')
    acto_juridico = models.ManyToManyField(
        ActoJuridico, related_name='acto_juridico', db_index=True, verbose_name='Acto Jurídico')
    fecha_reparto = models.DateField(
        verbose_name='Fecha Reparto', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")
    escritura = models.CharField(
        max_length=5, null=True, blank=True, verbose_name='Número Escritura') 
    fecha_escritura = models.DateField(
        null=True, blank=True, verbose_name='Fecha Escritura', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")
    hoja_ruta = models.CharField(max_length=20, null = True, blank=True)
    anio_escritura = models.CharField(max_length=10, unique=True, null = True, blank=True)
    activo = models.BooleanField(
        default=True,verbose_name='Reparto Activo')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    editado = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')

    class Meta:
        verbose_name = 'Hoja de Ruta'
        verbose_name_plural = 'Hojas de Ruta'
    
    def __str__(self):
        return str(self.id)


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
        User, on_delete=models.CASCADE, db_index=True, verbose_name='Otorgante')
    factura = models.CharField(
        max_length=20, verbose_name='Número Factura')
    derechos_notariales = models.DecimalField(
        max_digits=9, decimal_places=1, verbose_name='Derechos Notariales')
    valor_registro = models.DecimalField(
        max_digits=9, decimal_places=1, verbose_name='Registro')
    valor_rentas = models.DecimalField(
        max_digits=9, decimal_places=1, verbose_name='Rentas')
    canje = models.BooleanField(
        default=False, verbose_name='Para Canje')

    
    #pendiente metodo para calcular el total

    class Meta:
        verbose_name = 'Otorgante'
        verbose_name_plural = 'Otorgantes'


class Etapa(models.Model):
    nombre_etapa = models.CharField(
        max_length=150, verbose_name='Etapa')
    activo = models.BooleanField(
        default=True, verbose_name='Activa')

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __ster__(self):
        return self.nombre_etapa


class RepartoEtapa(models.Model):
    reparto = models.ForeignKey(
        Reparto, on_delete=models.CASCADE, db_index=True, verbose_name='Reparto')
    etapa = models.ForeignKey(
        Etapa, on_delete=models.CASCADE, db_index=True, verbose_name='Etapa')
    fecha_inicio = models.DateField(
        verbose_name='Fecha Inicio', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")
    fecha_final = models.DateField(
        verbose_name='Fecha Final', help_text="Introduzca la fecha en formato: <em>YYYY-MM-DD</em>.")

    class Meta:
        verbose_name = 'Etapa Hoja Ruta'
        verbose_name_plural = 'Etapas Hoja Ruta'
        ordering = ['-id']


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
        Reparto.objects.filter(id=instance.id).update(
            anio_escritura=re.fecha_escritura.strftime('%Y') + '-' + re.escritura)


#consultas
#https://programmerclick.com/article/66081820135/