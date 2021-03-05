from django.db import models
from apps.utils.models import Timestamps


class Deck(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title