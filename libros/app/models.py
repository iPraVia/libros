from django.db import models

# Create your models here.



class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=10,null=False,default='')

class Usuario(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE,null=True)
    estado = models.BooleanField()



class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

class Libro(models.Model):
	nombre = models.CharField(max_length=200)
	precio = models.FloatField()
	imagen = models.URLField(max_length=200)

	def __str__(self):
		return self.nombre

=======
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

class Libro(models.Model):
	nombre = models.CharField(max_length=200)
	precio = models.FloatField()
	def __str__(self) -> str:
         return f'{self.nombre} -> {self.precio}'
    
	


	
>>>>>>> 8e1dd5e4fd46d5bc80a0edf9cadf549a02d621ce
