from django.urls import reverse_lazy
from .models import Etapa  
from .forms import EtapaCreateForm, EtapaUpdateForm
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.views.generic.edit import DeleteView


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



