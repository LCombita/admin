from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from .models import Etapa, RepartoEtapa, ObservacionEtapa, Revision, Impuesto
from .forms import EtapaCreateForm, EtapaUpdateForm, RepartoEtapaUpdateForm
from .forms import ObservacionInlineFormSet, RevisionInlineFormSet, ImpuestoInlineFormSet
from django.views.generic import DetailView, CreateView, UpdateView, ListView, FormView
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
        context['revision'] = Revision.objects.filter(reparto_etapa=self.object.id)
        context['impuesto'] = Impuesto.objects.filter(reparto_etapa=self.object.id)
        return context

    def get_success_url(self):
        return reverse_lazy('stage:repartoetapa-update', args=[self.object.id])


class RepartoEtapaDetailView(DetailView):
    model = RepartoEtapa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['observaciones'] = ObservacionEtapa.objects.filter(reparto_etapa=self.object.id)
        context['impuesto'] = Impuesto.objects.filter(reparto_etapa=self.object.id)
        context['revision'] = Revision.objects.filter(reparto_etapa=self.object.id)
        return context


#OBSERVACIONES REPARTO ETAPAS
class ObservacionesRepartoEtapaEditView(SingleObjectMixin, FormView):
    """Abre desde RepartoEtapaUpdate"""

    model = RepartoEtapa
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


class ObservacionesRepartoEtapa2EditView(SingleObjectMixin, FormView):
    """Abre desde RepartoEtapaDetail"""

    model = RepartoEtapa
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
        return reverse_lazy('stage:repartoetapa-detail', args=[self.object.id])


#REVISION EN ETAPAS
class RevisionRepartoEtapaEditView(SingleObjectMixin, FormView):

    model = RepartoEtapa
    template_name = 'stage/reparto-etapa_revision_edit.html'

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
class ImpuestoRepartoEtapaEditView(SingleObjectMixin, FormView):

    model = RepartoEtapa
    template_name = 'stage/reparto-etapa_impuesto_edit.html'

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

