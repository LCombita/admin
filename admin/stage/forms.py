from django import forms
from .models import Etapa


class EtapaCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_etapa'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre_etapa'].widget.attrs.update({'class': 'form-control'})
        self.fields['activo'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Etapa
        fields = ['id', 'tipo_etapa', 'nombre_etapa', 'activo']
        labels = {'tipo_etapa':'', 'nombre_etapa':'', 'activo':''}
        help_texts = {
            'tipo_etapa': 'Seleccione el tipo de etapa.',
            'nombre_etapa': 'Introduzca el nombre de la etapa.',
            'activo': 'Etapa activa.'
            }


class EtapaUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_etapa'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre_etapa'].widget.attrs.update({'class': 'form-control'})
        self.fields['activo'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Etapa
        fields = ['id', 'tipo_etapa', 'nombre_etapa', 'activo']
        labels = {'tipo_etapa':'', 'nombre_etapa':'', 'activo':''}
        help_texts = {
            'tipo_etapa': 'Seleccione el tipo de etapa.',
            'nombre_etapa': 'Introduzca el nombre de la etapa.',
            'activo': 'Etapa activa.'
            }
