from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from .models import Reparto
from .forms import RepartoUpdateForm, NumeroEscrituraUpdateForm, RepartoCreateForm
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
    