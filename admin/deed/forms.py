from django import forms
from .models import Reparto

class RepartoUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proyecto'].widget.attrs.update({'class': 'form-control'})
        self.fields['acto_juridico'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_reparto'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['escritura'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})

    class Meta:
        model = Reparto
        fields = ['proyecto', 'acto_juridico', 'fecha_reparto', 'escritura',
                    'fecha_escritura', 'canje', 'activo']
        labels = {
            'escritura':'', 'fecha_escritura':'', 'fecha_reparto':'',
            'canje':'', 'activo':'', 'proyecto':'', 'acto_juridico':''
            }
        help_texts = {
            'proyecto': 'Seleccione el proyecto relacionado con el trámite.',
            'acto_juridico': 'Seleccione el acto relacionado. Si son varios, presion la tecla CTRL y seleccione los actos.',
            'fecha_escritura': 'Seleccione la fecha de la escritura.',
            'fecha_reparto': 'Seleccione la fecha de registro de la Hoja de Ruta.',
            'escritura': 'Digite el número de la escritura.',
            'canje': ' Active esta casilla si la factura de la constructora es para canje.',
            'activo': ' Active esta casilla si si es reparto se ha anulado.'
            }



        