from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from app.permissions import GlobalDefaultPermissions
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return Response({"message": "Deletado com sucesso."}, status=204)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class MovieStatsView(views.APIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermissions,
    )
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )
        total_reviews = Review.objects.count()
        average = Review.movie_review.aggregate(Avg("nota"))["nota__avg"]
        return response.Response(
            data={
                "total_movies": total_movies,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                "average": round(average, 1) if average else 0,
            },
            status=status.HTTP_200_OK,
        )
