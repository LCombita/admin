from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Grantor, Administrador, Autenticaciones, Ciudadano, Declaraciones
from .models import Escrituracion, Facturacion, Finalizacion, Juridica, RepartoUser, Tramitador
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    """personaliza el admin del usuario, insertando en el formulario los campos
    agregados apara personalizar el modelo User"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2','es_administrador')
    list_filter = ('is_staff','is_active',)
    search_fields = ('first_name', 'email',)
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions',)


class AdministradorAdmin(BaseUserAdmin):
    """personaliza el admin de proximodel Administrador"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'administrador'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='administrador')


class AutenticacionesAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Autenticaciones"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'autenticaciones'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='autenticaciones')


class CiudadanoAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Ciudadano"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'ciudadano'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='ciudadano')


class DeclaracionesAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Declaraciones"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'declaraciones'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='declaraciones')


class EscrituracionAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Escrituracion"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'escrituracion'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='escrituracion')


class FacturacionAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Facaturacion"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'facturacion'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='facturacion')


class FinalizacionAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Finalizacion"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'finalizacion'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='finalizacion')


class JuridicaAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Juridica"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'juridica'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='juridica')


class GrantorAdmin(BaseUserAdmin):
    """personaliza el admin de otorgantes, insertando en el formulario los campos
    agregados para personalizar el modelo"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'otorgante'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='otorgante')


class RepartoUserAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel RepartoUser"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'reparto'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='reparto')


class TramitadorAdmin(BaseUserAdmin):
    """personaliza el admin del proximodel Tramitador"""
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ( ('Información Personal'), {'fields': ('first_name', 'last_name', 'last_name2','identification')}),
        ( ('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ( ('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide'),
            'fields':('username', 'email', 'password1', 'password2')
         }),
    )
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'tramitador'"""
        qs = super().get_queryset(request)
        return qs.filter(groups__name='tramitador')


admin.site.register(User, UserAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Autenticaciones, AutenticacionesAdmin)
admin.site.register(Ciudadano, CiudadanoAdmin)
admin.site.register(Declaraciones, DeclaracionesAdmin)
admin.site.register(Escrituracion, EscrituracionAdmin)
admin.site.register(Facturacion, FacturacionAdmin)
admin.site.register(Finalizacion, FinalizacionAdmin)
admin.site.register(Juridica, JuridicaAdmin)
admin.site.register(Grantor, GrantorAdmin)
admin.site.register(RepartoUser, RepartoUserAdmin)
admin.site.register(Tramitador, TramitadorAdmin)



