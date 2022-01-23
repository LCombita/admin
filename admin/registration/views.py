from django.views.generic import TemplateView

"""El login es gestionado por el sistema de autenticación predeterminado de django, para esta
funcionalidad solo se le pasó el template 'registration/login.html'. Para el logout, tambien se utiliza
el  predeterminado de django, en este caso solo se pasa la url 'logout' en el template base 'base.html'"""

class HomePageView(TemplateView):
    """procesa el template 'registration/home.html' que representa el inicio del proyecto AdmIN"""
    template_name = 'registration/home.html'

    