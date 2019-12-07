from django.db import models

# Create your models here.
class DatosPersona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    mensaje = models.CharField(max_length=200)

    def Datos(self):
        cadena = "{0}, {1}, {2}, {3}"
        return cadena.format(self.nombres, self.apellidos, self.direccion, self.email)

    def __str__(self):
        return self.Datos()