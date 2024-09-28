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
        fields = ['title', 'description', 'image', 'align', 'justify', 'width', 'padding', 'size_title', 'size_description']
        widgets = {
            'size_title': forms.NumberInput(attrs={'class': 'form-control-home text-color-default w-full'}),
            'size_description': forms.NumberInput(attrs={'class': 'form-control-home text-color-default w-full'}),
            'width': forms.NumberInput(attrs={'class': 'form-control-home text-color-default w-full'}),
            'padding': forms.NumberInput(attrs={'placeholder': 'Espaçamento interno', 'class': 'form-control-home text-color-default w-full'}),
            'title': forms.TextInput(attrs={'placeholder': 'Nome do Banner', 'class': 'form-control-home text-color-default w-full'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descrição do Banner', 
                'class': 'form-control-home w-full text-color-default', 
                'rows': 2, 
                'cols': 40, 
                'maxlength': 500
            }),
            'image': forms.FileInput(attrs={'class': 'form-control-home text-color-default w-full'}), 
            'justify': forms.Select(attrs={'class': 'form-control-home text-color-default select-bg-gray w-full'}),
            'align': forms.Select(attrs={'class': 'form-control-home text-color-default select-bg-gray w-full'}),
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
