from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
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
        max_length=15, unique=True,
        help_text='Debe ingresar una identificacion',
        verbose_name='Identificacion')
    
    #establecer email como username para inicio de sesión
    USERNAME_FIELD = 'email'
    #se debe establecer como requerido para manejo interno de django.
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email
