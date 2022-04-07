from tkinter import Widget
from django import forms
from .models import Etapa, Impuesto, RepartoEtapa, ObservacionEtapa, Revision


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
        self.fields['tipo_repartoetapa'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['reparto'].widget.attrs.update(
            {'class': 'form-control', 'hidden':'True'})
        self.fields['etapa'].widget.attrs.update(
            {'class': 'form-control', 'hidden':'True'})
        self.fields['fecha_inicio'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['fecha_final'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['finalizado'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = RepartoEtapa
        fields = ['id',
            'reparto',
            'etapa',
            'fecha_inicio',
            'fecha_final',
            'finalizado',
            'tipo_repartoetapa',]
        labels = {'reparto':'',
            'etapa':'',
            'fecha_inicio':'',
            'fecha_final':'',
            'finalizado':'',
            'tipo_repartoetapa':'',}
        help_texts = {
            'reparto': 'Hoja de ruta.',
            'etapa': 'Etapa.',
            'fecha_inicio': 'Seleccione la fecha de inicio.',
            'fecha_final': 'Seleccione la fecha final.',
            'finalizado': 'Seleccione si finalizó la etapa.',
            'tipo_repartoetapa': 'Seleccione el tipo de etapa.',
            }


class ObservacionInlineFormSet(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ObservacionEtapa
        fields = ['id', 'observacion']
        labels = {'observacion':'',}
        help_texts = {
            'observacion': 'Verifique la información que se va a introducir, ya que no se puede modificar o eliminar.',
         }


class RepartoEtapaObservacionesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ObservacionEtapa
        fields = ['id', 'observacion']
        labels = {'observacion':'',}
        help_texts = {
            'observacion': 'Verifique la información que se va a introducir, ya que no se puede modificar o eliminar.',
         }


class RevisionInlineFormSet(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_revision'].widget.attrs.update({'class': 'form-control'})
        self.fields['reproceso'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Revision
        fields = [
            'id',
            'fecha_revision',
            'reproceso',
            'descripcion']
        labels = {
            'fecha_revision':'',
            'reproceso':'',
            'descripcion':'',}
        help_texts = {
            'fecha_revision': 'Seleccione la fecha en que hizo la revisión.',
            'reproceso': 'Seleccion esta obción si encontró errores en la revisión.',
            'descripcion': 'Describa los hallazgos econtrados.',
         }


class ImpuestoInlineFormSet(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reparto_etapa'].widget.attrs.update({'class': 'form-control'})
        self.fields['boleta_rentas'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_boleta_rentas'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_boleta_rentas'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['boleta_registro'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_boleta_registro'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_boleta_registro'].widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = Impuesto
        fields = [
            'id',
            'reparto_etapa',
            'boleta_rentas',
            'fecha_boleta_rentas',
            'file_boleta_rentas',
            'boleta_registro',
            'fecha_boleta_registro',
            'file_boleta_registro']
        labels = {
            'reparto_etapa':'',
            'boleta_rentas':'',
            'fecha_boleta_rentas':'',
            'file_boleta_rentas':'',
            'boleta_registro':'',
            'fecha_boleta_registro':'',
            'file_boleta_registro':'',}
        #widgets= {
        #    'file_boleta_rentas':forms.FileInput(attrs={'class':'form-control-file'}),
        #    'file_boleta_registro':forms.FileInput(attrs={'class':'form-control-file'}),
        # }
        help_texts = {
            'boleta_rentas':'rentas',
            'fecha_boleta_rentas':'rentas',
            'file_boleta_rentas':'rentas',
            'boleta_registro':'registro',
            'fecha_boleta_registro':'registro',
            'file_boleta_registro':'registro',
         }



