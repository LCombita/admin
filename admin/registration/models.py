from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    """Esta clase extiende la clase User por defecto de django.
    Se intruducen nuevos campos que son necesarios según el modelo de negocio"""
    email = models.EmailField(
        unique=True, max_length=150, 
        help_text='Debe introducir un email valido, este será usado para iniciar la sesión. Por ejemplo: miusuario@midominio.com.',
        verbose_name='Correo Electrónico')
    first_name = models.CharField(
        max_length=150,verbose_name='Nombres')
    last_name = models.CharField(
        max_length=150, verbose_name='Primer Apellido')
    last_name2 = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name='Segundo Apellido')
    identification = models.CharField(
        max_length=15, unique=True, null=True,
        help_text='Debe ingresar una identificacion',
        verbose_name='Identificacion')
    
    #establecer email como username para inicio de sesión
    USERNAME_FIELD = 'email'
    #se debe establecer como requerido para manejo interno de django.
    REQUIRED_FIELDS = ['username']

    def es_administrador(self):
        """Verificar si el usuario pertenece al grupo administrador"""
        return True if user_in_groups(self, ['administrador']) else False

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email


class Grantor(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios que serán otorgantes.
    Se va a crear una señal, para que cuando se cree un usuario otorgante, automaticamente
    se cree una instancia en modelo DataGrantor, que son datos que solo llevarán los otorgantes"""
    class Meta:
        proxy = True
        verbose_name = "Otorgante"
        verbose_name_plural = "Otorgantes"


class DataGrantor(models.Model):
    """Modelo para agregar los campos que se requieren unicamente para los usuarios que
    actua como otorgantes"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=36, verbose_name='Teléfono',
        help_text='Puede agregar hasta 3 número de teléfono, separados por un / ')
    address = models.CharField(max_length=150, verbose_name='Dirección',
        help_text='Introduzca la dirección completa usando abreviaciones')
    
    class Meta:
        verbose_name = "Datos Otorgante"
        verbose_name_plural = "Datos Otorgantes"


#FUNCIONES GLOBALES
def user_in_groups(user, list_groups):
    """Validar sin un usuario pertenece a uno o más grupos, con el fin
    de establecer restricciones con respecto a los permisos de cada grupo"""
    return True if user.groups.filter(name__in=list_groups) else False

@receiver(post_save, sender=Grantor)
def create_data_otorgante(sender, instance, **kwargs):
    """Señal para crear una instancia de Grantor en DataGrantor, para los datos
    que corresponden solo a los otorgantes. Se comprueba con un test"""
    if kwargs.get('created', False):
        DataGrantor.objects.get_or_create(user=instance)
   
