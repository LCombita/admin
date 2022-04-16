from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Count
from .forms import ReportRepartoXOtorganteForm
from deed.models import Reparto
from registration.models import Grantor, Escrituracion


@method_decorator(login_required, name='dispatch')
class ReportRepartosXOtorganteView(TemplateView):
    
    template_name = 'reports/repartos_x_otorgante.html'

    def dispatch(self, request, *args, **kwargs):
        grps = [
            'administrador',
            'reparto',
            'escrituracion',
            'juridica',
            'finalizacion',
            'facturacion']
        if user_in_groups(self.request.user, grps):
            return super(ReportRepartosXOtorganteView, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))

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


@method_decorator(login_required, name='dispatch')
class ReportRepartoTramitadorListView(ListView):
    """Gestiona la lista de hojas de ruta"""
    model=Reparto
    template_name = 'reports/repartos_x_tramitador.html'

    def dispatch(self, request, *args, **kwargs):
        if user_in_groups(self.request.user, ['tramitador']):
            return super(ReportRepartoTramitadorListView, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))

    def get_queryset(self):
        #Se crea un filtro para que se muestren solo los repartos activos
        #correspondientes al tramitador logueado
        return super().get_queryset().filter(
            activo='True').filter(
                proyecto__tramitador=self.request.user.id).order_by('-id')


@method_decorator(login_required, name='dispatch')
class ReportRepartosXAsistenteEscrituracionView(TemplateView):
    
    template_name = 'reports/repartos_x_asistente.html'

    def dispatch(self, request, *args, **kwargs):
        if user_in_groups(self.request.user, ['reparto, administrador']):
            return super(ReportRepartosXAsistenteEscrituracionView, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asistentes'] = Escrituracion.objects.filter(
            groups__name='escrituracion', reparto__activo = True).annotate(cant_reparto = Count('reparto'))
        return context

#FUNCIONES GENERALES
def user_in_groups(user, list_groups):
    """Validar sin un usuario pertenece a uno o más grupos, con el fin
    de establecer restricciones con respecto a los permisos de cada grupo"""
    
    return True if user.groups.filter(name__in=list_groups) else False
