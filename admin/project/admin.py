from django.contrib import admin
from .models import Cliente, Proyecto, User

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    """personaliza el admin del modelo proyecto"""
    list_display = ('cliente', 'nombre_proyecto')
    search_fields = ('nombre_proyecto',)
    orderin = ('nombre_proyecto',)
    filter_horizontal = ('tramitador',)

admin.site.register(Cliente)
admin.site.register(Proyecto, ProyectoAdmin)
