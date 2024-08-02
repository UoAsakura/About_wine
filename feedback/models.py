from django.db import models
from django.urls import reverse
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator)
from django.utils.text import slugify


class Feedback(models.Model):
    name = models.CharField(max_length=20)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])


class ErrorMessage(models.Model):
    name = models.CharField(max_length=30)
    type_error = models.CharField(max_length=50)
    about_error = models.TextField()
    image = models.FileField(upload_to='error_gallery', blank=True)


class InfoMessage(models.Model):
    name = models.CharField(max_length=30)
    type_inaccuracy = models.CharField(max_length=50)
    about_inaccuracy = models.TextField()
    image = models.FileField(upload_to='info_gallery', blank=True)



