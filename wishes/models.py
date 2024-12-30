from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Wish(models.Model):
    name = models.CharField(max_length=75)

    amount = models.FloatField(
        validators=[MinValueValidator(1)]
    )

    description = models.CharField(max_length=75)

    date = models.DateTimeField(auto_now=True)

