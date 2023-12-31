from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Servicios(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    descripcion = models.CharField(max_length=150, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'servicios'

    def __str__(self):
        return self.nombre