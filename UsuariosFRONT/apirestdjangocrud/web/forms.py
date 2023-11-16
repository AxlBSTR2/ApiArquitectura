from django import forms


class ServicioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    auto = forms.CharField(max_length=100)
   
