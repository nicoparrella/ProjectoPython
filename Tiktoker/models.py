from django.db import models

# Create your models here.
class Tiktoker(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"