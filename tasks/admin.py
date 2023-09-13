from django.contrib import admin

# Register your models here.
from tasks.models import Tarea, Tecnico, PDFGenerado

admin.site.register(Tarea)
admin.site.register(Tecnico)
admin.site.register(PDFGenerado)