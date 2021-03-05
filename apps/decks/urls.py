from django.urls import path, include
from rest_framework import routers
from .views import DeckViewSet

router = routers.DefaultRouter()
router.register(r'', DeckViewSet)

urlpatterns = [
    path('', include(router.urls)),
]