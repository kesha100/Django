from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Режиссёры'
        verbose_name_plural = 'Режиссёр'

    def __str__(self):
        return self.name


class Film(models.Model):
    class Meta:
        ordering = ['title', 'rating', 'duration']
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    title = models.CharField(max_length=200, verbose_name='Название')
    producer = models.CharField(max_length=100, verbose_name='Продюсер')
    rating = models.FloatField(verbose_name='Оценка')
    duration = models.CharField(max_length=50, verbose_name='Длительность')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director', verbose_name='Режиссёр')

    def __str__(self):
        return self.title