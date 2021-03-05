from django.shortcuts import render
from rest_framework import viewsets, serializers
from apps.decks.models import Deck
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    deck  = serializers.PrimaryKeyRelatedField(
        queryset = Deck.objects.all()
    )
    class Meta:
        model = Card
        fields = ('id', 'deck', 'question', 'answer')

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
