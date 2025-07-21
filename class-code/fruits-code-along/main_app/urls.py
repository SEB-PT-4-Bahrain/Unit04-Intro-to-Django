from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_route),
    path('fruits/', views.all_fruits),
    path('fruits/<int:id>/', views.show_fruit),
    path("fruits/create/",views.create_fruit),
    path("fruits/delete/<int:id>",views.delete_fruit)
]
