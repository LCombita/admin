from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import  Grantor


class CreateGrantorForm(UserCreationForm):
    
    class Meta:
        model = Grantor
        fields = [
            'username', 'email', 'password1', 'password2',
            'first_name', 'last_name', 'last_name2', 'identification']



"""
fields = '__all__'
fields = ['campo1', 'campo2']
exclude = ['campo1', 'campo2']
"""