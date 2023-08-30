from django.db import models
from datetime import date

class Pet(models.Model):
    name = models.CharField(max_length = 255)
    especie = models.CharField(max_length = 255)
    nacimiento = models.DateField(default = date(1900, 1, 1))
    num_vac = models.IntegerField(null = True)
