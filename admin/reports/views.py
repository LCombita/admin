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
            if Grantor.objects.filter(identification = identificacion).exists():    
                context['repartos'] = Reparto.objects.filter(
                    otorgantereparto__otorgante__identification = identificacion)
                context['otorgante'] = Grantor.objects.get(
                    identification = identificacion)
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReportRepartoXOtorganteForm()
        return context


class ReportRepartoTramitadorListView(ListView):
    """Gestiona la lista de hojas de ruta"""
    model=Reparto
    template_name = 'reports/repartos_x_tramitador.html'

    def get_queryset(self):
        #Se crea un filtro para que se muestren solo los repartos activos
        #correspondientes al tramitador logueado
        return super().get_queryset().filter(
            activo='True').filter(
                proyecto__tramitador=self.request.user.id).order_by('-id')


