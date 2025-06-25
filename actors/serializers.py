from rest_framework import serializers
from .models import Actor


class ActorSerializer(serializers.ModelSerializer):
    nationality = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "name", "birthday", "nationality"]

    def get_nationality(self, obj):
        return obj.nationality.nationality
