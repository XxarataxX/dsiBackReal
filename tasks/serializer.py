from rest_framework import serializers
from .models import Tarea

class MiModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class ConditionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

    def validate(self, attrs):
        instance = Tarea(**attrs)
        instance.clean()
        return attrs
    
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'