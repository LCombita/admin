from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Count
from .forms import ReportRepartoXOtorganteForm
from deed.models import Reparto
from registration.models import Grantor, Escrituracion
from registration.mixin import CheckTraMixin, CheckAdmRepMixin, CheckAdmRepEscJurFinFacTraMixin


"""Las lineas @method_decorator(login_required, name='dispatch'), se utlizan para que vista
solo sea gestionada por un usuario que haya iniciado sesión en el sistema.
Las clases *Mixin se heredan para controlar que la vista la pueda ejecutar un usuario 
que pertenece a un grupo específico."""


@method_decorator(login_required, name='dispatch')
class ReportRepartosXOtorganteView(CheckAdmRepEscJurFinFacTraMixin, TemplateView):
    """Gestiona el reporte repartos por otorgante. Se modifica el metodo post para capturar
    el número de identificación introducido para buscar los repartos asociados a este y
    enviarlos como contexto al template dispuesto para ello. La vista la pueden ejecutar los usuarios
    que pertenecen a los grupos administrador, reparto, escrituracion, juridica, finalizacion,
    facturación, y tramitador."""

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


@method_decorator(login_required, name='dispatch')
class ReportRepartoTramitadorListView(CheckTraMixin, ListView):
    """Gestiona el reporte repartos por tramitador. Se modifica el metodo get_queryset para
    filtrar los repartos asociados al tramitador logueado en el sistema y enviarlos como
    contexto al template dispuesto para ello. La vista la pueden ejecutar los usuarios
    que pertenecen al grupo tramitador."""

    model=Reparto
    template_name = 'reports/repartos_x_tramitador.html'

    def get_queryset(self):
        #Se crea un filtro para que se muestren solo los repartos activos
        #correspondientes al tramitador logueado
        return super().get_queryset().filter(
            activo='True').filter(
                proyecto__tramitador=self.request.user.id).order_by('-id')


@method_decorator(login_required, name='dispatch')
class ReportRepartosXAsistenteEscrituracionView(CheckAdmRepMixin, TemplateView):
    """Gestiona un reporte que muestra la cantidad de repartos por asistente de escrituración,
    el reporte muestra los datos agrupados por asistente con la respectiva cantidad de repartos
    asociados. Se modifica el metodo get_context_data paracrear el filtro que prepara los datos
    y se envía como contexto al template dispuesto para ello. La vista la solo la pueden ejecutar
    los usuarios de los grupos administrador y reparto."""
    
    template_name = 'reports/repartos_x_asistente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asistentes'] = Escrituracion.objects.filter(
            groups__name='escrituracion', reparto__activo = True).annotate(cant_reparto = Count('reparto'))
        return context

