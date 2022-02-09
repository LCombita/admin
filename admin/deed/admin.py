from django.contrib import admin
from .models import Reparto, Cliente, ActoJuridico, Proyecto, Inmueble, OtorganteReparto
from .models import Etapa, RepartoEtapa, ObservacionEtapa, Revision, Impuesto


class RepartoAdmin(admin.ModelAdmin):
    """personaliza el admin de de escrituración, registrado todos los modelos correspondientes"""

    list_display = ('id', 'fecha_reparto', 'proyecto',)
    list_filter = ('activo', 'canje',)
    search_fields = ('id',)
    orderin = ('id',)


admin.site.register(Reparto, RepartoAdmin)
admin.site.register(Cliente)
admin.site.register(ActoJuridico)
admin.site.register(Proyecto)
admin.site.register(Inmueble)
admin.site.register(OtorganteReparto)
admin.site.register(Etapa)
admin.site.register(RepartoEtapa)
admin.site.register(ObservacionEtapa)
admin.site.register(Revision)
admin.site.register(Impuesto)

