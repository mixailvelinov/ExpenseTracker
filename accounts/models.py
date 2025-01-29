from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models import Sum

from accounts.manager import CustomUserManager
from accounts.validators import name_validator


# Create your models here.

class CustomUser(auth_models.AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    objects = CustomUserManager()

    first_name = models.CharField(
        max_length=150,
        validators=[
            name_validator
        ]
    )

    last_name = models.CharField(
        max_length=150,
        validators=[
            name_validator
        ]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    @property
    def balance(self):
        total_deposits = self.deposit_set.aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = self.expense_set.aggregate(Sum('amount'))['amount__sum'] or 0
        bought_stuff = self.wish_set.filter(is_bought=True).aggregate(Sum('price'))['price__sum'] or 0
        result = total_deposits - total_expenses - bought_stuff
        return f"{result:.2f}"


class Profile(models.Model):
    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE
    )

    occupation = models.CharField(max_length=40),
    profile_picture = models.URLField(blank=True, null=True),
    interests = models.CharField(max_length=100, blank=True, null=True)




