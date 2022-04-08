from django import forms
from .models import Reparto, ActoJuridico, Inmueble, OtorganteReparto
from stage.models import RepartoEtapa
#from django.forms import inlineformset_factory

class RepartoUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hoja_ruta'].widget.attrs.update({'class': 'form-control', 'readonly':'True'})
        self.fields['anio_escritura'].widget.attrs.update({'class': 'form-control', 'readonly':'True'})
        self.fields['proyecto'].widget.attrs.update({'class': 'form-control'})
        self.fields['acto_juridico'].widget.attrs.update(
            {'class': 'form-control select2', 'data-placeholder':'Selecione los actos jurídicos.'})
        self.fields['fecha_reparto'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True', 'hidden':'True'})
        self.fields['fecha_escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['activo'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Reparto
        fields = ['id', 'hoja_ruta', 'anio_escritura', 'proyecto', 'acto_juridico',
         'fecha_reparto', 'escritura', 'fecha_escritura', 'activo']
        labels = {
            'escritura':'', 'fecha_escritura':'', 'fecha_reparto':'',
            'activo':'', 'proyecto':'', 'acto_juridico':'', 'hoja_ruta':'', 'anio_escritura':'' 
            }
        help_texts = {
            'proyecto': 'Seleccione el proyecto relacionado con el trámite.',
            'acto_juridico': 'Seleccione los actos relacionados.',
            'fecha_escritura': 'Fecha de la escritura.',
            'fecha_reparto': 'Seleccione la fecha de registro de la Hoja de Ruta.',
            'escritura': 'Número de la escritura.',
            'hoja_ruta': 'Hoja de Ruta.',
            'anio_escritura': 'Número de escritura.',
            'activo': ' Desmarque para anular el reparto.'
            }


class NumeroEscrituraUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hoja_ruta'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True','hidden':'True'})
        self.fields['anio_escritura'].widget.attrs.update({'class': 'form-control', 'readonly':'True'})
        self.fields['proyecto'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True', 'hidden':'True'})
        self.fields['acto_juridico'].widget.attrs.update(
            {'class': 'form-control select2', 'data-placeholder':'Selecione los actos jurídicos.',
                'readonly':'True', 'hidden':'True'})
        self.fields['fecha_reparto'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True', 'readonly':'True', 'hidden':'True'})
        self.fields['escritura'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['activo'].widget.attrs.update({'class': 'field-activo', 'readonly':'True', 'hidden':'True'})

    class Meta:
        model = Reparto
        fields = ['id', 'hoja_ruta', 'anio_escritura', 'proyecto', 'acto_juridico',
            'fecha_reparto', 'escritura', 'fecha_escritura', 'activo']
        labels = {
            'escritura':'', 'fecha_escritura':'', 'anio_escritura':'' 
            }
        help_texts = {
            'fecha_escritura': 'Seleccione la fecha de la escritura.',
            'escritura': 'Digite el número de la escritura.',
            'anio_escritura': 'Número de escritura.',
            }
 
    def clean(self):
        """Validar que el anio_escritura generado NO exista en la base de datos"""
        #TODO: pendiente poder actualizar la fecha de escritura
        cleaned_data = super().clean()
        fecha_escritura = cleaned_data.get("fecha_escritura")
        escritura = cleaned_data.get("escritura")
        if fecha_escritura and escritura:
            ae = fecha_escritura.strftime('%Y') + '-' + escritura
            if Reparto.objects.filter(anio_escritura=ae).exists():
                raise forms.ValidationError("La escritura ya existe, verifique el número y la fecha.")


class RepartoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hoja_ruta'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['anio_escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True', 'hidden':'True'})
        self.fields['protocolista'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['proyecto'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['acto_juridico'].widget.attrs.update(
            {'class': 'form-control select2', 'data-placeholder':'Selecione los actos jurídicos.'})
        self.fields['fecha_reparto'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True', 'readonly':'True'})
        self.fields['escritura'].widget.attrs.update({'class': 'form-control', 'hidden':'True'})
        self.fields['fecha_escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True', 'hidden':'True'})
        self.fields['activo'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Reparto
        fields = ['id', 'hoja_ruta', 'anio_escritura', 'proyecto', 'acto_juridico',
            'fecha_reparto', 'escritura', 'fecha_escritura', 'activo', 'protocolista']
        labels = {
            'escritura':'', 'fecha_escritura':'', 'fecha_reparto':'',
            'activo':'', 'proyecto':'', 'acto_juridico':'', 'hoja_ruta':'',
            'anio_escritura':'', 'procotolista':''
            }
        help_texts = {
            'proyecto': 'Seleccione el proyecto relacionado con el trámite.',
            'protocolista': 'Seleccione asistente de escrituración.',
            'acto_juridico': 'Seleccione los actos relacionados.',
            'fecha_escritura': 'Seleccione la fecha de la escritura.',
            'fecha_reparto': 'Seleccione la fecha de registro de la Hoja de Ruta.',
            'escritura': 'Digite el número de la escritura.',
            'hoja_ruta': 'Hoja de Ruta.',
            'anio_escritura': 'Número de escritura.',
            'activo': ' Activo.'
            }


#ACTOS JURIDICOS
class ActoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_acto'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ActoJuridico
        fields = ['id', 'nombre_acto']
        labels = { 'nombre_acto':''}
        help_texts = {'nombre_acto': 'Introduzca el nombre del acto jurídico.'}


class ActoUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_acto'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ActoJuridico
        fields = ['id', 'nombre_acto']
        labels = { 'nombre_acto':''}
        help_texts = {'nombre_acto': 'Introduzca el nombre del acto jurídico.'}


#INMUEBLES
class InmuebleInlineFormSet(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inmueble'].widget.attrs.update({'class': 'form-control'})
        self.fields['matricula'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Inmueble
        fields = ['inmueble', 'matricula']
        labels = {'inmueble':'', 'matricula':''}


#OTORGANTES
class RepartoOtorganteInlineFormSet(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['otorgante'].widget.attrs.update({'class': 'form-control'})
        self.fields['factura'].widget.attrs.update({'class': 'form-control'})
        self.fields['derechos_notariales'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor_registro'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor_rentas'].widget.attrs.update({'class': 'form-control'})
        self.fields['canje'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = OtorganteReparto
        fields = [
            'otorgante',
            'factura',
            'derechos_notariales',
            'valor_registro',
            'valor_rentas',
            'canje']
        labels = {
            'otorgante':'',
            'factura':'',
            'derechos_notariales':'',
            'valor_registro':'',
            'valor_rentas':'',
            'canje':''}


#ETAPAS
class RepartoEtapasInlineFormSet(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_repartoetapa'].widget.attrs.update({'class': 'form-control'})
        self.fields['grupo_repartoetapa'].widget.attrs.update({'class': 'form-control'})
        self.fields['etapa'].widget.attrs.update({'class': 'form-control', 'readonly':'True'})
        self.fields['orden'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_inicio'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_final'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = RepartoEtapa
        fields = [
            'tipo_repartoetapa',
            'grupo_repartoetapa',
            'etapa',
            'orden',
            'fecha_inicio',
            'fecha_final',
            'finalizado']
        labels = {
            'tipo_repartoetapa':'',
            'grupo_repartoetapa':'',
            'etapa':'',
            'orden':'',
            'fecha_inicio':'',
            'fecha_final':'',
            'finalizado':''}