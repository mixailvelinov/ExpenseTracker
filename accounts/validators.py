from django.core.exceptions import ValidationError


def name_validator(value):
    if not value.isalpha():
        raise ValidationError('The name should contain only letters.')

    if len(value) < 2:
        raise ValidationError(f'The name should be at least 2 letters long. {value} is too short.')