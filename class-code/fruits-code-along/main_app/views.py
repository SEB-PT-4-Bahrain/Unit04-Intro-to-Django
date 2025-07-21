from django.shortcuts import render
from .models import Fruit

# Create your views here.
def test_route(request):
    print(request)
    fruits = [
        {"name":"Orange", "isReadyToEat":False},
        {"name":"Pineapple", "isReadyToEat":True},
        {"name":"Watermelon", "isReadyToEat":False}
        ]
    return render(request, 'testing.html',{"fruits":fruits})


def all_fruits(request):
        
        fruits = Fruit.objects.all()
        
        return render(request,"all-fruits.html",{"fruits":fruits})

# set up a route

# 1. create a view function
# 2. create the html file that corresponds
# 3. add the view in the urls.py