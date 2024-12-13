from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify


def username_validator(value):
    if value.lower() != slugify(value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
