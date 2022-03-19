from django import forms
from .models import Etapa, RepartoEtapa, ObservacionEtapa


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


class RepartoEtapaUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reparto'].widget.attrs.update(
            {'class': 'form-control', 'hidden':'True'})
        self.fields['etapa'].widget.attrs.update(
            {'class': 'form-control', 'hidden':'True'})
        self.fields['fecha_inicio'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['fecha_final'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})

    class Meta:
        model = RepartoEtapa
        fields = ['id', 'reparto', 'etapa', 'fecha_inicio', 'fecha_final']
        labels = {'reparto':'', 'etapa':'', 'fecha_inicio':'', 'fecha_final':''}
        help_texts = {
            'reparto': 'Hoja de ruta.',
            'etapa': 'Etapa.',
            'fecha_inicio': 'Seleccione la fecha de inicio.',
            'fecha_final': 'Seleccione la fecha final.',
            }


class ObservacionInlineFormSet(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ObservacionEtapa
        fields = ['id', 'observacion']
        labels = {'observacion':''}
        help_texts = { 'observacion': 'Introduzca observaciones.', }