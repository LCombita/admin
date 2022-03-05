from django.urls import reverse_lazy
from .models import Proyecto, Cliente   
from .forms import ProyectoCreateForm
from .forms import ClienteCreateForm, ClienteUpdateForm
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

# PROYECTO
class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoCreateForm
    template_name = 'project/proyecto_create_form.html'

    def get_success_url(self):
        return reverse_lazy('project:proyecto-list')


class ProyectoListView(ListView):
    """Gestiona la lista proyectos"""
    model=Proyecto


# CLIENTE
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteCreateForm
    template_name = 'project/cliente_create_form.html'

    def get_success_url(self):
        return reverse_lazy('project:cliente-list')


class ClienteListView(ListView):
    """Gestiona la lista proyectos"""
    model=Cliente


class ClienteUpdateView(UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo cliente"""
    model = Cliente
    form_class = ClienteUpdateForm
    template_name = 'project/cliente_update_form.html'

    def get_success_url(self):
        return reverse_lazy('project:cliente-list')