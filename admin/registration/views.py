from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django import forms
from .models import DataGrantor, Grantor, Tramitador, Escrituracion
from .forms import CreateGrantorForm, DataGrantorForm, UpdateGrantorForm
from .forms import CreateTramitadorForm, UpdateTramitadorForm
from .forms import CreateEscrituracionForm, UpdateEscrituracionForm
from .mixin import CheckAdmRepMixin, CheckAdmRepEscAutMixin


"""El login es gestionado por el sistema de autenticación predeterminado de django, para esta
funcionalidad solo se le pasó el template 'registration/login.html'. Para el logout, tambien se utiliza
el  predeterminado de django, en este caso solo se pasa la url 'logout' en el template base 'base.html'"""

class HomePageView(TemplateView):
    """Gestiona el template 'registration/home.html' que representa el inicio del proyecto AdmIN"""

    template_name = 'registration/home.html'


@method_decorator(login_required, name='dispatch')
class NoPermisoPageView(TemplateView):
    """Gestiona el template 'registration/no_permiso.html' para redireccionar a los usuarios que
    intentan ejecutar una vista a la que no tienen permiso."""

    template_name = 'registration/no_permiso.html'


@method_decorator(login_required, name='dispatch')
class CreateGrantorView(CheckAdmRepEscAutMixin, CreateView):
    """Gestiona el formulario para crear el otorgante.
    El método get_form modifica el formulario en tiempo de ejecución para no perder las validadicones
    ya que se está extendiendo el formulario UserCreationForm predeterminado de django. La vista
    solo la pueden ejecutar los usuarios que pertenecen al grupo administrador, reparto,
    escrituracion y autenticaciones."""

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


@method_decorator(login_required, name='dispatch')
class UpdateGrantorView(CheckAdmRepEscAutMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos del otorgante.
    El método get_form modifica el formulario en tiempo de ejecución para no perder las validadicones
    ya que se está extendiendo el formulario UserCreationForm predeterminado de django. La vista
    solo la pueden ejecutar los usuarios que pertenecen al grupo administrador, reparto,
    escrituracion y autenticaciones."""

    model = Grantor
    form_class = UpdateGrantorForm 
    template_name = 'registration/update_grantor_form.html'

    def get_form(self, form_class=None):
        form = super(UpdateGrantorView, self).get_form()
        form.fields['username'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})
        form.fields['email'].widget =forms.EmailInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})   
        form.fields['password'].widget =forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})
        form.fields['first_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['last_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['last_name2'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['identification'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        return form

    def get_success_url(self):
        #se define el paramétro para la actualización de los datos del otorgante
        return reverse_lazy('registration:data-grantor', args=[self.object.datagrantor.id])


@method_decorator(login_required, name='dispatch')
class DataGrantorView(CheckAdmRepEscAutMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos complementarios del otorgante. Al crear un 
    otorgante, automáticamente se crea una instancia del modelo DataGrantor, en el cual se almacena
    la información complementaria de los otorgantes. La vista solo la pueden ejecutar los usuarios que
    pertenecen al grupo administrador, reparto, escrituracion y autenticaciones."""    

    model = DataGrantor
    form_class = DataGrantorForm
    template_name = 'registration/datagrantor_form.html'
    success_url = reverse_lazy('registration:grantor-list')


#TODO: pendiente agregas las otras columnas al template
@method_decorator(login_required, name='dispatch')
class GrantorListView(CheckAdmRepEscAutMixin, ListView):
    """Gestiona una lista de los usuarios que pertenecen al grupo otorgante, utilizando el template
    grantor_list.html. La vista solo la pueden ejecutar los usuarios que pertenecen al grupo
    administrador, reparto, escrituracion y autenticaciones."""
    
    model = Grantor
    
    def get_queryset(self):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'otorgante'"""
        qs = super().get_queryset()
        print("desde GrantorAdmin, el qs", qs)
        return qs.filter(groups__name='otorgante')


#TRAMITADORES
@method_decorator(login_required, name='dispatch')
class CreateTramitadorView(CheckAdmRepEscAutMixin, CreateView):
    """Gestiona el formulario para crear tramitadores.
    El método get_form modifica el formulario en tiempo de ejecución para no perder las validadicones
    ya que se está extendiendo el formulario UserCreationForm predeterminado de django. La vista
    solo la pueden ejecutar los usuarios que pertenecen al grupo administrador, reparto,
    escrituracion y autenticaciones."""

    model = Tramitador
    form_class = CreateTramitadorForm
    template_name = 'registration/create_tramitador_form.html'

    def get_form(self, form_class=None):
        form = super(CreateTramitadorView, self).get_form()
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
        return reverse_lazy('registration:tramitador-list')


@method_decorator(login_required, name='dispatch')
class TramitadorListView(CheckAdmRepEscAutMixin, ListView):
    """Gestiona una lista de los usuarios que pertenecen al grupo tramitador, utilizando el template
    tramitador_list.html. La vista solo la pueden ejecutar los usuarios que pertenecen al grupo
    administrador, reparto, escrituracion y autenticaciones."""

    model = Tramitador
    
    def get_queryset(self):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'tramitador'"""
        qs = super().get_queryset()
        return qs.filter(groups__name='tramitador')


@method_decorator(login_required, name='dispatch')
class UpdateTramitadorView(CheckAdmRepEscAutMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos del tramitador.
    El método get_form modifica el formulario en tiempo de ejecución para no perder las validadicones
    ya que se está extendiendo el formulario UserCreationForm predeterminado de django. La vista
    solo la pueden ejecutar los usuarios que pertenecen al grupo administrador, reparto,
    escrituracion y autenticaciones."""

    model = Tramitador
    form_class = UpdateTramitadorForm 
    template_name = 'registration/update_tramitador_form.html'

    def get_form(self, form_class=None):
        form = super(UpdateTramitadorView, self).get_form()
        form.fields['username'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})
        form.fields['email'].widget =forms.EmailInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})   
        form.fields['password'].widget =forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})
        form.fields['first_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['last_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['last_name2'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['identification'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        return form

    def get_success_url(self):
        #se define el paramétro para la actualización de los datos del otorgante
        return reverse_lazy('registration:update-tramitador', args=[self.object.id])


#ASISTENTES DE ESCRITURACION
@method_decorator(login_required, name='dispatch')
class CreateEscrituracionView(CheckAdmRepMixin, CreateView):
    """Gestiona el formulario para crear asistentes de escrituración.
    El método get_form modifica el formulario en tiempo de ejecución para no perder las validadicones
    ya que se está extendiendo el formulario UserCreationForm predeterminado de django. La vista
    solo la pueden ejecutar los usuarios que pertenecen al grupo administrador y reparto."""

    model = Escrituracion
    form_class = CreateEscrituracionForm
    template_name = 'registration/create_escrituracion_form.html'

    def get_form(self, form_class=None):
        form = super(CreateEscrituracionView, self).get_form()
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
        return reverse_lazy('registration:escrituracion-list')


@method_decorator(login_required, name='dispatch')
class EscrituracionListView(CheckAdmRepMixin, ListView):
    """Gestiona una lista de los usuarios que pertenecen al grupo escrituracion, utilizando el template
    escrituracion_list.html. La vista solo la pueden ejecutar los usuarios que pertenecen al grupo
    administrador y reparto."""

    model = Escrituracion
    
    def get_queryset(self):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'tramitador'"""
        qs = super().get_queryset()
        return qs.filter(groups__name='escrituracion')


@method_decorator(login_required, name='dispatch')
class UpdateEscrituracionView(CheckAdmRepMixin, UpdateView):
    """Gestiona el formulario para actualizar los datos de un usuario del escrituracion.
    El método get_form modifica el formulario en tiempo de ejecución para no perder las validadicones
    ya que se está extendiendo el formulario UserCreationForm predeterminado de django. La vista
    solo la pueden ejecutar los usuarios que pertenecen al grupo administrador y reparto."""

    model = Escrituracion
    form_class = UpdateEscrituracionForm 
    template_name = 'registration/update_escrituracion_form.html'

    def get_form(self, form_class=None):
        form = super(UpdateEscrituracionView, self).get_form()
        form.fields['username'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})
        form.fields['email'].widget =forms.EmailInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})   
        form.fields['password'].widget =forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'readonly':'readonly'})
        form.fields['first_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['last_name'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['last_name2'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        form.fields['identification'].widget =forms.TextInput(
            attrs={'class':'form-control mb-2'})
        return form

    def get_success_url(self):
        #se define el paramétro para la actualización de los datos del otorgante
        return reverse_lazy('registration:update-escrituracion', args=[self.object.id])

