from django.db import models
from django.core.validators import MinValueValidator


class Direction(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    sort_number = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    directions = models.ManyToManyField(Direction, related_name='directions')
    description = models.TextField()
    birthdate = models.DateField()
    experience = models.IntegerField(validators=[MinValueValidator(0)])
    sort_number = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

