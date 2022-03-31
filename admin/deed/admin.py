from django.contrib import admin
from .models import Reparto, ActoJuridico, Inmueble, OtorganteReparto
#from .models import Etapa, RepartoEtapa, ObservacionEtapa, Revision, Impuesto, Cliente


class RepartoAdmin(admin.ModelAdmin):
    """personaliza el admin de de escrituración, registrando el modelo Reparto"""

    list_display = ('id', 'hoja_ruta', 'fecha_reparto', 'anio_escritura', 'proyecto', 'activo')
    list_filter = ('activo', 'proyecto')
    search_fields = ('id', 'hoja_ruta', 'anio_escritura')
    ordering = ('-id',)
    filter_horizontal = ('acto_juridico',)


class OtorganteRepartoAdmin(admin.ModelAdmin):
    """personaliza el admin de de escrituración, registrando el modelo OtorganteReparto"""

    list_display = (
        'reparto',
        'otorgante',
        'factura',
        'derechos_notariales',
        'valor_rentas',
        'valor_registro',
        'canje')
    list_filter = ('reparto',)
    search_fields = ('reparto', 'otorgante')
    ordering = ('-reparto',)


admin.site.register(Reparto, RepartoAdmin)
admin.site.register(ActoJuridico)
admin.site.register(Inmueble)
admin.site.register(OtorganteReparto, OtorganteRepartoAdmin)


