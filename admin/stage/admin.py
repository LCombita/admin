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
    """personaliza el admin de etapas, personaliza el modelo Etapa"""

    list_display = ('id',
        'orden',
        'tipo_etapa',
        'nombre_etapa',
        'activo')
    search_fields = ('id', 'nombre_etapa')
    ordering = ('id',)

class ObservacionEtapaAdmin(admin.ModelAdmin):
    """personaliza el admin de etapas, personaliza el modelo ObservacionEtapa """
    list_display = (
        'id',
        'reparto_etapa',
        'observacion')
    search_fields = ('reparto_etapa',)
    ordering = ('id',)


admin.site.register(Etapa, EtapaAdmin)
admin.site.register(RepartoEtapa, RepartoEtapaAdmin)
admin.site.register(ObservacionEtapa, ObservacionEtapaAdmin)
admin.site.register(Revision)
admin.site.register(Impuesto)