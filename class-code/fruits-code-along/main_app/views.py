from django.shortcuts import render, redirect
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


# def all_fruits(request):
        
#         fruits = Fruit.objects.all() #method to get all fruits
        
#         return render(request,"all-fruits.html",{"fruits":fruits})

def show_fruit(request,id):
      fruit = Fruit.objects.get(id =id)
      return render(request,'show-fruit.html',{"fruit":fruit})


def create_fruit(request):
      if request.method == "POST":
            print("isReadyToEat" in request.POST)
            name = request.POST['name']
            is_ready_to_eat = "isReadyToEat" in request.POST

            # save to the database
            Fruit.objects.create(name=name, is_ready_to_eat=is_ready_to_eat)
            return redirect("/fruits/")


def delete_fruit(request,id):
      fruit = Fruit.objects.get(id=id)
      fruit.delete() #deletes a fruit from the database
      return redirect("/fruits")

def edit_fruit(request,id):
      fruit = Fruit.objects.get(id=id)
      return render(request,"update-fruit.html",{"fruit":fruit})

def update_fruit(request,id):
      fruit = Fruit.objects.get(id = id)
      if request.method == "POST":
            fruit.name = request.POST['name']
            fruit.is_ready_to_eat = "isReadyToEat" in request.POST
            fruit.save()
            return redirect("/fruits")

# set up a route

# 1. create a view function
# 2. create the html file that corresponds
# 3. add the view in the urls.py




# class based views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class FruitListView(ListView):
      model = Fruit
      template_name = "all-fruits.html"
      context_object_name = "fruits"



class FruitCreateView(CreateView):
      model = Fruit
      template_name = "all-fruits.html"
      fields = ["name","is_ready_to_eat"]
      success_url = "/fruits"