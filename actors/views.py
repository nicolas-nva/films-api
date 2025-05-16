from rest_framework import generics
from rest_framework.response import Response
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    def delete(self, *args, **kwargs):
         instance = self.get_object()
         try: 
             instance.delete() 
             return Response(
             {'message': 'Deletado com sucesso.'}, status=204); 
         except Exception as e: 
             return Response(
             {'error': str(e)}, status=500)