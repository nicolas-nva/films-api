from rest_framework import serializers
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1990!"
            )
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                "Resumo deve ter menos que 200 caracteres!"
            )
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    stars = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "actors", "release_date", "rate", "resume"]

    def get_rate(self, obj):
        rate = obj.movie_review.aggregate(Avg("nota"))["nota__avg"]

        if rate:
            return rate

        return None

    def get_stars(self, obj):
        rate = self.get_rate(obj)
        if rate is not None:
            full_stars = "★" * int(round(rate))
            empty_stars = "☆" * (5 - int(round(rate)))
            return full_stars + empty_stars
        return "No reviews"
