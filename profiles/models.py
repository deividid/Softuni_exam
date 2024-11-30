from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(
        max_length=15,
        validators=[MinValueValidator(2), RegexValidator(r'^[0-9a-zA-Z_]*$')],
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
