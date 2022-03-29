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

    """los siguientes metodos se utilizar para identificar que tipo de rol o a qué
    grupo pertenece el usuario. Devuelven True si el grupo consultado existe"""
    def es_administrador(self):
        return True if user_in_groups(self, ['administrador']) else False

    def es_autenticaciones(self):
        return True if user_in_groups(self, ['autenticaciones']) else False

    def es_ciudadano(self):
        return True if user_in_groups(self, ['ciudadano']) else False

    def es_declaraciones(self):
        return True if user_in_groups(self, ['declaraciones']) else False

    def es_escrituracion(self):
        return True if user_in_groups(self, ['escrituracion']) else False

    def es_facturacion(self):
        return True if user_in_groups(self, ['facturacion']) else False

    def es_finalizacion(self):
        return True if user_in_groups(self, ['finalizacion']) else False

    def es_juridica(self):
        return True if user_in_groups(self, ['juridica']) else False

    def es_otorgante(self):
        return True if user_in_groups(self, ['otorgante']) else False

    def es_reparto(self):
        return True if user_in_groups(self, ['reparto']) else False
    
    def es_tramitador(self):
        return True if user_in_groups(self, ['tramitador']) else False

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


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


class Administrador(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán administradores."""

    class Meta:
        proxy = True
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"


class Autenticaciones(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán de autenticaciones."""

    class Meta:
        proxy = True
        verbose_name = "Autenticaciones"
        verbose_name_plural = "Autenticaciones"


class Ciudadano(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán ciudadanos."""

    class Meta:
        proxy = True
        verbose_name = "Ciudadano"
        verbose_name_plural = "Ciudadanos"


class Declaraciones(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán declaraciones."""

    class Meta:
        proxy = True
        verbose_name = "Declaraciones"
        verbose_name_plural = "Declaraciones"


class Escrituracion(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán escrituracion."""

    class Meta:
        proxy = True
        verbose_name = "Escrituracion"
        verbose_name_plural = "Asistentes_Escrituracion"


class Facturacion(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán facturacion."""

    class Meta:
        proxy = True
        verbose_name = "Facturacion"
        verbose_name_plural = "Facturadores"


class Finalizacion(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán finalizacion."""

    class Meta:
        proxy = True
        verbose_name = "Finalizacion"
        verbose_name_plural = "Finalizacion"


class Juridica(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán juridica."""

    class Meta:
        proxy = True
        verbose_name = "Juridica"
        verbose_name_plural = "Juridica"


class Grantor(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán otorgantes."""

    class Meta:
        proxy = True
        verbose_name = "Otorgante"
        verbose_name_plural = "Otorgantes"


class RepartoUser(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán reparto."""

    class Meta:
        proxy = True
        verbose_name = "Reparto"
        verbose_name_plural = "Reparto"


class Tramitador(User):
    """Modelo proxi para personalizar el comportamiento de los usuarios 
    que serán otorgantes."""

    class Meta:
        proxy = True
        verbose_name = "Tramitador"
        verbose_name_plural = "Tramitadores"


#FUNCIONES GLOBALES
def user_in_groups(user, list_groups):
    """Validar sin un usuario pertenece a uno o más grupos, con el fin
    de establecer restricciones con respecto a los permisos de cada grupo"""
    
    return True if user.groups.filter(name__in=list_groups) else False


@receiver(post_save, sender=Grantor)
def create_data_otorgante(sender, instance, **kwargs):
    """Señal para crear una instancia de Grantor en DataGrantor, para los datos
    que corresponden solo a los otorgantes. Además, al crear el otorgante, se verifica
    que el grupo otorgante exista y se agrega el grupo al otorgante, si el grupo no existe,
    se crea el grupo y luego se agrega al usuario. Se comprueba con los tests:
    GrantorTestCase y GroupTestCase"""
    
    if kwargs.get('created', False):
        DataGrantor.objects.get_or_create(user=instance)
        #crear y/o asignar grupo otorgate
        existgroup = Group.objects.filter(name='otorgante').exists()
        if existgroup:
            grp =  Group.objects.get(name='otorgante')
            instance.groups.add(grp)
        else:
            grp = Group.objects.create(name='otorgante')
            instance.groups.add(grp)

@receiver(post_save, sender=Administrador)
def add_group_to_administrador(sender, instance, **kwargs):
    """Señal para asignar el grupo administrador invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'administrador', **kwargs)

@receiver(post_save, sender=Autenticaciones)
def add_group_to_autenticaciones(sender, instance, **kwargs):
    """Señal para asignar el grupo autenticaciones invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'autenticaciones', **kwargs)

@receiver(post_save, sender=Ciudadano)
def add_group_to_ciudadano(sender, instance, **kwargs):
    """Señal para asignar el grupo ciudadano invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'ciudadano', **kwargs)

@receiver(post_save, sender=Declaraciones)
def add_group_to_declaraciones(sender, instance, **kwargs):
    """Señal para asignar el grupo declaraciones invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'declaraciones', **kwargs)

@receiver(post_save, sender=Escrituracion)
def add_group_to_escrituracion(sender, instance, **kwargs):
    """Señal para asignar el grupo escrituracion invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'escrituracion', **kwargs)

@receiver(post_save, sender=Facturacion)
def add_group_to_facturacion(sender, instance, **kwargs):
    """Señal para asignar el grupo facturacion invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'facturacion', **kwargs)

@receiver(post_save, sender=Finalizacion)
def add_group_to_finalizacion(sender, instance, **kwargs):
    """Señal para asignar el grupo finalizacion invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'finalizacion', **kwargs)

@receiver(post_save, sender=Juridica)
def add_group_to_juridica(sender, instance, **kwargs):
    """Señal para asignar el grupo juridica invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'juridica', **kwargs)

@receiver(post_save, sender=RepartoUser)
def add_group_to_reparto(sender, instance, **kwargs):
    """Señal para asignar el grupo reparto invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'reparto', **kwargs)

@receiver(post_save, sender=Tramitador)
def add_group_to_tramitador(sender, instance, **kwargs):
    """Señal para asignar el grupo tramitador invocando la funcion add_groups_to_users."""

    add_groups_to_users(instance, 'tramitador', **kwargs)

def add_groups_to_users(instance, grp, **kwargs):
    """Se verifica que el grupo enviado exista y se agrega el grupo al usuario.
    Si el grupo no existe, se crea el grupo y luego se agrega al usuario."""

    if kwargs.get('created', False):
        existgroup = Group.objects.filter(name=grp).exists()
        if existgroup:
            grp =  Group.objects.get(name=grp)
            instance.groups.add(grp)
        else:
            grp = Group.objects.create(name=grp)
            instance.groups.add(grp)