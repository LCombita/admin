from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from .models import Reparto
from .forms import RepartoUpdateForm
from django.urls import reverse_lazy

class RepartoUpdateView(UpdateView):
    model = Reparto
    form_class = RepartoUpdateForm
    template_name = 'deed/reparto_update_form.html'

    def get_success_url(self):
        return reverse_lazy('deed:reparto-update', args=[self.object.id])

