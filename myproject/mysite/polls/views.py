from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
variable = "trying_something"

def index(request):
    return HttpResponse("Hello, World")
