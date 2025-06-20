from django.urls import path
from .views import MovieCreateListView, MovieRetrieveUpdateDestroyView, MovieStatsView

urlpatterns = [
    path("movies/", MovieCreateListView.as_view(), name="movie-create-list"),
    path(
        "movies/<int:pk>", MovieRetrieveUpdateDestroyView.as_view(), name="movie-detail"
    ),
    path("movies/stats/", MovieStatsView.as_view(), name="moview-stats"),
]
