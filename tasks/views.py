from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .serializer import MiModeloSerializer, UserSerializer
from .models import Tarea, Tecnico
from django.shortcuts import get_object_or_404


import base64
from PIL import Image
import io

from django.core.files.base import ContentFile
from .serializer import MiModeloSerializer, TareaSerializer
from .models import Tarea

# Create your views here.
class ConditionListApiView(generics.ListAPIView):

    serializer_class = MiModeloSerializer

    def get_queryset(self):
        return Tarea.objects.all()
    
class UserListApiView(generics.ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        return Tecnico.objects.all()
    
class VisitorDetailCorreoClave(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        clave = self.kwargs['clave']
        correo = self.kwargs['correo']
        
        obj = get_object_or_404(Tecnico, password=clave, email=correo)
        return obj
    
# Create your views here.
class DetailTarea(generics.RetrieveAPIView):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'
    
    
class ListTareaTecnico(generics.ListAPIView):

    serializer_class = TareaSerializer

    def get_queryset(self):
        tecnico_id = self.kwargs['tecnico_id']
        
        # Filtra las tareas donde el campo 'tecnico' sea igual al ID del técnico
        return Tarea.objects.filter(tecnico=tecnico_id)

class TareaUpdateView(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = MiModeloSerializer

    lookup_field = 'pk' 

    def resize_image(self, image_base64, max_size=200):
        try:
            image_data = base64.b64decode(image_base64)
            image = Image.open(io.BytesIO(image_data))

            # Obtiene el tamaño original de la imagen
            width, height = image.size

            # Calcula las nuevas dimensiones para el reescalado
            if width > height:
                new_width = max_size
                new_height = int(height * (max_size / width))
            else:
                new_width = int(width * (max_size / height))
                new_height = max_size

            # Redimensiona la imagen sin anti-aliasing
            resized_image = image.resize((new_width, new_height), Image.NEAREST)

            # Convierte la imagen redimensionada de nuevo a bytes
            output_buffer = io.BytesIO()
            resized_image.save(output_buffer, format='PNG')
            image_data = output_buffer.getvalue()

            return ContentFile(image_data, 'resized_image.png')

        except Exception as e:
            print(e)
            return None


    def put(self, request, *args, **kwargs):
        tarea = self.get_object()

        image_fields = ['image_1', 'image_2', 'image_3']
        for field_name in image_fields:
            image_base64 = request.data.get(f'{field_name}_base64')
            image_base64 = image_base64 + "=="

            if image_base64:
                resized_image = self.resize_image(image_base64)
                if resized_image:
                    setattr(tarea, field_name, resized_image)
                else:
                    return Response({'error': 'Error al procesar la imagen base64.'}, status=status.HTTP_400_BAD_REQUEST)

        firma_base64 = request.data.get('firma_base64')
        firma_base64 = firma_base64 + "=="
        print(firma_base64)
        if firma_base64:
            try:
                # Decodifica la firma base64
                firma_data = base64.b64decode(firma_base64)

                # Guarda la firma en formato SVG directamente
                tarea.firma = ContentFile(firma_data, 'firma.svg')
            except Exception as e:
                print(e)
                return Response({'error': 'Error al procesar la firma base64.'}, status=status.HTTP_400_BAD_REQUEST)

        correo = request.data.get('correo')
        cliente = request.data.get('cliente')
            
        tarea.recibio = cliente
        tarea.correo = correo
        
        tarea.save()
        serializer = self.get_serializer(tarea)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # Obtén el ID del técnico desde la URL
        