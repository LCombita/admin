from django.contrib import admin
from .models import Reparto, ActoJuridico, Proyecto, Inmueble, OtorganteReparto
#from .models import Etapa, RepartoEtapa, ObservacionEtapa, Revision, Impuesto, Cliente


class RepartoAdmin(admin.ModelAdmin):
    """personaliza el admin de de escrituración, registrado todos los modelos correspondientes"""

    list_display = ('id', 'hoja_ruta', 'fecha_reparto', 'anio_escritura', 'proyecto', 'activo')
    list_filter = ('activo', 'proyecto')
    search_fields = ('id', 'hoja_ruta', 'anio_escritura')
    ordering = ('-id',)


admin.site.register(Reparto, RepartoAdmin)
#admin.site.register(Cliente)
admin.site.register(ActoJuridico)
admin.site.register(Proyecto)
admin.site.register(Inmueble)
admin.site.register(OtorganteReparto)
#admin.site.register(Etapa)
#admin.site.register(RepartoEtapa)
#admin.site.register(ObservacionEtapa)
#admin.site.register(Revision)
#admin.site.register(Impuesto)

