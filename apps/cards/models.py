from django.db import models
from apps.decks.models import Deck
from apps.utils.models import Timestamps

class Card(Timestamps, models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    buckets = (
        (1, '1 Day'),
        (2, '3 Days'),
        (3, '7 Days'),
        (4, '16 Days'),
        (5, '30 Days'),
    )
    bucket = models.IntegerField(choices=buckets, default=1)
    next_review_at = models.DateTimeField(auto_now_add=True)
    last_reviwed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.question