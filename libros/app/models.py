from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=10,null=False,default='')

class Usuario(models.Model):
    nombre = models.CharField(max_length=20);
    apellido = models.CharField(max_length=20)
    rut = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, default='')
    email = models.EmailField()
    password = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)
    terminos = models.BooleanField(default=True)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE,null=True)
    estado = models.BooleanField()

class Genero(models.Model):
    nombre = models.CharField(max_length=20,default='',null=False)


class Libro(models.Model):
    imagen = models.URLField()
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=150,default='')
    usuario = models.ForeignKey(User,max_length=150,on_delete=models.CASCADE,default='',null=True)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE,null=True,default='')

    def __str__(self) -> str:
        return f'{self.nombre} -> {self.precio}'
    
	