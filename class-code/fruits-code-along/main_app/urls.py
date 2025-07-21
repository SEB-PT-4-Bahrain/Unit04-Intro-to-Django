from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_route),
    path('fruits/', views.all_fruits)
]
