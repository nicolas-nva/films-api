from django.urls import path
from .views import ReviewCreateListView, ReviewRetrieverUpdateDestroyView

urlpatterns = [
    path("reviews/", ReviewCreateListView.as_view(), name="review-create-list"),
    path(
        "reviews/<int:pk>",
        ReviewRetrieverUpdateDestroyView.as_view(),
        name="review-detail",
    ),
]
