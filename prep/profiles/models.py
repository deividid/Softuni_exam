from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import username_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2), username_validator],
    )

    email = models.EmailField()

    age = models.PositiveSmallIntegerField()

