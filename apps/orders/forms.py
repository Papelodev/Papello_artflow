from django import forms

class Art_quantity_forms(forms.Form):
    quantidade_artes = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'id': 'quantidade_artes'}))

    def __init__(self, *args, **kwargs):
        quantidade_produtos = kwargs.pop('quantidade_produtos')
        super(Art_quantity_forms, self).__init__(*args, **kwargs)
        self.fields['quantidade_artes'].choices = [(str(i), str(i)) for i in range(0, quantidade_produtos + 1)]