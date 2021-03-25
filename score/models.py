from django.db import models


# Create your models here.
class Scores(models.Model):
    score = models.IntegerField(
        max_length=20,
        default=0
    )
    predict = models.CharField(
        max_length=20
    )
