from django.shortcuts import render
from rest_framework import viewsets, serializers
from apps.decks.models import Deck
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    deck  = serializers.PrimaryKeyRelatedField(
        queryset = Deck.objects.all()
    )
    bucket = serializers.IntegerField(read_only=True)
    class Meta:
        model = Card
        fields = ('id', 'deck', 'question', 'answer','bucket', 'created_at', 'updated_at')

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
