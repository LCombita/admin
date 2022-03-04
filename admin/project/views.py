from django.urls import reverse_lazy
from .models import Proyecto
from .forms import ProyectoCreateForm
from django.views.generic import TemplateView, CreateView, UpdateView, ListView


class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoCreateForm
    template_name = 'project/proyecto_create_form.html'

    def get_success_url(self):
        return reverse_lazy('project:proyecto-create')


class ProyectoListView(ListView):
    """Gestiona la lista proyectos"""
    model=Proyecto
