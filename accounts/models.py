from django.db import models
from django.contrib.auth import models as auth_models
from accounts.manager import CustomUserManager


# Create your models here.

class CustomUser(auth_models.AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


class Profile(models.Model):
    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE
    )

    occupation = models.CharField(max_length=40),
    profile_picture = models.URLField(blank=True, null=True),
    interests = models.CharField(max_length=100, blank=True, null=True)




