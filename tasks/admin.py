from django.contrib import admin

# Register your models here.
from tasks.models import Tarea

admin.site.register(Tarea)