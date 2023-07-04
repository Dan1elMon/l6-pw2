

# Create your models here.
from django.db import models

class DestinosTuristicos(models.Model): 
     # Atributos del modelo
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to='destinos/')
    precioTour = models.DecimalField(max_digits=8, decimal_places=2)
    ofertaTour = models.BooleanField()

    def __str__(self):
        return self.nombreCiudad

    class Meta:
        app_label = 'travello'  # Etiqueta de aplicación explícita