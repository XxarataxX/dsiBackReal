from django.shortcuts import render
from rest_framework import generics
from .serializer import MiModeloSerializer
from .models import Tarea

# Create your views here.
class ConditionListApiView(generics.ListAPIView):

    serializer_class = MiModeloSerializer

    def get_queryset(self):
        return Tarea.objects.all()
    
# Create your views here.
class DetailTarea(generics.ListAPIView):

    serializer_class = MiModeloSerializer

    def get_queryset(self):
        return Tarea.objects.all()
    