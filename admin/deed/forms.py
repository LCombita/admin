from django import forms
from .models import Reparto

class RepartoUpdateForm(forms.ModelForm):

    class Meta:
        model = Reparto
        fields = ['id', 'proyecto', 'acto_juridico', 'fecha_reparto', 'escritura',
                    'fecha_escritura', 'canje', 'activo']
        widgets = {
            #'id':forms.NumberInput(attrs={'class':'form-control', 'hidden':'false'}),
            #'proyecto':forms.NumberInput(attrs={'class':'form-control', 'hidden':'false'}),
            'fecha_reparto':forms.DateInput(attrs={'class': 'form-control'}),
            'escritura':forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_escritura':forms.DateInput(attrs={'class': 'form-control'}),
            'canje':forms.CheckboxInput(attrs={'class': 'form-control'}),
            'activo':forms.CheckboxInput(attrs={'class': 'form-control'}),
            }
        labels = {
            'escritura':''
            }
