from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    
    return HttpResponse("Hello, world. You're at the productos index.")