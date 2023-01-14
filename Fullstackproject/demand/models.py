from django.db import models

# Create your models here.
class AllJobsStats(models.Model):
    year = models.IntegerField()
    averageSalary = models.DecimalField(decimal_places = 2,max_digits= 13)
    vacanciesAmount = models.IntegerField()


class FullStackStats(models.Model):
    year = models.IntegerField()
    averageSalary = models.DecimalField(decimal_places = 2,max_digits= 13)
    vacanciesAmount = models.IntegerField()

class StatsImages(models.Model):
    allImg = models.ImageField(upload_to="media", null= True)
    fullStackImg = models.ImageField(upload_to="media", null= True)
    def __str__(self):
        return str(self.allImg)
