from django import forms
from .models import Reparto

class RepartoUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proyecto'].widget.attrs.update({'class': 'form-control'})
        self.fields['acto_juridico'].widget.attrs.update(
            {'class': 'form-control select2', 'data-placeholder':'Selecione los actos jurídicos.'})
        self.fields['fecha_reparto'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['escritura'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        #self.fields['canje'].widget.attrs.update({'class':'icheck-danger'})
        #self.fields['activo'].widget.attrs.update({'class':'icheck-primary d-inline'})

    class Meta:
        model = Reparto
        fields = ['proyecto', 'acto_juridico', 'fecha_reparto', 'escritura',
                    'fecha_escritura', 'activo']
        labels = {
            'escritura':'', 'fecha_escritura':'', 'fecha_reparto':'',
            'activo':'', 'proyecto':'', 'acto_juridico':''
            }
        help_texts = {
            'proyecto': 'Seleccione el proyecto relacionado con el trámite.',
            'acto_juridico': 'Seleccione el acto relacionado. Si son varios, presion la tecla CTRL y seleccione los actos.',
            'fecha_escritura': 'Seleccione la fecha de la escritura.',
            'fecha_reparto': 'Seleccione la fecha de registro de la Hoja de Ruta.',
            'escritura': 'Digite el número de la escritura.',
            'activo': ' Activo. Desmarque esta opción si se anula el reparto.'
            }



        