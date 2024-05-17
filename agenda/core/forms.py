from django import forms
from django.core.exceptions import ValidationError


class AgendaForm(forms.Form):
    nome = forms.CharField(max_length=150)
    cpf = forms.CharField(max_length=30)
    telefone = forms.CharField(max_length=20)
        
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if telefone.startswith('19') or telefone.startswith('16'):
            return telefone
        raise ValidationError('Apenas DDD 16 ou 19 são válidos')
    
    #validacao do cpf
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) == 11:
            return cpf
        raise ValidationError('O CPF deve conter 11 caracteres')
