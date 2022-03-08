from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from .models import Reparto, ActoJuridico
from .forms import RepartoUpdateForm, NumeroEscrituraUpdateForm, RepartoCreateForm
from .forms import ActoCreateForm, ActoUpdateForm
from django.urls import reverse_lazy

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