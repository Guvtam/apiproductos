from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(null=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre