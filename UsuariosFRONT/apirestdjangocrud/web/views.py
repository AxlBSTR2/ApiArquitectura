from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from rest_framework.utils import json
from .forms import ServicioForm
from django.shortcuts import render


# Create your views here.


def index(request):
    response = requests.get('http://44.210.223.7:8000/usuarios/').json()
    return render(request, 'web/index.html', {
        'response': response
    })


def post_servicio(request):
    url = "http://44.210.223.7:8000/usuarios/crear"
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        auto = form.cleaned_data.get("auto")

        print(nombre)
        print(password)
        print(email)
        print(auto)

        data = {'nombre': nombre, 'password': password, 'email': email, 'auto': auto}
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return render(request, 'web/form.html', {
            'response': response
        })
