from django.urls import path, include
from .views import FruitViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'fruits',FruitViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]
