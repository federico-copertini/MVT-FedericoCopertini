from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30) #texto
    edad = models.PositiveSmallIntegerField()
    ROLES = (
        (1,"Madre"),
        (2,"Padre"),
        (3,"Hijo"),
        (4,"Hija"),
        (5,"Mascota")
    )
    rol =  models.PositiveSmallIntegerField(choices=ROLES)
    fecha_de_nacimiento = models.DateField()