from django.db import models

# Create your models here.



class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=10,null=False,default='')

class Usuario(models.Model):
    nombre = models.CharField(max_length=10);
    email = models.EmailField();
    password = models.CharField(max_length=10);
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE,null=True)
    estado = models.BooleanField()


class Libro(models.Model):
	nombre = models.CharField(max_length=200)
	precio = models.FloatField()
	def __str__(self) -> str:
         return f'{self.nombre} -> {self.precio}'
    
	


	
    


