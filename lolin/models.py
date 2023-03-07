from django.db import models


# Create your models here.

class ClassName(models.Model):
    name = models.CharField(max_length=12)
    year = models.DateField()


class Students(models.Model):
    name = models.CharField(max_length=48)
    age = models.IntegerField()
    className = models.ForeignKey(ClassName, on_delete=models.CASCADE)
