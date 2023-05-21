from django.db import models

# Create your models here.

class TiposProductos(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion



class Producto(models.Model):
     nombre = models.CharField(max_length=200)
     precio = models.IntegerField()
     stock = models.IntegerField()
     descripcion = models.CharField(max_length=200)
     tipo = models.ForeignKey(TiposProductos, on_delete=models.CASCADE)
     imagen = models.ImageField(null=True,blank=True)
     vigente = models.BooleanField()

     def __str__(self):
      return self.nombre
     
class Empleado(models.Model):
    nombreEmp = models.CharField(max_length=100)
    edad = models.IntegerField()
    rut = models.CharField(max_length=11)
    direccion = models.CharField(max_length=100) 
    correo = models.CharField(max_length=100) 

    def __str__(self):
      return self.nombreEmp

    
class Cliente(models.Model):
    nombreCli = models.CharField(max_length=100)
    edad = models.IntegerField()
    rut = models.CharField(max_length=11)
    direccion = models.CharField(max_length=100) 
    correo = models.CharField(max_length=100) 

    def __str__(self):
      return self.nombreCli
    
class Subscripcion(models.Model):
    nombreSubs = models.CharField(max_length=100)
    correo = models.CharField(max_length=100) 
    rut = models.CharField(max_length=11)

    def __str__(self):
      return self.nombreSubs
    

class Historial(models.Model):
    nombreProducto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100) 
    precio = models.IntegerField()
    pago = models.CharField(max_length=100)

    def __str__(self):
      return self.nombreProducto    