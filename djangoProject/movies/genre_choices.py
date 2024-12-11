from django.db import models


class GenreChoices(models.TextChoices):

    ACTION = "Action", "Action"
    COMEDY = "Comedy", "Comedy"
    CRIME = "Crime", "Crime"
    Romance = "Romance", "Romance"
    SCIFI = "Sci-fi", "Sci-fi"
    ADVENTURE = "Adventure", "Adventure"
    HORROR = "Horror", "Horror"
    DRAMA = "Drama", "Drama"
    Animation = "Animation", "Animation"
    MUSICAL = "Musical", "Musical"
    WESTERN = "Western", "Western"

