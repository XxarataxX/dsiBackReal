from rest_framework import serializers
from .models import Tarea, Tecnico


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
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'