from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name="movie_genre"
    )
    release_date = models.DateField(blank=True, null=True)
    actors = models.ManyToManyField(Actor, related_name="actor_movie")
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
