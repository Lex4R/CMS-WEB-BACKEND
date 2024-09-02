from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Libro

#para el manejo de los jsons
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ["id", "titulo", "fecha", "autor"]
        extra_kwargs ={"autor": {"read_only": True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only":True}}
    
    #para el registro una vez se convierte al modelo user validate_data ya comprueba si esta todo correcto en la clase userSerializer
    def create (self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    