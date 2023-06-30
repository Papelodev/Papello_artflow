from django import forms
from apps.galeria.models import Fotografia, Arte

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels ={
            'descricao':'Descrição',
            'data_fotografia':'Data de registro',
            'usuario':'Usuário',
        }

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'legenda':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia':forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                    }
                ),
            'usuario':forms.Select(attrs={'class':'form-control'}),
        }

class ArteForms(forms.ModelForm):
    class Meta:
        model = Arte
        exclude = ['idCustomer', 'idOrder', 'status', 'idProduct', 'mockup', 'alteracounter', 'alterafiles', 'artefinal', 'alteracoes', 'date']
        labels ={
            'instructions':'Envie aqui todo tipo de referência de mídia  para a confecção da arte',
            'referencefiles': 'Envie aqui todo tipo de referência de mídia  para a confecção da arte do produto'
        }

        widgets = {
            'instructions':forms.Textarea(attrs={'class':'form-control'}),
            'referencefiles':forms.FileInput(attrs={'class':'form-control'}),
        }

class PrototipoForms(forms.ModelForm):
    class Meta:
        model = Arte
        exclude = ['idCustomer', 'idOrder', 'idProduct', 'alteracounter', 'alterafiles', 'artefinal', 'alteracoes', 'referencefiles', 'instructions', 'date', 'status']
        labels ={
            'mockup':'Envie aqui o protótipo pronto.',
        }
        widgets = {
            'mockup':forms.FileInput(attrs={'class':'form-control', 'style':'width: 50%;'}),
        }