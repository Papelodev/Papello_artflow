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
        exclude = ['idCustomer', 'idOrder', 'status', 'idProduct', 'designer_responsible','orderProduct','rejection_reason', 'mockup', 'alteracounter', 'alterafiles', 'artefinal', 'alteracoes', 'date']
        labels ={
            'referencefiles': 'Envie aqui todo tipo de referência de mídia  para a confecção da arte do produto',
            'instructions': '',
        }

        widgets = {
            'instructions':forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Envie aqui todo tipo de referência de mídia  para a confecção da arte...'}),
            'referencefiles':forms.FileInput(attrs={'class':'form-control'}),
        }

class PrototipoForms(forms.ModelForm):
    class Meta:
        model = Arte
        exclude = ['idCustomer', 'idOrder', 'idProduct','designer_responsible', 'alteracounter','orderProduct','rejection_reason', 'alterafiles', 'artefinal', 'alteracoes', 'referencefiles', 'instructions', 'date', 'status']
        labels ={
            'mockup':'Envie aqui o protótipo pronto.',
        }
        widgets = {
            'mockup':forms.FileInput(attrs={'class':'form-control', 'style':'width: 50%;'}),
        }

class AlteracaoForms(forms.ModelForm):
    class Meta:
        model = Arte
        exclude = ['idCustomer', 'idOrder', 'idProduct', 'orderProduct','designer_responsible','rejection_reason', 'alteracounter', 'mockup', 'artefinal', 'referencefiles', 'instructions', 'date', 'status']
        labels ={
            'alterafiles':'Envie aqui todo tipo de referência de mídia  para a alteracão da arte do produto.',
            'alteracoes':'Explique aqui o que você deseja alterar no protótipo'
        }
        widgets = {
            'alterafiles':forms.FileInput(attrs={'class':'form-control', 'style':'width: 50%;'}),
            'alteracoes': forms.Textarea(attrs={'class': 'form-control text-area' })
        }

class rejectionReviewerForm(forms.ModelForm):
    class Meta:
        model = Arte
        exclude = ['idCustomer', 'idOrder', 'idProduct','alterafiles','orderProduct','designer_responsible', 'alteracoes', 'alteracounter', 'mockup', 'artefinal', 'referencefiles', 'instructions', 'date', 'status']
        labels ={
            'rejection_reason':'Envie aqui o motivo da reprovação.',
        }
        widgets = {
            'rejection_reason':forms.Textarea(attrs={'class':'form-control text-area', 'style':'width: 100%; display: none', 'placeholder': 'Escreva aqui o motivo da reprovação...'}),
        }