from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Tecnico(AbstractUser):


    #temporalmente no necesaria la foto
    profilePicture = models.ImageField(upload_to='usuarios', null=True, blank=True)



    groups = models.ManyToManyField(Group, related_name='visitor_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='visitor_user_permissions')

    class Meta:
        verbose_name_plural = 'Visitors'


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
    
