from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CheckAdmRepEscAutMixin(object):
    def dispatch(self, request, *args, **kwargs):
        grps = [
            'administrador',
            'reparto',
            'escrituracion',
            'autenticaciones']
        if user_in_groups(self.request.user, grps):
            return super(CheckAdmRepEscAutMixin, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))


class CheckAdmRepMixin(object):
    def dispatch(self, request, *args, **kwargs):
        grps = [
            'administrador',
            'reparto']
        if user_in_groups(self.request.user, grps):
            return super(CheckAdmRepMixin, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))


class CheckTraMixin(object):
    def dispatch(self, request, *args, **kwargs):
        grps = ['tramitador']
        if user_in_groups(self.request.user, grps):
            return super(CheckTraMixin, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))


class CheckAdmRepEscJurFinFacTraMixin(object):
    def dispatch(self, request, *args, **kwargs):
        grps = [
            'administrador',
            'reparto',
            'escrituracion',
            'juridica',
            'finalizacion',
            'facturacion']
        if user_in_groups(self.request.user, grps):
            return super(CheckTraMixin, self).dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('registration:no-permiso'))


#FUNCIONES GENERALES
def user_in_groups(user, list_groups):
    """Validar sin un usuario pertenece a uno o más grupos, con el fin
    de establecer restricciones con respecto a los permisos de cada grupo"""
    
    return True if user.groups.filter(name__in=list_groups) else False