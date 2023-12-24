from django.db import models
from musician.models import Musician


# Create your models here.
class Album(models.Model):
    Album_Name = models.CharField(max_length=20)
    Album_Release_Date = models.DateTimeField()
    choicesValue = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    Rating = models.PositiveSmallIntegerField(choices=choicesValue)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.Album_Name
