from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LoginPageView(TemplateView):
    template_name = 'registration/login.html'


class HomePageView(TemplateView):
    template_name = 'registration/base.html'
