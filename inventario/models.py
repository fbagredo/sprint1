from django.db import models
from django.utils import timezone

class Proveedor(models.Model):
    
    tipoIdentificacion = models.CharField(max_length=2)
    numeroIdentificacion = models.TextField()
    nombre = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    email = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    
    tipoIdentificacion = models.CharField(max_length=2)
    numeroIdentificacion = models.TextField()
    nombre = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    email = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):

    nombre = models.TextField()
    descripcion = models.TextField()
    tipoProducto = models.TextField()
    medidas = models.TextField()
    proveedor = models.ManyToManyField(Proveedor)
    cliente = models.ManyToManyField(Cliente)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
    