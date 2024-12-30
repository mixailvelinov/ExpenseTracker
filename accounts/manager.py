from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You can't register without an email!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        username = extra_fields.get('username', email.split('@')[0])
        if self.model.objects.filter(username=username).exists():
            raise ValidationError(f"Username '{username}' is already taken.")

        return self.create_user(email, password, username=username, **extra_fields)