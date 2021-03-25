from django.db import models
import datetime


# Create your models here.
class Scores(models.Model):
    score = models.IntegerField(
        max_length=20,
        default=0
    )
    origin = models.CharField(
        max_length=20
    )
    date = models.DateField(
        default=datetime.date.today(),
    )
