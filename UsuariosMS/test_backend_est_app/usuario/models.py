from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    auto = models.CharField(max_length=100)


    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.nombre
    

