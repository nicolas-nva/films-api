from django.urls import path, include
from .views import *

urlpatterns = [
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),
    ]