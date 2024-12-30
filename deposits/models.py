from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Deposit(models.Model):
    amount = models.FloatField(
        validators=[MinValueValidator(1)]
    )

    date = models.DateTimeField(auto_now=True)

    description = models.CharField(max_length=75)

    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

