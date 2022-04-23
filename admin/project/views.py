from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Proyecto, Cliente   
from .forms import ProyectoCreateForm, ProyectoUpdateForm
from .forms import ClienteCreateForm, ClienteUpdateForm
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from registration.mixin import CheckAdmRepEscMixin

"""Las lineas @method_decorator(login_required, name='dispatch'), se utlizan para que vista
solo sea gestionada por un usuario que haya iniciado sesión en el sistema.
Las clases *Mixin se heredan para controlar que la vista la pueda ejecutar un usuario 
que pertenece a un grupo específico."""


# PROYECTO; gestión de proyectos inmobiliarios
@method_decorator(login_required, name='dispatch')
class ProyectoCreateView(CheckAdmRepEscMixin, CreateView):
    """Gestiona el formulario para crear proyectos (proyectos inmobiliarios asociados a una constructura)
    nuevos. Esta vista solo la pueden ejecutar los usuarios que pertenecen a los grupos adminitrador,
    reparto y escrituracion. La restricción la controla la CheckAdmRepEscMixin"""

    model = Proyecto
    form_class = ProyectoCreateForm
    template_name = 'project/proyecto_create_form.html'

    def get_success_url(self):
        return reverse_lazy('project:proyecto-list')


@method_decorator(login_required, name='dispatch')
class ProyectoListView(CheckAdmRepEscMixin, ListView):
    """Gestiona un listado de proyectos activos, a través del template proyecto_list.html.
    Esta vista la pueden ejecutar los usuarios de los grupos administrador, reparto y
    escrituracion, la restriccion es controlada por la CheckAdmRepEscMixin."""

    model=Proyecto


@method_decorator(login_required, name='dispatch')
class ProyectoDeleteView(CheckAdmRepEscMixin, DeleteView):
    """Gestiona la eliminación de un un proyecto utilizando el template proyecto_list.html
    para la confirmación, recibe el id como paramétro en la url. Esta vista la pueden ejecutar
    los usuarios de los grupos administrador, reparto y escrituracion, la restriccion
    es controlada por la CheckAdmRepEscMixin."""
    
    model = Proyecto
    success_url = reverse_lazy('project:proyecto-list')


@method_decorator(login_required, name='dispatch')
class ProyectoUpdateView(CheckAdmRepEscMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo Poryecto, recibiendo
    el id como paramétro en la url. Esta vista solo la pueden ejecutar los usuarios de los
    grupos administrador, reparto y escrituracion, la restricción la
    controla la CheckAdmRepEscMixin."""
    
    model = Proyecto
    form_class = ProyectoUpdateForm
    template_name = 'project/proyecto_update_form.html'

    def get_success_url(self):
        return reverse_lazy('project:proyecto-list')


# CLIENTE; contruuctor u oficina de abogados que gestionan grandes volúmenes de escrituración
@method_decorator(login_required, name='dispatch')
class ClienteCreateView(CheckAdmRepEscMixin, CreateView):
    """Gestiona el formulario para crear clientes nuevos. Esta vista solo la pueden
    ejecutar los usuarios que pertenecen a los grupos adminitrador, reparto y
    escrituracion. La restricción la controla la CheckAdmRepEscMixin"""

    model = Cliente
    form_class = ClienteCreateForm
    template_name = 'project/cliente_create_form.html'

    def get_success_url(self):
        return reverse_lazy('project:cliente-list')


@method_decorator(login_required, name='dispatch')
class ClienteListView(CheckAdmRepEscMixin, ListView):
    """Gestiona un listado de clientes activos, a través del template cliente_list.html.
    Esta vista la pueden ejecutar los usuarios de los grupos administrador, reparto y
    escrituracion, la restriccion es controlada por la CheckAdmRepEscMixin."""

    model=Cliente


@method_decorator(login_required, name='dispatch')
class ClienteUpdateView(CheckAdmRepEscMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo Cliente, recibiendo
    el id del cliente como paramétro por la url. Esta vista solo la pueden ejecutar los usuarios de los
    grupos administrador, reparto y escrituracion, la restricción la  controla la
    CheckAdmRepEscMixin."""

    model = Cliente
    form_class = ClienteUpdateForm
    template_name = 'project/cliente_update_form.html'

    def get_success_url(self):
        return reverse_lazy('project:cliente-list')


@method_decorator(login_required, name='dispatch')
class ClienteDeleteView(CheckAdmRepEscMixin, DeleteView):
    """Gestiona la eliminación de un cliente utilizando el template proyecto_list.html
    para la confirmación y recibe el id como paramétro en la url. Esta vista la pueden
    ejecutar los usuarios de los grupos administrador, reparto y escrituracion,
    la restriccion es controlada por la CheckAdmRepEscMixin."""

    model = Cliente
    success_url = reverse_lazy('project:cliente-list')

