from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Expense(models.Model):
    amount = models.FloatField(
        validators=[MinValueValidator(1)]
    )

    expense_name = models.CharField(max_length=75)

    description = models.CharField(max_length=75)

    date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)



