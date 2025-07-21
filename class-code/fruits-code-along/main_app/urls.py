from django.urls import path
from . import views
from .views import FruitListView, FruitCreateView

urlpatterns = [
    path('test/', views.test_route),
    # path('fruits/', views.all_fruits),
    path('fruits/<int:id>/', views.show_fruit),
    # path("fruits/create/",views.create_fruit),
    path("fruits/delete/<int:id>",views.delete_fruit),
    path("fruits/edit/<int:id>",views.edit_fruit),

    path("fruits/update/<int:id>",views.update_fruit),


    # class based view
    path("fruits/",FruitListView.as_view()),
    path("fruits/create/", FruitCreateView.as_view())
]
