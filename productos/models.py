from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de Categoría")
    descripcion = models.TextField(help_text="Descripción detallada de la categoría")
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Producto")
    descripcion = models.TextField(help_text="Descripción detallada del producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['nombre']),
        ]
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15, help_text="Número de teléfono del cliente")
    email = models.EmailField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
      
      

