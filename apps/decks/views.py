from datetime import date

from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.response import Response

from .models import Deck
from apps.cards.models import Card
from apps.cards.views import CardSerializer

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'title', 'description','created_at', 'updated_at')

class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

class CardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        queryset = Card.objects.filter(deck=decks_pk)
        serializers = CardSerializer(queryset, many=True)
        return Response(serializers.data)

class TodaysCardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        today = date.today()
        queryset = Card.objects.filter(
            deck=decks_pk,
            next_review_at__day=today.day
        )
        serializers = CardSerializer(queryset, many=True)
        return Response(serializers.data)