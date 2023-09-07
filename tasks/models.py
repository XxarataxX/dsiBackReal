from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Create your models here.

class Tarea(models.Model):

    opciones = (
        (1, 'Pendiente'),
        (2, 'Completada'),
        (3, 'cancelada')
    )

    titulo = models.CharField(max_length=50)
    description = models.CharField(max_length=10)
    fecha_creacion = models.DateField(default=date.today)
    fecha_vencimiento = models.DateField()
    status = models.IntegerField(choices=opciones)
    firma = models.TextField(blank=True)
    recibio = models.CharField(max_length=50, blank=True)
    image_1 = models.ImageField(upload_to='completos', null=True, blank=True)
    image_2 = models.ImageField(upload_to='completos', null=True, blank=True)
    image_3 = models.ImageField(upload_to='completos', null=True, blank=True)
    tecnico = models.ForeignKey(User, on_delete=models.CASCADE) 


    def __str__(self):
        return self.titulo