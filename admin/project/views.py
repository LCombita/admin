from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Proyecto, Cliente   
from .forms import ProyectoCreateForm, ProyectoUpdateForm
from .forms import ClienteCreateForm, ClienteUpdateForm
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from registration.mixin import CheckAdmRepEscMixin

# PROYECTO
@method_decorator(login_required, name='dispatch')
class ProyectoCreateView(CheckAdmRepEscMixin, CreateView):
    model = Proyecto
    form_class = ProyectoCreateForm
    template_name = 'project/proyecto_create_form.html'

    def get_success_url(self):
        return reverse_lazy('project:proyecto-list')


@method_decorator(login_required, name='dispatch')
class ProyectoListView(CheckAdmRepEscMixin, ListView):
    """Gestiona la lista proyectos"""
    model=Proyecto


@method_decorator(login_required, name='dispatch')
class ProyectoDeleteView(CheckAdmRepEscMixin, DeleteView):
    model = Proyecto
    success_url = reverse_lazy('project:proyecto-list')


@method_decorator(login_required, name='dispatch')
class ProyectoUpdateView(CheckAdmRepEscMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo cliente"""
    model = Proyecto
    form_class = ProyectoUpdateForm
    template_name = 'project/proyecto_update_form.html'

    def get_success_url(self):
        return reverse_lazy('project:proyecto-list')


# CLIENTE
@method_decorator(login_required, name='dispatch')
class ClienteCreateView(CheckAdmRepEscMixin, CreateView):
    model = Cliente
    form_class = ClienteCreateForm
    template_name = 'project/cliente_create_form.html'

    def get_success_url(self):
        return reverse_lazy('project:cliente-list')


@method_decorator(login_required, name='dispatch')
class ClienteListView(CheckAdmRepEscMixin, ListView):
    """Gestiona la lista proyectos"""
    model=Cliente


@method_decorator(login_required, name='dispatch')
class ClienteUpdateView(CheckAdmRepEscMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo cliente"""
    model = Cliente
    form_class = ClienteUpdateForm
    template_name = 'project/cliente_update_form.html'

    def get_success_url(self):
        return reverse_lazy('project:cliente-list')


@method_decorator(login_required, name='dispatch')
class ClienteDeleteView(CheckAdmRepEscMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('project:cliente-list')

