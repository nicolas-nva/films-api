from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def delete(self, *args, **kwargs):
         instance = self.get_object()
         try: 
             instance.delete() 
             return Response(
             {'message': 'Deletado com sucesso.'}, status=204); 
         except Exception as e: 
             return Response(
             {'error': str(e)}, status=500)
