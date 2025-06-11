from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Movie
from gemini_api.client import get_movie_resume


@receiver(pre_save, sender=Movie)
def movie_pre_save(sender, instance, **kwargs):
    if not instance.resume:
        ai_resume = get_movie_resume(
            instance.title, instance.genre, instance.release_date
        )
        instance.resume = ai_resume
