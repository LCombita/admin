from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from .models import DataGrantor, Grantor
from .forms import CreateGrantorForm, DataGrantorForm

"""El login es gestionado por el sistema de autenticación predeterminado de django, para esta
funcionalidad solo se le pasó el template 'registration/login.html'. Para el logout, tambien se utiliza
el  predeterminado de django, en este caso solo se pasa la url 'logout' en el template base 'base.html'"""

class HomePageView(TemplateView):
    """procesa el template 'registration/home.html' que representa el inicio del proyecto AdmIN"""
    template_name = 'registration/home.html'


class CreateGrantorView(CreateView):
    """Gestiona el formulario para crear el otorgante.
    El métoro get_form modifica el formulario en tiempo de ejecución para no perder las validadicones
    ya que se está estendiento el formulario UserCreationForm predeterminado de django"""
    model = Grantor
    form_class = CreateGrantorForm
    template_name = 'registration/create_grantor_form.html'

    def get_form(self, form_class=None):
        form = super(CreateGrantorView, self).get_form()
        form.fields['username'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'nombre de usuario'})
        form.fields['email'].widget =forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'correo electrónico'})   
        form.fields['password1'].widget =forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'contraseña'})
        form.fields['password2'].widget =forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'confirme la contraseña'})
        form.fields['first_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'primer nombre'})
        form.fields['last_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'primer apellido'})
        form.fields['last_name2'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'segundo apellido'})
        form.fields['identification'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'número de identificación'})
        return form

    def get_success_url(self):
        #se define el paramétro para la actualización de los datos del otorgante
        return reverse_lazy('registration:data-grantor', args=[self.object.datagrantor.id])


class DataGrantorView(UpdateView):
    model = DataGrantor
    form_class = DataGrantorForm
    template_name = 'registration/datagrantor_form.html'
    success_url = reverse_lazy('registration:home')

    """
    template_name_suffix = '_update_form'
    def get_object(self):
        #recuperar el objete a editar
        datagrantor, create = DataGrantor.objects.get_or_create(user=self.request.user)
        return datagrantor
        """