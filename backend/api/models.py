from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#clase del orm para la creacion de libros
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    #el related_name me permite user.notes()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="libro")

    def __str__(self):
        return self.titulo
