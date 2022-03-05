from django import forms
from .models import Proyecto, Cliente

class ProyectoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs.update({'class': 'form-control'})
        self.fields['tramitador'].widget.attrs.update(
            {'class': 'form-control select2', 'data-placeholder':'Selecione los tramitadores'})
        self.fields['nombre_proyecto'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Proyecto
        fields = ['id', 'cliente', 'tramitador', 'nombre_proyecto']
        labels = {
            'cliente':'', 'tramitador':'', 'nombre_proyecto':''
            }
        help_texts = {
            'cliente': 'Seleccione el cliente relacionado con el trámite.',
            'tramitador': 'Seleccione tramitador de proyecto.',
            'nombre_proyecto': 'Introduzca el nombre del proyecto.'
            }


class ClienteCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_cliente'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Cliente
        fields = ['id', 'nombre_cliente']
        labels = {'nombre_cliente':''}
        help_texts = {'nombre_cliente': 'Introduzca el nombre del cliente corporativo.'}


class ClienteUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_cliente'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Cliente
        fields = ['id', 'nombre_cliente']
        labels = {'nombre_cliente':''}
        help_texts = {'nombre_cliente': 'Introduzca el nombre del cliente corporativo.'}