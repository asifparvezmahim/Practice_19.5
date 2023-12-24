from django.db import models


# Create your models here.
class Musician(models.Model):
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=11)
    Instrument_Type = models.CharField(max_length=20)

    def __str__(self):
        return self.First_Name
