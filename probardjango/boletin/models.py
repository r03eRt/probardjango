from __future__ import unicode_literals

from django.db import models


# Create your models here.


# Creamos el modelo Registrado con los tipos de datos
class Registrado(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    codigo_postal = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) # Solo se anade en el momento que se crea
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True) # Solo se actualiza cuando se edita



    def __unicode__(self):  # Python 3 __str__
        return self.email
