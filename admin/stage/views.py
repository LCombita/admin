from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.detail import SingleObjectMixin
from .models import Etapa, RepartoEtapa, ObservacionEtapa, Revision, Impuesto
from registration.models import User
from registration.mixin import CheckAdmRepMixin, CheckEscFacJurFinMixin
from .forms import EtapaCreateForm, EtapaUpdateForm, RepartoEtapaUpdateForm
from .forms import RevisionInlineFormSet, ImpuestoInlineFormSet, RepartoEtapaObservacionesForm
from django.views.generic import DetailView, CreateView, UpdateView, ListView, FormView, TemplateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


"""Las lineas @method_decorator(login_required, name='dispatch'), se utlizan para que vista
solo sea gestionada por un usuario que haya iniciado sesión en el sistema.
Las clases *Mixin se heredan para controlar que la vista la pueda ejecutar un usuario 
que pertenece a un grupo específico."""


@method_decorator(login_required, name='dispatch')
class EtapaCreateView(CheckAdmRepMixin, CreateView):
    """Gestiona el formulario para crear etapas. La vista solo la pueden ejecutar los usuarios
    que pertenecen a los grupos administrador y reparto. La restrección la controla la CheckAdmRepMixin."""

    model = Etapa
    form_class = EtapaCreateForm
    template_name = 'stage/etapa_create_form.html'

    def get_success_url(self):
        return reverse_lazy('stage:etapa-list')


@method_decorator(login_required, name='dispatch')
class EtapaListView(CheckAdmRepMixin, ListView):
    """Gestiona la lista de las etapas registradas en el sistema, empleando para ello el template
    etapa_list.html. La vista solo la pueden ejecutar los usuarios que pertenecen a los grupos
    administrador y reparto. La restrección la controla la CheckAdmRepMixin."""
    
    model=Etapa

@method_decorator(login_required, name='dispatch')
class EtapaDeleteView(CheckAdmRepMixin, DeleteView):
    """Gestiona la eliminación de una etapa, empleando el template etapa_confirm_delete.html 
    para la confirmación de la eliminación de la etapa. La vista solo pueden ejecutar los usuarios
    que pertenecen a los grupos administrador y reparto. La restrección la controla la CheckAdmRepMixin."""
    
    model = Etapa
    success_url = reverse_lazy('stage:etapa-list')

@method_decorator(login_required, name='dispatch')
class EtapaUpdateView(CheckAdmRepMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos de las etapas. La vista solo la
    pueden ejecutar los usuarios que pertenecen a los grupos administrador y reparto.
    La restrección la controla la CheckAdmRepMixin."""

    model = Etapa
    form_class = EtapaUpdateForm
    template_name = 'stage/etapa_update_form.html'

    def get_success_url(self):
        return reverse_lazy('stage:etapa-list')


#REPARTO ETAPA
@method_decorator(login_required, name='dispatch')
class RepartoEtapaUpdateView(CheckEscFacJurFinMixin, UpdateView):
    model = RepartoEtapa
    form_class = RepartoEtapaUpdateForm
    template_name = 'stage/reparto-etapa_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['observaciones'] = ObservacionEtapa.objects.filter(reparto_etapa=self.object.id)
        context['revision'] = Revision.objects.filter(reparto_etapa=self.object.id)
        context['impuesto'] = Impuesto.objects.filter(reparto_etapa=self.object.id)
        return context

    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-update', args=[self.object.id])


@method_decorator(login_required, name='dispatch')
class RepartoEtapaDetailView(DetailView):
    model = RepartoEtapa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['observaciones'] = ObservacionEtapa.objects.filter(reparto_etapa=self.object.id)
        context['impuesto'] = Impuesto.objects.filter(reparto_etapa=self.object.id)
        context['revision'] = Revision.objects.filter(reparto_etapa=self.object.id)
        return context


#OBSERVACIONES REPARTO ETAPAS
@method_decorator(login_required, name='dispatch')
class ObservacionCreateView(CheckEscFacJurFinMixin, TemplateView):
    """Esta vista controla la creación de observaciones desde RepartoEtapaUdate.
    Recibe por url el codigo del RepartoEtapa que se está editanto para crear la observación
    y el usuario que ha iniciado sesión"""

    template_name = 'stage/reparto-etapa_observaciones.html'

    def post(self, request, *args, **kwargs):
        """Se sobrescribe este método para crear la observación con base en id RepartoEtapa
        recibido en la url"""

        obs = request.POST.get('observacion', '')
        if obs:
            usr = User.objects.get(id=self.request.user.id)
            repeta = RepartoEtapa.objects.get(id=self.kwargs['id'])
            ObservacionEtapa.objects.create(
                reparto_etapa=repeta, observacion = obs, usuario = usr.username)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        """Sobre escribe el get_context_Data para enviar al template el formulario de las
        observaciones y el id recibido en la url"""

        context = super().get_context_data(**kwargs)
        context['form'] = RepartoEtapaObservacionesForm()
        context['rep_eta'] = RepartoEtapa.objects.get(id=self.kwargs['id'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-update', args=[self.kwargs['id']])


@method_decorator(login_required, name='dispatch')
class ObservacionCreate2View(TemplateView):
    """Esta vista controla la creación de observaciones desde RepartoEtapaDetail.
    Recibe por url el codigo del RepartoEtapa que se está editanto para crear la observación
    y el usuario que ha iniciado sesión"""

    template_name = 'stage/reparto-etapa_observaciones.html'

    def dispatch(self, request, *args, **kwargs):
        if user_in_groups(self.request.user, ['tramitador']):
            return super(ObservacionCreate2View, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))

    def post(self, request, *args, **kwargs):
        """Se sobrescribe este método para crear la observación con base en id RepartoEtapa
        recibido en la url"""

        obs = request.POST.get('observacion', '')
        if obs:
            usr = User.objects.get(id=self.request.user.id)
            repeta = RepartoEtapa.objects.get(id=self.kwargs['id'])
            ObservacionEtapa.objects.create(
                reparto_etapa=repeta, observacion = obs, usuario = usr.username)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        """Sobre escribe el get_context_Data para enviar al template el formulario de las
        observaciones y el id recibido en la url"""

        context = super().get_context_data(**kwargs)
        context['form'] = RepartoEtapaObservacionesForm()
        context['rep_eta'] = RepartoEtapa.objects.get(id=self.kwargs['id'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-detail', args=[self.kwargs['id']])


#REVISION EN ETAPAS
@method_decorator(login_required, name='dispatch')
class RevisionRepartoEtapaEditView(SingleObjectMixin, FormView):

    model = RepartoEtapa
    template_name = 'stage/reparto-etapa_revision_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if user_in_groups(self.request.user, ['juridica']):
            return super(RevisionRepartoEtapaEditView, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=RepartoEtapa.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=RepartoEtapa.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self):
        form_class = RevisionInlineFormSet
        RepartoEtapaRevisionFormSet = inlineformset_factory(
            RepartoEtapa, Revision, fields=(
                'fecha_revision',
                'reproceso',
                'descripcion',),
            form=form_class, max_num=Revision.objects.filter(reparto_etapa=self.object).count()+1)
        return RepartoEtapaRevisionFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-update', args=[self.object.id])


#IMPUESTO EN ETAPAS
@method_decorator(login_required, name='dispatch')
class ImpuestoRepartoEtapaEditView(SingleObjectMixin, FormView):

    model = RepartoEtapa
    template_name = 'stage/reparto-etapa_impuesto_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if user_in_groups(self.request.user, ['finalizacion']):
            return super(ImpuestoRepartoEtapaEditView, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=RepartoEtapa.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=RepartoEtapa.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self):
        form_class = ImpuestoInlineFormSet
        RepartoEtapaImpuestoFormSet = inlineformset_factory(
            RepartoEtapa, Impuesto, fields=(
                'reparto_etapa',
                'boleta_rentas',
                'fecha_boleta_rentas',
                'file_boleta_rentas',
                'boleta_registro',
                'file_boleta_registro',
                'fecha_boleta_registro',),
            form=form_class, max_num=Impuesto.objects.filter(reparto_etapa=self.object).count()+1)
            #form=form_class, max_num=4)
        return RepartoEtapaImpuestoFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-update', args=[self.object.id])

