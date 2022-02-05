from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Grantor
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


class GrantorAdmin(BaseUserAdmin):
    """personaliza el admin de otorgantes, insertando en el formulario los campos
    agregados apara personalizar el modelo"""
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
    list_filter = ('is_staff','is_active')
    search_fields = ('first_name', 'email')
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_queryset(self, request):
        """Se crea un filtro para que se muesten los usuarios que tienen el grupo 'otorgante'"""
        qs = super().get_queryset(request)
        print("desde GrantorAdmin, el qs", qs)
        return qs.filter(groups__name='otorgante')

admin.site.register(User, UserAdmin)
admin.site.register(Grantor, GrantorAdmin)