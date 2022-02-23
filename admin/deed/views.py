from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from .models import Reparto
from .forms import RepartoUpdateForm
from django.urls import reverse_lazy

class RepartoUpdateView(UpdateView):
    """Gestiona el formulario para actualizar los datos del modelo reparto"""
    model = Reparto
    form_class = RepartoUpdateForm
    template_name = 'deed/reparto_update_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:reparto-update', args=[self.object.id])
    #TODO: validar que no se repita anio_escritura


class RepartoListView(ListView):
    """Gestiona la lista de hojas de ruta"""
    model=Reparto
    
    def get_queryset(self):
        """Se crea un filtro para que se muestren solo los repartos activos"""
        qs = super().get_queryset()
        print("desde GrantorAdmin, el qs", qs)
        return qs.filter(activo='True')