from django import forms

class ReportRepartoXOtorganteForm(forms.Form):

    identificacion = forms.CharField(label="Identificación", max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control'}
        ))