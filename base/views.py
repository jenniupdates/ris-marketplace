from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

products = [
      {'id': 1, 'name': 'clean dreamy belt', 'price': 15},
      
] 

def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')