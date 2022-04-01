from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ReportRepartoXOtorganteForm
from deed.models import Reparto
from registration.models import Grantor


class ReportRepartosXOtorganteView(TemplateView):
    
    template_name = 'reports/repartos_x_otorgante.html'

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        #if self.request.method == "POST":
            #id_form = ReportRepartoXOtorganteForm(data=self.request.POST)
            #if id_form.is_valid():
        identificacion = request.POST.get('identificacion', '')
        #identificacion = 1027845214
        context['repartos'] = Reparto.objects.filter(otorgantereparto__otorgante__identification = identificacion)
        context['otorgante'] = Grantor.objects.filter(identification = identificacion)
        context['form'] = ReportRepartoXOtorganteForm()
        print ("desde vista: ", identificacion)
        return context
        #else:
         #   context['form'] = ReportRepartoXOtorganteForm()
          #  return context
