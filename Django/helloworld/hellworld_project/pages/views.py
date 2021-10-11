from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Here, we wrote like whenever homepageview is called return the hello world.
def homepageView(request):
    return HttpResponse("Hello, World")