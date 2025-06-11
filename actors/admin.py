from django.contrib import admin
from .models import Actor, Nationality


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nationality",
    )
    search_fields = ("nationality",)
    verbose_name = "Nationality"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "birthday", "nationality")
    search_fields = ("name", "birthday", "nationality")
    verbose_name = "Actor"
