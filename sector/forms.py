from django import forms
from .models import Sector, Banner

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do Setor', 'class': 'form-control-home text-color-default w-full'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descrição do Setor', 
                'class': 'form-control-home text-color-default w-full', 
                'rows': 2, 
                'cols': 40, 
                'maxlength': 500
            }),
        }
        error_messages = {
            'name': {
                'required': "O campo Nome do Setor é obrigatório.",
            },
            'description': {
                'required': "O campo Descrição do Setor é obrigatório.",
            },
        }

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Nome do Banner', 'class': 'form-control-home text-color-default w-full'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descrição do Banner', 
                'class': 'form-control-home w-full text-color-default', 
                'rows': 2, 
                'cols': 40, 
                'maxlength': 500
            }),
            'image': forms.FileInput(attrs={'class': 'form-control-home text-color-default w-full'})
        }
        error_messages = {
            'name': {
                'required': "O campo Nome do Banner é obrigatório.",
            },
            'description': {
                'required': "O campo Descrição do Banner é obrigatório.",
            },
            'image': {
                'required': "O campo de imagem do Banner é obrigatório.",
            },
        }
