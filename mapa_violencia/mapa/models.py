from django.db import models

# Create your models here.

#Model with one line for every crime commited
class Crime(models.Model):
    bairro = models.CharField(max_length=200)
    local_fato = models.CharField(max_length=200)
    enquadramento = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

#One line for every neighborhood
class Bairro(models.Model):
    bairro = models.CharField(max_length=200, unique=True)
    date_creation = models.DateField()
    area = models.DecimalField(max_digits=7, decimal_places=2)
    population = models.DecimalField(max_digits=7, decimal_places=2)
    density = models.DecimalField(max_digits=7, decimal_places=2)
    income = models.DecimalField(max_digits=7, decimal_places=2)
