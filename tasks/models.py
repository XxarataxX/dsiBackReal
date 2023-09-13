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

class Historial_pagos(models.Model):
       
       tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE)
       
       pago_porcentaje = models.IntegerField(null=True, blank=True)
       
       def __str__(self):
        return self.tarea.titulo

class Tarea(models.Model):

    opciones = (
        (1, 'Pendiente'),
        (2, 'Completada'),
        (3, 'En Proceso'),
        (4, 'cancelada')
    )
    
    opciones_pagado = (
        (1, 'no pagado'),
        (2, 'cobrado'),
        (3, 'cancelada')
    )

    opciones_factura = (
        (1, 'no facturado'),
        (2, 'facturado')
    )


    titulo = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    fecha_creacion = models.DateField(default=date.today)
    fecha_vencimiento = models.DateField()
    status = models.IntegerField(choices=opciones, default= 1)
    firma = models.ImageField(upload_to='firmas', null=True, blank=True)
    recibio = models.CharField(max_length=50, blank=True)
    image_1 = models.ImageField(upload_to='completos', null=True, blank=True)
    image_2 = models.ImageField(upload_to='completos', null=True, blank=True)
    image_3 = models.ImageField(upload_to='completos', null=True, blank=True)
    image_persona = models.ImageField(upload_to='completos', null=True, blank=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE) 
    correo = models.CharField(max_length=50, default="", null=True, blank=True)
    estatus_pago = models.IntegerField(choices=opciones_pagado, default=1)
    estatus_Factura = models.IntegerField(choices=opciones_factura, default=1)
    no_Factura = models.CharField(max_length=50, default="", null=True, blank=True)
    no_Factura_nota = models.CharField(max_length=50, default="", null=True, blank=True)

    porcentaje_de_pago= models.IntegerField(null=True, blank=True)
    notas_tecnico = models.TextField(null=True, blank=True)
    def save(self, *args, **kwargs):
       # Lógica para crear o modificar un registro en Historial_pagos

        print(f'Se ha creado o modificado una tarea: {self.pk}')
        # Por ejemplo:
        tarea_existente = Tarea.objects.get(pk=self.pk)
        historial_pago = Historial_pagos.objects.create(tarea=tarea_existente, pago_porcentaje=self.porcentaje_de_pago)
        historial_pago.save()

    def __str__(self):
        return self.titulo
    
class PDFGenerado(models.Model):
    name = models.CharField(max_length=150)
    # Modelo para almacenar los PDF generados
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='pdfs/')
    
    class Meta:
        # Agregar una restricción única en la ForeignKey para que solo pueda haber un PDF por tarea
        unique_together = ('tarea', )


    

