from django import forms


class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    password = forms.CharField(max_length=12)
    email = forms.CharField(max_length=100)
    auto = forms.CharField(max_length=100)