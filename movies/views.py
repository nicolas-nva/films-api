from rest_framework import generics
from rest_framework.response import Response
from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def delete(self, *args, **kwargs):
         instance = self.get_object()
         try: 
             instance.delete() 
             return Response(
             {'message': 'Deletado com sucesso.'}, status=204); 
         except Exception as e: 
             return Response(
             {'error': str(e)}, status=500)