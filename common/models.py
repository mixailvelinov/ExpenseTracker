from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.


class Wish(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(1.00)])
    is_bought = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    image = models.URLField(null=True, blank=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

