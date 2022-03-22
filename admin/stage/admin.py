from django.contrib import admin
from .models import Etapa, RepartoEtapa, ObservacionEtapa, Revision, Impuesto


class RepartoEtapaAdmin(admin.ModelAdmin):
    """personaliza el admin de de escrituración, registrado todos los modelos correspondientes"""

    list_display = ('id',
        'tipo_repartoetapa',
        'reparto',
        'etapa',
        'orden',
        'fecha_inicio',
        'fecha_final',
        'finalizado')
    list_filter = ('finalizado', 'reparto')
    search_fields = ('id', 'reparto')
    ordering = ('id',)


class EtapaAdmin(admin.ModelAdmin):
    """personaliza el admin de de escrituración, registrado todos los modelos correspondientes"""

    list_display = ('id',
        'orden',
        'tipo_etapa',
        'nombre_etapa',
        'activo')
    search_fields = ('id', 'nombre_etapa')
    ordering = ('id',)

admin.site.register(Etapa, EtapaAdmin)
admin.site.register(RepartoEtapa, RepartoEtapaAdmin)
admin.site.register(ObservacionEtapa)
admin.site.register(Revision)
admin.site.register(Impuesto)