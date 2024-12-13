from django.db import models


class GenreChoices(models.TextChoices):
    POP = 'Pop Music', 'Pop Music'
    ROCK = 'Rock Music', 'Rock Music'
    DANCE = 'Dance Music', 'Dance Music'
    JAZZ = 'Jazz Music', 'Jazz Music'
    COUNTRY = 'Country Music', 'Country Music'
    RNB = 'R&B Music', 'R&B Music'
    HIPHOP = 'Hip Hop Music', 'Hip Hop Music'
    OTHER = 'Other', 'Other'