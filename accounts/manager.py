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

        # Set the username based on the email if it's not provided
        username = extra_fields.get('username')
        if not username:
            username = email.split('@')[0]  # Use part of the email as the default username

        # Check if username already exists
        if self.model.objects.filter(username=username).exists():
            raise ValidationError(f"Username '{username}' is already taken.")

        # Pass the username as part of extra_fields instead of explicitly as an argument
        extra_fields['username'] = username

        return self.create_user(email, password, **extra_fields)
