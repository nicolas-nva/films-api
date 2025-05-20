from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'genre', 'release_date', 'resume')
    list_filter = ('title', 'genre', 'release_date')
    verbose_name = ('Filmes')
