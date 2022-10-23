from django.db import models

# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=200)
    producer = models.CharField(max_length=100)
    rating = models.FloatField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title