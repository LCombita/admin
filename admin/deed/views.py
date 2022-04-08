from django.views.generic import CreateView, UpdateView, ListView, FormView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeleteView
from .models import Reparto, ActoJuridico, Inmueble, OtorganteReparto
from stage.models import RepartoEtapa
from .forms import RepartoUpdateForm, NumeroEscrituraUpdateForm, RepartoCreateForm
from .forms import ActoCreateForm, ActoUpdateForm
from .forms import InmuebleInlineFormSet, RepartoOtorganteInlineFormSet, RepartoEtapasInlineFormSet
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory


class RepartoUpdateView(UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo reparto"""
    model = Reparto
    form_class = RepartoUpdateForm
    template_name = 'deed/reparto_update_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:reparto-detail', args=[self.object.id])


class NumeroEscrituraUpdateView(UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo reparto"""
    model = Reparto
    form_class = NumeroEscrituraUpdateForm
    template_name = 'deed/num_escritura_update_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:reparto-update', args=[self.object.id])


class RepartoListView(ListView):
    """Gestiona la lista de hojas de ruta"""
    model=Reparto
    
    def get_queryset(self):
        """Se crea un filtro para que se muestren solo los repartos activos"""
        qs = super().get_queryset()
        return qs.filter(activo='True').order_by('-id')


class RepartoCreateView(CreateView):

    model = Reparto
    form_class = RepartoCreateForm
    template_name = 'deed/reparto_create_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:reparto-detail', args=[self.object.id])


class RepartoDetailView(DetailView):
    model = Reparto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inmueble'] = Inmueble.objects.filter(reparto=self.object.id)
        context['etapas'] = RepartoEtapa.objects.filter(reparto=self.object.id).order_by('orden')
        context['otorgantes'] = OtorganteReparto.objects.filter(reparto=self.object.id).order_by('otorgante')
        return context


#ACTOS JURIDICOS
class ActoCreateView(CreateView):

    model = ActoJuridico
    form_class = ActoCreateForm
    template_name = 'deed/acto_create_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:acto-list')


class ActoUpdateView(UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo ActoJuridico"""
    model = ActoJuridico
    form_class = ActoUpdateForm
    template_name = 'deed/acto_update_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:acto-list')

    
class ActoListView(ListView):
    """Gestiona la lista de actos jurídicos"""
    model=ActoJuridico


class ActoDeleteView(DeleteView):
    model = ActoJuridico
    success_url = reverse_lazy('deed:acto-list')


#IMUEBLES
class RepartoInmuebleEditView(SingleObjectMixin, FormView):

    model = Reparto
    template_name = 'deed/reparto_inmueble_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Reparto.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Reparto.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self):
        form_class = InmuebleInlineFormSet
        RepartoInmuebleFormSet = inlineformset_factory(
            Reparto, Inmueble, fields=('reparto', 'inmueble', 'matricula',),
            form=form_class, max_num=Inmueble.objects.filter(reparto=self.object).count()+1)
        return RepartoInmuebleFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('deed:reparto-inmueble-edit', args=[self.object.id])


#OTORGANTES
class RepartoOtorganteEditView(SingleObjectMixin, FormView):

    model = Reparto
    template_name = 'deed/reparto_otorgante_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Reparto.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Reparto.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self):
        form_class = RepartoOtorganteInlineFormSet
        RepartoOtorganteFormSet = inlineformset_factory(
            Reparto, OtorganteReparto, fields=(
                'otorgante',
                'factura',
                'derechos_notariales',
                'valor_registro',
                'valor_rentas',
                'canje',),
            form=form_class, max_num=OtorganteReparto.objects.filter(reparto=self.object).count()+1)
        return RepartoOtorganteFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('deed:reparto-otorgante-edit', args=[self.object.id])


#CONFIGURACIÓN DE ETAPAS
class RepartoEtapasEditView(SingleObjectMixin, FormView):

    model = Reparto
    template_name = 'deed/reparto_etapas_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Reparto.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Reparto.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self):
        form_class = RepartoEtapasInlineFormSet
        RepartoEtapasFormSet = inlineformset_factory(
            Reparto, RepartoEtapa, fields=(
                'tipo_repartoetapa',
                'grupo_repartoetapa',
                'etapa',
                'orden',
                'fecha_inicio',
                'fecha_final',
                'finalizado'),
            form=form_class, max_num=RepartoEtapa.objects.filter(reparto=self.object).count()+1)
        return RepartoEtapasFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('deed:reparto-etapas-edit', args=[self.object.id])
