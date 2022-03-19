from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from .models import Etapa, RepartoEtapa, ObservacionEtapa
from .forms import EtapaCreateForm, EtapaUpdateForm, RepartoEtapaUpdateForm, ObservacionInlineFormSet
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, FormView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory


class EtapaCreateView(CreateView):
    model = Etapa
    form_class = EtapaCreateForm
    template_name = 'stage/etapa_create_form.html'

    def get_success_url(self):
        return reverse_lazy('stage:etapa-list')


class EtapaListView(ListView):
    """Gestiona la lista proyectos"""
    model=Etapa


class EtapaDeleteView(DeleteView):
    model = Etapa
    success_url = reverse_lazy('stage:etapa-list')


class EtapaUpdateView(UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo cliente"""
    model = Etapa
    form_class = EtapaUpdateForm
    template_name = 'stage/etapa_update_form.html'

    def get_success_url(self):
        return reverse_lazy('stage:etapa-list')


class EtapaDeleteView(DeleteView):
    model = Etapa
    success_url = reverse_lazy('stage:etapa-list')


#REPARTO ETAPA
class RepartoEtapaUpdateView(UpdateView):
    model = RepartoEtapa
    form_class = RepartoEtapaUpdateForm
    template_name = 'stage/reparto-etapa_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['observaciones'] = ObservacionEtapa.objects.filter(reparto_etapa=self.object.id)
        return context

    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-update', args=[self.object.id])


#OBSERVACIONES REPARTO ETAPAS
class RepartoEtapaEditView(SingleObjectMixin, FormView):

    model = RepartoEtapa
    form_class = RepartoEtapaUpdateForm
    template_name = 'stage/reparto-etapa_observacion_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=RepartoEtapa.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=RepartoEtapa.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self):
        form_class = ObservacionInlineFormSet
        RepartoEtapaObservacionFormSet = inlineformset_factory(
            RepartoEtapa, ObservacionEtapa, fields=('observacion',),
            form=form_class, max_num=ObservacionEtapa.objects.filter(reparto_etapa=self.object).count()+1)
        return RepartoEtapaObservacionFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-update', args=[self.object.id])



