from django.contrib import admin

# Register your models here.
from tasks.models import Tarea, Tecnico

admin.site.register(Tarea)
admin.site.register(Tecnico)