from django.db import models

# Create your models here.

class SalaryInCity(models.Model):
    city = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class SalaryVacancies(models.Model):
    city = models.CharField(max_length=100)
    vacancies = models.IntegerField()
class Image(models.Model):
    image = models.ImageField(upload_to="media", null= True)

