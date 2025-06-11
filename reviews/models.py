from django.db import models
from movies.models import Movie


class StarRating(models.IntegerChoices):
    ONE = 1, "★☆☆☆☆"
    TWO = 2, "★★☆☆☆"
    THREE = 3, "★★★☆☆"
    FOUR = 4, "★★★★☆"
    FIVE = 5, "★★★★★"


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name="movie_review"
    )
    nota = models.IntegerField(choices=StarRating.choices, default=StarRating.THREE)
    comment = models.TextField(null=True, blank=True)
