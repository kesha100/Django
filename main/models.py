from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200)
    producer = models.CharField(max_length=100)
    rating = models.FloatField()
    duration = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return self.title