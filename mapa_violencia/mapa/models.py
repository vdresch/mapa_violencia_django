from django.db import models

# Create your models here.

class Crime(models.Model):
    bairro = models.ForeignKey(
        "Bairro", on_delete=models.CASCADE)
    local_fato = models.CharField(max_length=200)
    enquadramento = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

class Bairro(models.Model):
    bairro = models.CharField(max_length=200)
    date_creation = models.DateField()
    area = models.DecimalField(max_digits=7, decimal_places=2)
    popularion = models.DecimalField(max_digits=7, decimal_places=2)
    densidade = models.DecimalField(max_digits=4, decimal_places=2)
    income = models.DecimalField(max_digits=4, decimal_places=2)
