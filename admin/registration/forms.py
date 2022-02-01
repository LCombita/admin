from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  Grantor, DataGrantor


class CreateGrantorForm(UserCreationForm):

    class Meta:
        model = Grantor
        fields = [
            'username', 'email', 'password1', 'password2',
            'first_name', 'last_name', 'last_name2', 'identification']


class UpdateGrantorForm(UserChangeForm):

    class Meta:
        model = Grantor
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name', 'last_name2', 'identification']


class DataGrantorForm(forms.ModelForm):
    
    class Meta:
        model = DataGrantor
        fields = ['phone', 'address']
        widgets = {
            'phone':forms.TextInput(attrs={
                'class':'form-control mb-2', 'placeholder':'número de teléfono'}),
            'address':forms.TextInput(attrs={
                'class':'form-control mb-2', 'placeholder':'dirección'}),
        }

"""
labels = {
    'username': '', 'email': '', 'password': '',
    'first_name': '','last_name': '', 'last_name2': '', 'identification': ''
}
"""
"""
fields = '__all__'
fields = ['campo1', 'campo2']
exclude = ['campo1', 'campo2']
"""