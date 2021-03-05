from django.urls import path, include
from rest_framework import routers
from .views import CardViewSet

router = routers.DefaultRouter()
router.register(r'', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]