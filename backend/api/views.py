from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Libro

# Create your views here.

#clase para la creacion de usuarios (ya incluido en el framework)
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #verificamos que no existe ya el user
    serializer_class = UserSerializer #especificamos que tipo de datos necesitamos para la creacion
    permission_classes = [AllowAny] #especifiacomes quien puede llamar a esta funcion
    #con estos parametros se hace la creacion automatica


#Crear un libro (COMING SOON )