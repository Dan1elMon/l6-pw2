from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to='destinos')
    precioTour = models.DecimalField(max_digits=8, decimal_places=2)
    ofertaTour = models.BooleanField(default=False)