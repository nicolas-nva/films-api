from django.db import models

class Nationality(models.Model):
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.nationality
    
    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"


class Actor (models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null = True, blank=True)
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.PROTECT,
        related_name="actor_nationality"
    )

    def __str__(self): 
        return self.name
