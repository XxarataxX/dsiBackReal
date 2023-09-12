from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser, Group, Permission



# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    firma = models.ImageField(upload_to='firmas', null=True, blank=True)
    recibio = models.CharField(max_length=50, blank=True)
    image_1 = models.ImageField(upload_to='completos', null=True, blank=True)
    image_2 = models.ImageField(upload_to='completos', null=True, blank=True)
    image_3 = models.ImageField(upload_to='completos', null=True, blank=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE) 
    correo = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.titulo
    
class PDFGenerado(models.Model):
    name = models.CharField(max_length=150)
    # Modelo para almacenar los PDF generados
    archivo = models.FileField(upload_to='pdfs/')


    

