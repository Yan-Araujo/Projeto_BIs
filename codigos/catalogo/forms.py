from django import forms
from catalogo.models import BiCard


class BiCardsForms(forms.ModelForm):
    class Meta:
        model = BiCard
        exclude = ['ativo']
        labels = {
            "name": "BI",
            "description": "Descrição",
            "url": "URL"
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "url": forms.TextInput(attrs={"class": "form-control"}),
        }
