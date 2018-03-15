from django.db import models
from django.utils import timezone

class Producto(models.Model):

    nombre = models.TextField()
    descripcion = models.TextField()
    tipoProducto = models.TextField()
    medidas = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
    
class Imagen(models.Model):
    
    linkImgen = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.linkImgen
    
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
    
class registroProducto(models.Model):
    
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=20, decimal_places=2, default="")
    cantidadDisponible = models.IntegerField()

    
    def publish(self):
        self.save()
        
    def __str__(self):
        return str(proveedor) + " " + str(producto)  

    
class imagenProducto(models.Model):
    
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

