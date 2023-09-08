from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializer import MiModeloSerializer, TareaSerializer
from .models import Tarea

# Create your views here.
class ConditionListApiView(generics.ListAPIView):

    serializer_class = MiModeloSerializer

    def get_queryset(self):
        return Tarea.objects.all()
    
# Create your views here.
class DetailTarea(generics.RetrieveAPIView):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'
    
    
class ListTareaTecnico(generics.ListAPIView):

    serializer_class = TareaSerializer

    def get_queryset(self):
        # Obtén el ID del técnico desde la URL
        tecnico_id = self.kwargs['tecnico_id']
        
        # Filtra las tareas donde el campo 'tecnico' sea igual al ID del técnico
        return Tarea.objects.filter(tecnico=tecnico_id)