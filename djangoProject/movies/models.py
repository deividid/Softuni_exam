from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import CustomUser
from movies.genre_choices import GenreChoices


# Create your models here.


class Director(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2)],
    )

    last_name = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2)],
    )

    birth_date = models.DateField()

    picture = models.URLField()

    is_active = models.BooleanField(
        default=True,
    )

    country_of_origin = models.CharField(
        max_length=15,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

    uploaded_by = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="uploaded_directors",
    )

    @property
    def get_movie_names(self):
        movie_names = []
        for movie in self.movies.all():
            movie_names.append(movie.title)

        return movie_names

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name


class Studios(models.Model):
    name = models.CharField(
        max_length=20,
    )

    picture_url = models.URLField()

    creation_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],

    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

    uploaded_by = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="uploaded_studios",
    )

    @property
    def get_movie_names(self):
        movie_names = []
        for movie in self.movies.all():
            movie_names.append(movie.title)

        return movie_names

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=70,
        unique=True,

    )

    poster = models.URLField()

    release_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2026)],
    )

    genre = models.CharField(
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    director = models.ForeignKey(
        to=Director,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="movies",
    )

    studio = models.ForeignKey(
        to=Studios,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="movies",
    )

    uploaded_by = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="uploaded_movies",
    )

    @property
    def get_comments(self):
        all_comments = self.comments.all()
        return all_comments


class Comment(models.Model):
    title = models.CharField(
        max_length=70,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    to_movie = models.ForeignKey(
        to=Movie,
        on_delete=models.CASCADE,
        related_name="comments",
    )