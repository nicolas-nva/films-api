from django.urls import path
from .views import *

urlpatterns = [
    path ('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>',GenreRetrieveUpdateDestroyView.as_view(),name = 'genre-detail'),
]