from rest_framework import generics
from rest_framework.response import Response
from genres.models import Genre
from genres.serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    def delete(self, *args, **kwargs):
         instance = self.get_object()
         try: 
             instance.delete() 
             return Response(
             {'message': 'Deletado com sucesso.'}, status=204); 
         except Exception as e: 
             return Response(
             {'error': str(e)}, status=500)
