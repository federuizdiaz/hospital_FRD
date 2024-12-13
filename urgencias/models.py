from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    obra_social = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
