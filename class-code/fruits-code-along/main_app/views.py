from django.shortcuts import render

# Create your views here.
def test_route(request):
    return render(request, 'testing.html')


# set up a route

# 1. create a view function
# 2. create the html file that corresponds
# 3. add the view in the urls.py