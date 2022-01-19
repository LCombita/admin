from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
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
    list_display = ('email', 'first_name', 'last_name2')
    list_filter = ('is_staff','is_active',)
    search_fields = ('first_name', 'email',)
    orderin = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)