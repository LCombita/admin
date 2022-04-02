from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .forms import ReportRepartoXOtorganteForm
from deed.models import Reparto
from registration.models import Grantor


class ReportRepartosXOtorganteView(TemplateView):
    
    template_name = 'reports/repartos_x_otorgante.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        identificacion = request.POST.get('identificacion', '')
        if identificacion:
            g = Grantor.objects.filter(identification = identificacion).exists()
            if g:    
                context['repartos'] = Reparto.objects.filter(otorgantereparto__otorgante__identification = identificacion)
                context['otorgante'] = Grantor.objects.get(identification = identificacion)
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReportRepartoXOtorganteForm()
        return context


class ReportRepartoProyectosListView(ListView):
    """Gestiona la lista de hojas de ruta"""
    model=Reparto
"""
    def get_queryset(self):
        #Se crea un filtro para que se muestren solo los repartos activos
        #correspondientes al tramitador logueado
        #TODO: organizar el queryset para mostrar los reparto de los proyectos con tramitador logueado
        qs = super().get_queryset()
        return qs.filter(activo='True').filter(user=self.request.user).order_by('-id')

"""