from django.views.generic import CreateView, UpdateView, ListView, FormView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeleteView
from .models import Reparto, ActoJuridico
from .forms import RepartoUpdateForm, NumeroEscrituraUpdateForm, RepartoCreateForm
from .forms import ActoCreateForm, ActoUpdateForm
from .forms import RepartoInmuebleFormSet
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class RepartoUpdateView(UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo reparto"""
    model = Reparto
    form_class = RepartoUpdateForm
    template_name = 'deed/reparto_update_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:reparto-update', args=[self.object.id])


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
        return reverse_lazy('deed:reparto-update', args=[self.object.id])

class RepartoDetailView(DetailView):
    model = Reparto


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

    def get_form(self, form_class=None):
        return RepartoInmuebleFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        #messages.add_message(
        #    self.request,
        #    messages.SUCCESS,
        #    'Changes were saved.'
        #)
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('deed:reparto-inmueble-edit', args=[self.object.id])