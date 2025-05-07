from django.db import models
from django.core.exceptions import ValidationError

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.precio < 0:
            raise ValidationError('El precio no puede ser negativo.')
